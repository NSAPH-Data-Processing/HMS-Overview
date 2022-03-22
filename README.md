# HMS Smoke Product Data Overview
This repository contains code, documentation and general information concerning the
HMS smoke product shapefiles which can be downloaded
[here](https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Smoke_Polygons/Shapefile/).

## Missing values
(Work shown in Jupyter Notebook hms_investigations.ipynb)

| year | NAN-Density | NAN-Start/End | NAN-Satellite | Total |
|------|-------------|---------------|---------------|-------|
| 2005 | 6296        | 0             | 6296          | 6296  |
| 2006 | 15453       | 0             | 15453         | 15453 |
| 2007 | 19623       | 0             | 19881         | 19881 |
| 2008 | 5076        | 0             | 23285         | 23285 |
| 2009 | 23369       | 0             | 23369         | 23517 |
| 2010 | 7446        | 0             | 26881         | 27241 |
| 2011 | 0           | 0             | 33721         | 33721 |
| 2012 | 0           | 0             | 27901         | 27972 |
| 2013 | 0           | 0             | 23162         | 23162 |
| 2014 | 0           | 0             | 18565         | 18565 |
| 2015 | 12          | 12            | 16182         | 16357 |
| 2016 | 0           | 0             | 19008         | 21280 |
| 2017 | 0           | 0             | 0             | 24739 |
| 2018 | 306         | 306           | 306           | 40948 |
| 2019 | 0           | 0             | 0             | 42945 |
| 2020 | 0           | 12            | 0             | 45329 |
| 2021 | 0           | 0             | 0             | 27573 |


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
- Validation shows that :
  * using all categories of HMS smoke to define smoke days leads to the highest true positive rate but introduces more false positives, or days categorized as non-smoke by airport data but smoke by HMS.
  * using heavy HMS smoke to define smoke days maximizes overall accuracy and minimizes false-positive rates.

HMS datasets in repository are:
* [HMS_county_2020.csv](https://github.com/xiaodan-zhou/covid_wildfire/blob/master/data/HMS_county_2020.csv)
* [HMS_zipCodes_2020.csv](https://github.com/xiaodan-zhou/covid_wildfire/blob/master/data/HMS_zipCodes_2020.csv).

Both CSVs consist of daily readings where the only value which appears is 5,16, or 27.

In the repo code, HMS_county_2020.csv is used in two scripts:
* [Utilities.R](https://github.com/xiaodan-zhou/covid_wildfire/blob/master/src/Utilities.R)
* [combine.R](https://github.com/xiaodan-zhou/covid_wildfire/blob/master/src/combine.R)
