
import logging
import math

import shutil
import copy



from pathlib import Path


import geopandas as gpd
import numpy as np
import pandas as pd


import osgeo.gdal as gdal
import ogr

from .object import create_maskedraster
log = logging.getLogger(__name__)


def split_parcels(input_gpkg, eotiled_gpkg_output_filename, output_dir, subtiles_count=10):
    do_split_save_gpkg(input_gpkg, eotiled_gpkg_output_filename, output_dir, subtiles_count)
    log.info(f"Done splitting parcels for {input_gpkg}")


def group_polygons_assigngroupid(gdf_input, check_overlap_only=False):
    gdf = copy.deepcopy(gdf_input)

    invalid_mask = ~gdf.geometry.is_valid
    gdf.loc[invalid_mask, 'geometry'] = gdf.loc[invalid_mask, 'geometry'].buffer(0)

    # Create a new column to store the group ID for each polygon
    gdf['group_id'] = -1

    group_id = 0
    # Iterate over each row in the GeoDataFrame
    for idx, row in gdf.iterrows():

        # Get the group ID of the current row
        if row['group_id'] != -1:
            row_group_id = row['group_id']
        else:
            row_group_id = group_id
            group_id += 1

        # Find all polygons that touch or intersect the current row's geometry
        if check_overlap_only:
            neighbors = gdf[gdf.touches(row['geometry']) | gdf.intersects(row['geometry'].buffer(1))]
        else:
            neighbors = gdf[gdf.intersects(row['geometry'].buffer(1))]

        # Check if any neighbors have a different group ID
        neighbor_group_ids = neighbors.loc[neighbors['group_id'] != -1, 'group_id']
        if not neighbor_group_ids.empty:
            # Get the unique group IDs of the neighbors
            unique_group_ids = neighbor_group_ids.unique()

            # Assign the current row's group ID to the neighbors with different group IDs
            gdf.loc[neighbors.index, 'group_id'] = row_group_id

            # Update the group ID for all polygons with the unique group IDs
            gdf.loc[gdf['group_id'].isin(unique_group_ids), 'group_id'] = row_group_id

        else:
            # Assign the current row's group ID to the neighbors with the default group ID
            gdf.loc[neighbors.index, 'group_id'] = row_group_id

    grouped_geoms = []
    for unique_group_id in gdf.group_id.unique():
        gdf_group_id = gdf.loc[gdf.group_id == unique_group_id]
        touching_geoms = []
        for idx, row in gdf_group_id.iterrows():
            touching_geoms.append(row)
        grouped_geoms.append(touching_geoms)
    return grouped_geoms


def add_indexed_to_gdf(gdfs, flattened_list, subtiles_count):
    gdf_count = 0
    for gdf_item in gdfs:
        if len(gdf_item) > 0:
            gdf_count += 1

    flattened_list_index = 0
    flattened_list_len = len(flattened_list)
    while gdf_count <= subtiles_count and flattened_list_len > flattened_list_index:
        gdfs[gdf_count] = pd.concat([gdfs[gdf_count], flattened_list[flattened_list_index]], ignore_index=True,
                                    sort=False)
        flattened_list_index += 1
        gdf_count += 1
    return gdfs


def add_flattened_to_gdf(gdfs, flattened_list):
    gdf_index = 1

    for list_index, list_item in enumerate(flattened_list):
        flattened_list_item_gdf = gpd.GeoDataFrame([flattened_list[list_index]])
        gdfs[gdf_index] = pd.concat([gdfs[gdf_index], flattened_list_item_gdf], ignore_index=True, sort=False)

        gdf_index += 1
        if gdf_index >= len(gdfs) - 1:
            gdf_index = 0
        if len(gdfs[gdf_index + 1]) == 0:
            gdf_index = 0
    return gdfs


def split_gdf_nonoverlap(gdf, subtiles_count, min_rows=2000):
    total_rows = len(gdf)
    if min_rows is None:
        min_rows = total_rows / subtiles_count
    max_rows_per_split = math.ceil(max(min_rows, total_rows / subtiles_count))
    splits = []
    for i in range(subtiles_count):
        start_idx = i * max_rows_per_split
        end_idx = min((i + 1) * max_rows_per_split, total_rows)
        split_gdf = gdf.iloc[start_idx:end_idx]
        splits.append(split_gdf)
    return splits


def check_parceloverlap_splitted_gdfs(gdfs_added, output_raster, parcel_list_master, work_dir, column_name):
    parcel_list = []
    for gdf_index, gdf_subset in enumerate(gdfs_added):

        if len(gdf_subset) != 0:
            output_file = work_dir.joinpath(f"{Path(output_raster).name}.flatten_added_{gdf_index}.gpkg")
            output_file.unlink(missing_ok=True)
            gdf_subset.to_file(output_file, driver='GPKG')

            raster_path = work_dir.joinpath(output_file.name.replace(".gpkg", ".tif"))
            shutil.copy(output_raster, raster_path)

            create_maskedraster(output_file, raster_path, touch_status="all_in", column_name=column_name)
            raster_ds = gdal.Open(str(raster_path))
            rasterized_parcels = np.unique(raster_ds.GetRasterBand(1).ReadAsArray())
            parcel_list.extend(rasterized_parcels)
            raster_ds = None

    missing_parcel = set(parcel_list_master).difference(set(parcel_list))
    return missing_parcel


def group_by_index(lst):
    grouped_lists = [gpd.GeoDataFrame() for _ in range(len(max(lst, key=len)))]

    for sublist in lst:
        for i, item in enumerate(sublist):
            gdf = gpd.GeoDataFrame([item])
            grouped_lists[i] = pd.concat([grouped_lists[i], gdf], ignore_index=True, sort=False)

    return grouped_lists


