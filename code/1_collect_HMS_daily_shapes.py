"""
This script downloads, concatenates, and saves to a combined shapefile 
the hms smoke plume shapefiles available at 
https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Smoke_Polygons/Shapefile.
It also produces a CSV with metadata for each date in the range specified.
"""
import urllib
import logging
from datetime import datetime

import requests
import pandas as pd
import geopandas as gpd
from tqdm import tqdm

# set up logger.
datestr = datetime.today().strftime("%Y%m%d")
logger = logging.getLogger(__name__)
logging.basicConfig(filename="hms_collection.log", 
                    format='%(message)s',
                    filemode="w")
logger.setLevel(logging.INFO)
logger.info(f"{datestr}\n\n")

def confirm_matching_crs(gdf_list):
    """
    Produce set of unique crs values from geodataframes in a list. Print and
    log a warning if more than one unique crs value is present.
    """
    crs_set = {gdf.crs for gdf in gdf_list}
    if len(crs_set) > 1:
        print("WARNING: MULTIPLE CRS VALUES DETECTED")
        print(crs_set)


# Define time period to collect. Here, collecting from earliest available to end of 2021.
start_date = datetime(2005, 8, 5)
end_date = datetime(2021, 12, 31)

dates = pd.date_range(start_date, end_date)

# create list to hold dataframes for each day
df_list = []
# create list to hold metadata for each dataframe
meta_list = []


for date in tqdm(dates):
    logger.info(date)
    # define date vars
    date_formatted = str(date.date())
    year = date.year
    month = date.month
    day = date.day
    # plug date vars into url
    url = f"https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Smoke_Polygons/Shapefile/{year}/{month:02}/hms_smoke{year}{month:02}{day:02}.zip"
    #try to collect file from that url. If this doesn't work, log it and skip to next date.
    try:
        tmp_df = gpd.read_file(url)
    except urllib.error.HTTPError:
        logger.info(f"No file for {date}")
        meta_dict = {"date": date_formatted, 
                     "year": year,
                     "missing": True}
        meta_list.append(meta_dict)
        continue
    except:
        meta_dict = {"date": date_formatted, 
                     "year": year,
                     "other_error": True}
        meta_list.append(meta_dict)
        logger.warning(f"Error for file {date}\n       error:", exc_info=True)
        continue
    # record date and year values in df as strings to enable saving to shapefile.
    tmp_df["date"] = date_formatted
    tmp_df['year'] = str(year)

    # record columns and projection of original dataframe and add to meta_dict
    meta_dict = {
        "date": date_formatted,
        "year": year,
        "columns": ", ".join(tmp_df.columns.values.tolist()),
        "entries":len(tmp_df),
        "crs": str(tmp_df.crs)
    }
    meta_list.append(meta_dict)
    # add to list
    df_list.append(tmp_df)

# concatenate daily dataframes into one dataframe.
hms_df = pd.concat(df_list).reset_index(drop=True)
# remove any empty columns.
hms_df = hms_df.dropna(how="all", axis=1)

# change Density datatype to float.
hms_df["Density"] = hms_df["Density"].astype(float)

#save data to file.
hms_df.to_file("../data/hms_smoke_shapes_2005_2021/hms_smoke_shapes_20050805_20211231.shp")

# produce dataframe of metadata records
meta_df = pd.DataFrame.from_records(meta_list)
# format entries column as int
meta_df['entries'] = meta_df['entries'].astype("Int64")
# save to CSV
meta_df.to_csv("../data/hms_2005_2021_metadata.csv", index=False)
