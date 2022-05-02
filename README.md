# HMS Smoke Product Data Overview
This repository contains code, documentation and general information concerning the
HMS smoke product shapefiles which can be downloaded at
https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Smoke_Polygons/Shapefile/ .

The dataset reviewed contains data from 2005.08.05 (the first day for which shapes are
available) to 2021.12.31 (the last day of 2021). Data up to the present day is available
through the website.

## Code

`1_collect_HMS_daily_shapes.py`
*   Produces shapefile and CSV of metadata containing the original column names in each file,
    number of entries, and whether a shapefile was present for that date.

`2_produce_date_json.py`
*   Produces `hms_2005_2021_absent_dates.json`, which contains easy-to-reference lists of
    dates in the dataset for which shapefiles are empty or missing.

## Data

The columns in hms_smoke_shapes_2005_2021 are as follows:
-   `ID` - a daily unique ID. It is assigned each day starting from "1". Not used after 2017.
-   `Start` - time the plume is first observed.
-   `End` - time the plume is last observed.
-   `Density` - density of the plume shape. Value will be 5, 16, or 27.
-   `geometry` - shape data for the plume.
-   `date` - date of plume observation.
-   `year` - year of plume observation.
-   `tessellate`, `extrude`, `visibility` `altitudeMo` - these columns are only collected
     for one day in the full span of HMS data 2005-2021. It is unclear what they mean or 
     what use these values might have. They are retained in this dataset purely for posterity.
-   `Satellite` - name or identifier of satellite which produced the source images.

## Missing values
(Work shown in Jupyter Notebook `hms_investigations_1.ipynb`)

#### Table: missing data by day

Values:
* `days` - total number of days that could be represented in the set.
* `no entries` - number of days which contained a shapefile with no entries.
  This is presumed to represent a day in which no smoke was present.
* `missing` - number of days for which no shapefile was found. Whether a missing
  day implies missing data or no smoke to report has not been confirmed.
* `NAN-Density` - the number of days for which no density values were recorded.
* `unrepresented` - the sum of `missing` and `NAN-Density`.
* `%` - `unrepresented` divided by `days` to produce percent of days per year that
  are unrepresented.

| year | days | no entries | missing | NAN-Density | unrepresented | %     |
|------|------|------------|---------|-------------|---------------|-------|
| 2005 | 149  | 1          | 2       | 146         | 148           | 99.3  |
| 2006 | 365  | 4          | 5       | 356         | 361           | 98.9  |
| 2007 | 365  | 5          | 2       | 354         | 356           | 97.5  |
| 2008 | 366  | 4          | 3       | 119         | 122           | 33.3  |
| 2009 | 365  | 3          | 2       | 358         | 360           | 98    |
| 2010 | 365  | 3          | 0       | 146         | 146           | 40    |
| 2011 | 365  | 2          | 0       | 0           | 0             | 0     |
| 2012 | 366  | 3          | 1       | 0           | 1             | 0.2   |
| 2013 | 365  | 6          | 0       | 0           | 0             | 0     |
| 2014 | 365  | 8          | 0       | 0           | 0             | 0     |
| 2015 | 365  | 8          | 2       | 1           | 3             | 0.8   |
| 2016 | 366  | 5          | 2       | 0           | 2             | 0.5   |
| 2017 | 365  | 1          | 5       | 0           | 5             | 1.3   |
| 2018 | 365  | 1          | 1       | 1           | 2             | 0.5   |
| 2019 | 365  | 0          | 2       | 0           | 2             | 0.5   |
| 2020 | 366  | 0          | 1       | 0           | 1             | 0.3   |
| 2021 | 365  | 0          | 0       | 0           | 0             | 0     |


#### Table: missing data by entry

| year | Entries | NAN-Density | NAN-Start/End | NAN-Satellite |
|------|---------|-------------|---------------|---------------|
| 2005 | 6296    | 6296        | 0             | 6296          |
| 2006 | 15453   | 15453       | 0             | 15453         |
| 2007 | 19881   | 19623       | 0             | 19881         |
| 2008 | 23285   | 5076        | 0             | 23285         |
| 2009 | 23517   | 23369       | 0             | 23369         |
| 2010 | 27241   | 7446        | 0             | 26881         |
| 2011 | 33721   | 0           | 0             | 33721         |
| 2012 | 27972   | 0           | 0             | 27901         |
| 2013 | 23162   | 0           | 0             | 23162         |
| 2014 | 18565   | 0           | 0             | 18565         |
| 2015 | 16357   | 12          | 12            | 16182         |
| 2016 | 21280   | 0           | 0             | 19008         |
| 2017 | 24739   | 0           | 0             | 0             |
| 2018 | 40948   | 306         | 306           | 306           |
| 2019 | 42945   | 0           | 0             | 0             |
| 2020 | 45329   | 0           | 0             | 0             |
| 2021 | 27573   | 0           | 0             | 0             |


## Excerpts and Links

