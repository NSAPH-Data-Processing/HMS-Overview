# produce a JSON of missing or zero-value dates from hms_2005_2021_metadata
import json
import pandas as pd

# read in csv
meta_df = pd.read_csv("../data/hms_2005_2021_metadata.csv")
# make list of dates with missing shapefiles
missing = meta_df.loc[meta_df["missing"] == True]['date'].tolist()
# make list of dates with empty shapefiles
no_entries = meta_df.loc[meta_df["entries"] == 0]['date'].tolist()

dates_dict = {  "first_date": meta_df.iloc[0]['date'],
                "last_date": meta_df.iloc[-1]['date'], 
                "missing": missing, 
                "no_entries": no_entries}

with open('../data/hms_2005_2021_absent_dates.json', 'w') as fp:
    json.dump(dates_dict, fp, indent=2)
