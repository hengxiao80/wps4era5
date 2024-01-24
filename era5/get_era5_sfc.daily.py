# Template script for downloading ERA5 surface data for WRF/WPS.
# From https://dreambooker.site/2018/04/20/Initializing-the-WRF-model-with-ERA5 on 6-Mar-2020.

import cdsapi
import pandas as pd

c = cdsapi.Client()

dates = pd.date_range("03-01-2021", "04-01-2021", inclusive="both")
for d in dates.strftime("%Y%m%d"):
    print(d)
    c.retrieve(
        "reanalysis-era5-complete",
        {
            "class": "ea",
            "date": d,
            "area": "60/-160/20/-100",
            "expver": "1",
            "levtype": "sfc",
            "param": "msl/sp/skt/2t/10u/10v/2d/z/lsm/sst/ci/sd/stl1/stl2/stl3/stl4/swvl1/swvl2/swvl3/swvl4/tclw/tciw/tcwv/blh/tcc/lcc/mcc/hcc/iews/inss/ishf/ie/fal/fsr/flsr",
            "stream": "oper",
            "time": "00/to/23/by/1",
            "type": "an",
            "grid": "0.25/0.25",
        },
        f"era5.{d}.sfc.grb",
    )