def split_geodataframe(gdf, subtiles_count, min_rows=750, split_overlap=False, input_gpkg=None, work_dir=None,
                       parcel_column='AZID'):
    if not split_overlap:
        splits = split_gdf_nonoverlap(gdf, subtiles_count, min_rows=min_rows)
        return splits

    else:

        gpkg_ds = ogr.Open(str(input_gpkg), 0)  # 0 for read-only mode
        extent = gdf.total_bounds

        # Define the pixel size
        pixel_size = 20
        # Specify the column to burn into the raster
        column_name = parcel_column

        driver = gdal.GetDriverByName('GTiff')
        rows = int((extent[3] - extent[1]) / pixel_size)
        cols = int((extent[2] - extent[0]) / pixel_size)

        output_raster_path = Path(work_dir).joinpath(f"{Path(input_gpkg).name}.tif")
        output_raster = driver.Create(str(output_raster_path), cols, rows, 1, gdal.GDT_Float32)
        output_raster.SetGeoTransform((extent[0], pixel_size, 0, extent[3], 0, -pixel_size))
        output_raster.SetProjection(gdf.crs.to_wkt())
        output_raster = None

        # rasterize
        masked_raster_path = Path(work_dir).joinpath(f"{Path(input_gpkg).name}_masked.tif")
        shutil.copy(output_raster_path, masked_raster_path)
        create_maskedraster(input_gpkg, masked_raster_path, touch_status="all_in", column_name=column_name)
        # gdal.RasterizeLayer(output_raster, [1], layer, options=['ATTRIBUTE=' + column_name, 'ATTRIBUTE=no_touch'])

        raster_ds = gdal.Open(str(masked_raster_path))
        rasterized_parcels = np.unique(raster_ds.GetRasterBand(1).ReadAsArray())

        gpkg_parcel_list = gdf[column_name].to_list()
        missing_parcel = set(gpkg_parcel_list).difference(set(rasterized_parcels))

        parcels_gdf_rasterized_parcels = gdf.loc[~gdf[column_name].isin(missing_parcel)]
        parcels_gdf_missing_parcels = gdf.loc[gdf[column_name].isin(missing_parcel)]

        gdfs = split_gdf_nonoverlap(parcels_gdf_rasterized_parcels, subtiles_count=subtiles_count, min_rows=min_rows)

        group_withid = group_polygons_assigngroupid(parcels_gdf_missing_parcels, check_overlap_only=True)
        indexgrouped = group_by_index(group_withid)
        gdfs_added = add_indexed_to_gdf(gdfs, indexgrouped, subtiles_count)
        missing_parcels_afterflattended_add = check_parceloverlap_splitted_gdfs(gdfs_added, output_raster_path,
                                                                                gpkg_parcel_list, work_dir,
                                                                                parcel_column)
        log.debug(missing_parcels_afterflattended_add)
        return gdfs_added, missing_parcels_afterflattended_add


def do_split_save_gpkg(input_gpkg, output_gpkg_basename, output_dir,
                       subtiles_count=14, min_parcels=None, split_overlap=False, work_dir=None, parcel_column='AZID'):
    logfilepath = output_dir.joinpath("tiling_log.txt")
    logfile = open(logfilepath, "w")
    logfile.write("--------------------------------\n")
    logfile.write("-SUBTILE PARCEL COUNT-\n")
    logfile.write("--------------------------------\n")

    gpkg_filename = Path(input_gpkg).name
    gpkg_ds = ogr.Open(str(input_gpkg))

    # Get the number of parcels
    layer_name = gpkg_ds.GetLayer().GetName()
    feature_count = gpkg_ds.GetLayer().GetFeatureCount()

    # Load the GeoPackage file into a GeoDataFrame
    gdf = gpd.read_file(input_gpkg, layer=layer_name)

    missing_parcels = None
    if min_parcels is None:
        # Divide the GeoDataFrame into n equal parts
        gdfs = np.array_split(gdf, subtiles_count)
    else:
        gdfs, missing_parcels = split_geodataframe(gdf, subtiles_count, min_parcels, split_overlap, input_gpkg,
                                                   work_dir, parcel_column)

    gpgk_paths = []
    # Write each subset of data to a new GeoPackage file
    parcel_count = 0
    for gdf_index, gdf_subset in enumerate(gdfs):

        number_of_parcels = len(gdf_subset)
        parcel_count += number_of_parcels

        if number_of_parcels != 0:
            output_file = output_dir.joinpath(output_gpkg_basename.replace(".gpkg", f"-{gdf_index + 1}.gpkg"))
            output_file.unlink(missing_ok=True)
            layer_name = gpkg_filename.replace(".gpkg", f"_{gdf_index + 1}.gpkg")
            gdf_subset.to_file(output_file, layer=layer_name, driver='GPKG')
            gpgk_paths.append(output_file)
        else:
            output_file = output_dir.joinpath(output_gpkg_basename.replace(".gpkg", f"-{gdf_index + 1}_NODATA.txt"))
            output_file.unlink(missing_ok=True)
            output_file.write_text("No parcel")
            gpgk_paths.append(output_file)
        logfile.write(f"{output_file} -- {number_of_parcels} \n")
    logfile.write("--------------------------------\n")
    logfile.write(f"PARCEL COUNT = {parcel_count}\n")
    logfile.write(f"missing parcel: {missing_parcels}")
    logfile.close()
    return gpgk_paths