From [NOAA](https://www.ospo.noaa.gov/Products/land/hms.html#about):

> HMS's smoke analysis is based on visual classification of plumes using GOES-16 and GOES-17
ABI true-color imagery available during the sunlit part of the orbit. Since the analysis
generally requires a sequential set of satellite images to help distinguish smoke from
clouds and other atmospheric aerosols, the first smoke analysis for the current day is
usually produced around the local noon time – until then, only fire detection points may
be available.
>
> Additional smoke analysis will occur throughout the day until sunset or as observation
conditions permit.
>
> Smoke attributes carry the start and end times (in Universal Time Coordinated - UTC) of
the satellite image sequence used to outline the smoke polygon, the corresponding
satellite from which the image was derived, and the plume density. The density information
is qualitatively described using thin, medium, and thick labels that are assigned based
on the apparent thickness (opacity) of the smoke in the satellite imagery. A numerical
smoke attribute is also provided, in which a density of 5 corresponds to a thin plume, 16
is medium, and 27 is thick. [...] Because of this approximation and the qualitative nature
of the visual analysis, those shouldn't be used as absolute cutoff values.

From Summer 2012 ARSET-AQ Advanced Webinar, [The NOAA/NESDIS Fire and Smoke Analysis Product](https://appliedsciences.nasa.gov/sites%/default/files/2021-04/NOAA_Smoke_Product.doc):

> Plume outline/edges are most easily determined when there is a sharp contrast between
the smoke/no smoke areas. This is usually the case for relatively fresh smoke from
active fires but is also dependent on other factors such as vertical wind profiles,
atmospheric stability, presence of clouds, etc.  The 'older' the smoke gets (smoke can
stay aloft for days to weeks) the more likely it will become more diffuse and lose
its sharp edge. It is also more likely to mix with other aerosol constituents
(primarily haze pollution) in stagnant weather patterns. This frequently occurs in the
summer when there are large smoke producing fires in the West. The smoke will often
drift into the central and eastern US and mix with pollution in these areas which can
make it very difficult to define plumes from particular sources. To help track smoke in
these cases (and discriminate between blowing dust and haze pollution) as well as track
long range transport from Asia or elsewhere various additional resources can be used,
including the [NWS smoke forecast](http://airquality.weather.gov/), the
[UMBC smog blog](http://alg.umbc.edu/usaq/), the
[Naval Research Lab aerosol forecast](http://www.nrlmry.navy.mil/aerosol_web/loop_html/globaer_noramer_loop.html) and
[NASA's GEOS-5 model](http://portal.nccs.nasa.gov/cgi-fp/fp_2d_chem.cgi?region=pac&dtg=2012041900&prod=coclbbae&model=fp&tau=000&&region_old=pac&dtg_old=2012041900&prod_old=fineaot&model_old=fp&tau_old=000&&loop=0).

More information:

*  Rolph et al. 2009,
[Description and Verification of the NOAA Smoke Forecasting System: The 2007 Fire Season](https://journals.ametsoc.org/view/journals/wefo/24/2/2008waf2222165_1.xml)


## Prior Research Using HMS Smoke Data

### Aguilera et al. 2021
* Paper: "[Wildfire smoke impacts respiratory health more than fine particles from other sources: observational evidence from Southern California](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7935892/)"

### Zhou et al. 2021
* Paper: "[Excess of COVID-19 cases and deaths due to fine particulate matter exposure during the 2020 wildfires in the United States](https://www.science.org/doi/10.1126/sciadv.abi8789?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%20%200pubmed)"
* Repository: [xiaodan-zhou/covid_wildfire](https://github.com/xiaodan-zhou/covid_wildfire)

Notes on decision of smoke day classification definition from paper's Supplementary Materials:
- Validates HMS smoke product by comparing HMS smoke plumes against the NOAA Integrated Surface Data (ISD; https://www.ncdc.noaa.gov/isd/data-access) collected at four airports in California, Oregon, and Washington.
- Calculated accuracy of HMS smoke product when used as a binary proxy for the presence of ground-level smoke on a daily basis for July-November of 2007-2020.
- Validation shows that:
  * using all categories of HMS smoke to define smoke days leads to the highest true positive rate but introduces more false positives, or days categorized as non-smoke by airport data but smoke by HMS.
  * using heavy HMS smoke to define smoke days maximizes overall accuracy and minimizes false-positive rates.

HMS datasets in repository are:
* [HMS_county_2020.csv](https://github.com/xiaodan-zhou/covid_wildfire/blob/master/data/HMS_county_2020.csv)
* [HMS_zipCodes_2020.csv](https://github.com/xiaodan-zhou/covid_wildfire/blob/master/data/HMS_zipCodes_2020.csv).

Both CSVs consist of daily readings where the only value which appears is 5,16, or 27.
The numbers represent the maximum smoke density value within the county/zip code for each day.


In the repo code, HMS_county_2020.csv is used in two scripts:
* [Utilities.R](https://github.com/xiaodan-zhou/covid_wildfire/blob/master/src/Utilities.R)
* [combine.R](https://github.com/xiaodan-zhou/covid_wildfire/blob/master/src/combine.R)
