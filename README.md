# Readme

This is a set of scripts and tables for downloading the ERA5 data and preprocessing it to drive WRF simulations.

Following are descriptions of each subdirectory's content:

## `ERA5`

These python scripts download ERA5 data using the cdsapi python package.

For these scripts to work, you need to install the package via pip and have the `.cdsapirc` file ready in the home directory.

For `ungrib.exe` of WPS to work (with the `Vtable` file downloaded from `dreambooker.site`), you need to convert the `ml` data (model level data) to grib1 first using `grib_set -s deletePV=1,edition=1 era5.20210701-20210901.ml.grb era5.20210701-20210901.ml.grib1`.

The `sfc` data is already in GRIB1.

## `ungrib`

- First use `link_grib.csh` to link the downloaded grib1 files for `ml` and `sfc` ERA5 data here.

- Make sure the Vtable is linked to the correct one (`Vtable.ECMWF_sigma`).

- Run `ungrib.exe` with the right `namelist.wps` for meteorological fields.

- Run `calc_ecmwf_p.exe` (`ecmwf_coeffs` is needed) to generate the pressure levels for ERA5.

## `metgrid`

- Run `metgrid.exe` with the correct `METGRID.TBL.ARW` (just have both `METGRID.TBL` and `METGRID.TBL.ARW` here), `namelist.wps` (should be the same one as that in `ungrib`) and `geo_em.d01.nc`.

- Bill said when `geo_em.d01.nc` is missing, WPS may complain that `METGRID.TBL` is missing instead unless you use higher debug levels.

