# Template script for downloading ERA5 model-level data for WRF/WPS.
# From https://dreambooker.site/2018/04/20/Initializing-the-WRF-model-with-ERA5 on 6-Mar-2020.

import cdsapi

c = cdsapi.Client()

c.retrieve(
    "reanalysis-era5-complete",
    {
        "class": "ea",
        "date": "20210701/to/20210901",
        "area": "60/-160/20/-100",
        "expver": "1",
        "levelist": "1/to/137",
        "levtype": "ml",
        "param": "129/130/131/132/133/152/75/76/135/246/247/248",
        "stream": "oper",
        "time": "00/to/23/by/1",
        "type": "an",
        "grid": "0.25/0.25",
    },
    "era5.20210701-20210901.ml.grb",
)
