# Copernicus Marine Service client

A library to facilitate the access of Copernicus Marine Service products and datasets.

## Introduction

This package allows to recover products and datasets information from Command Line Interface,
as well as download subsets and originally produced files.

## Command Line Interface (CLI)

### Command *describe*

Retrieve information about all products as JSON:

```txt
> copernicus-marine describe
{
  "products": [
    {
      "title": "Antarctic Sea Ice Extent from Reanalysis",
      "product_id": "ANTARCTIC_OMI_SI_extent",
      "thumbnail_url": "https://catalogue.marine.copernicus.eu/documents/IMG/ANTARCTIC_OMI_SI_extent.png",
      "production_center": "Mercator Oc\u00e9an International",
      "creation_datetime": "2018-02-12",
      "modified_datetime": "2018-02-12",
    }
    ...
  ]
}
```

Retrieve all information about datasets as JSON:

```txt
> copernicus-marine describe --include-datasets
{
  "products": [
    {
      "title": "Antarctic Sea Ice Extent from Reanalysis",
      "product_id": "ANTARCTIC_OMI_SI_extent",
      "thumbnail_url": "https://catalogue.marine.copernicus.eu/documents/IMG/ANTARCTIC_OMI_SI_extent.png",
      "production_center": "Mercator Oc\u00e9an International",
      "creation_datetime": "2018-02-12",
      "modified_datetime": "2018-02-12",
      "datasets": [
        {
          "dataset_id": "antarctic_omi_si_extent",
          "dataset_name": "antarctic_omi_si_extent",
          "services": [
            {
              "protocol": "ftp",
              "uri": "ftp://my.cmems-du.eu/Core/ANTARCTIC_OMI_SI_extent/antarctic_omi_si_extent"
            }
          ],
          "variables": []
        }
      ]
    },
    ...
  ]
}
```

### Command *login*

Create the configuration files for access to the copernicus marine service:
'.dodsrc', '.netrc', '.motuclient-python.ini'.
The directory to store these configuration files can be modified by the user using the "config-file-directory" option
but beware as it should also be passed to the *subset* and *get* command afterwards.
By default, if the configuration files already exist, the user is asked for confirmation to overwrite them.

Example:
```
> copernicus marine login
< Username :
< Password :
> INFO     - root - Configuration files stored in ${HOME}\.copernicus_marine_client
```

### Command *subset*

Download a dataset subset, based on dataset id, variable names and attributes slices:

```txt
> copernicus-marine subset -i METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2 -v analysed_sst -v sea_ice_fraction -t 2021-01-01 - T 2021-01-03 -x 0.0 -X 0.1 -y 0.0 -Y 0.1

< Username:
< Password:
< Trying to download as one file...
```

File downloaded to ./{dataset_id}.{nc/zarr} if not specified otherwise (through -o/--output-directory and -f/--output-filename options). If the output-filename argument ends with '.nc' suffix, the file will be downloaded as a netCDF file.

Options `--minimal-longitude FLOAT` and `--maximal-longitude FLOAT` work as follow:
* `--minimal-longitude` must be lower or equal to `--maximal-longitude`
* If `maximal-longitude - minimal-longitude >= 360`, return the full dataset.
* Else:
    - If the requested range **does not cross** the antemeridian, the result dataset will be between -180° and 180°.
    - If it **does cross** the antemeridian, the result dataset will be between 0° and 360°.

Note that you can request any longitudes you want. A modulus is applied to bring the result between -180° and 360°. For example, if you request [530°, 560°], the result dataset will be in [170°, 190°].


The `--vertical-dimension-as-originally-produced BOOLEAN` option is used to obtain a dataset whose vertical dimension (the z-axis) is as in the originally produced dataset. This dimension will be named `depth` with descending positive values. Its default value is `true`.

### Command *get*

Download an originally produced file (or files), based on dataset id or path to files:

Example:

```txt
> copernicus-marine get -u ftp://my.cmems-du.eu/Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/

< Username:
< Password:
< You requested the download of the following files:
Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202207.nc - 3.27 MB
Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202208.nc - 3.29 MB
Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202209.nc - 3.28 MB
Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202210.nc - 3.26 MB
Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202211.nc - 3.26 MB
Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202212.nc - 3.26 MB

Total size of the download: 19.62 MB


Do you want to proceed with download? [Y/n]:
```

File(s) downloaded to ./{path}/{filename} if not specified otherwise:

- "--output-path" specifies a directory to dump the files in
- "--no-directories" to not recreate the folder structure

If not specified otherwise, after the header display with a summary of the request,
the user is asked for confirmation:

- "--no-confirmation" to turn down the confirmation prompt
- "--show-outputnames" to display the full paths of the outputs files

Option `--filter TEXT` allows to specify a Unix shell-style wildcard pattern (see [fnmatch — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html)) and select specific files. It work with both `--dataset-id` and `--dataset-url` options.

Option `--regex TEXT` allows to specify a regular expression and select specific files. It work with both `--dataset-id` and `--dataset-url` options.

Example:
```
> copernicus-marine get -u ftp://my.cmems-du.eu/Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m --regex ".*2022(08|09|10).nc"
Password:
You requested the download of the following files:
Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202208.nc - 3.29 MB
Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202209.nc - 3.28 MB
Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202210.nc - 3.26 MB

Total size of the download: 9.82 MB


Do you want to proceed with download? [Y/n]:
```

### The overwrite option

Both `get` and `subset` commands provide an `--overwrite-ouput-data` option.
When not provided (default behavior), once the download has been accepted (or if the `--force-download` option was provided), if the file already exists on destination, then a new one with a unique index will be created.
On the other hand, if the `--overwrite-ouput-data` option is provided and the file already exists, then it'll be overwritten.

### The `--help` argument

In any case, please remember that you can call the `--help` argument on any CLI option. This may save you some time or find what you need.

## Installation

Using pip, for example:

```shell
pip install copernicus-marine-client
```

## Technical details

This module is organized around two capabilities:

- a catalogue, parsed from web requests, that contains informations on the available datasets
- a downloader, to simplify the download of dataset files or subsets

The catalogue can be displayed by the user and is used by the downloader to link the user
requests with files or subset of files to retrieve.
The downloader will help the user download the needed datasets.

A rigid format, specified in "request_structure.py" is used to ensure conformity of the information passed between the CLI command and the python functions.

For subset command, the format is:

```python
@dataclass
class SubsetRequest:
    dataset_url: Optional[str] = None
    dataset_id: Optional[str] = None
    variables: Optional[List[str]] = None
    minimal_longitude: Optional[float] = None
    maximal_longitude: Optional[float] = None
    minimal_latitude: Optional[float] = None
    maximal_latitude: Optional[float] = None
    minimal_depth: Optional[float] = None
    maximal_depth: Optional[float] = None
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None
    output_directory: Optional[str] = None
    output_filename: Optional[str] = None
    force_download: Optional[bool] = None
    force_protocol: Optional[str] = None
```
