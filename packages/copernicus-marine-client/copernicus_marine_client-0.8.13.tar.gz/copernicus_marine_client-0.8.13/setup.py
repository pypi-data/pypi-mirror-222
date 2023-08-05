# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['copernicus_marine_client',
 'copernicus_marine_client.catalogue_parser',
 'copernicus_marine_client.command_line_interface',
 'copernicus_marine_client.download_functions']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3',
 'boto3>=1.28.2,<2.0.0',
 'cachier>=2.0.2',
 'click>=8.0.4',
 'dask>=2022.1.1',
 'motuclient==1.8.4',
 'netCDF4>=1.6.3',
 'numpy>=1.0',
 'owslib>=0.27.2',
 'pydap>=3.2.2',
 'requests>=2.27.1',
 'setuptools>=62.0.0',
 'tqdm>=4.65.0',
 'xarray>=2023.3.0',
 'zarr>=2.13.3']

entry_points = \
{'console_scripts': ['copernicus-marine = '
                     'copernicus_marine_client.command_line_interface.copernicus_marine:command_line_interface']}

setup_kwargs = {
    'name': 'copernicus-marine-client',
    'version': '0.8.13',
    'description': '',
    'long_description': '# Copernicus Marine Service client\n\nA library to facilitate the access of Copernicus Marine Service products and datasets.\n\n## Introduction\n\nThis package allows to recover products and datasets information from Command Line Interface,\nas well as download subsets and originally produced files.\n\n## Command Line Interface (CLI)\n\n### Command *describe*\n\nRetrieve information about all products as JSON:\n\n```txt\n> copernicus-marine describe\n{\n  "products": [\n    {\n      "title": "Antarctic Sea Ice Extent from Reanalysis",\n      "product_id": "ANTARCTIC_OMI_SI_extent",\n      "thumbnail_url": "https://catalogue.marine.copernicus.eu/documents/IMG/ANTARCTIC_OMI_SI_extent.png",\n      "production_center": "Mercator Oc\\u00e9an International",\n      "creation_datetime": "2018-02-12",\n      "modified_datetime": "2018-02-12",\n    }\n    ...\n  ]\n}\n```\n\nRetrieve all information about datasets as JSON:\n\n```txt\n> copernicus-marine describe --include-datasets\n{\n  "products": [\n    {\n      "title": "Antarctic Sea Ice Extent from Reanalysis",\n      "product_id": "ANTARCTIC_OMI_SI_extent",\n      "thumbnail_url": "https://catalogue.marine.copernicus.eu/documents/IMG/ANTARCTIC_OMI_SI_extent.png",\n      "production_center": "Mercator Oc\\u00e9an International",\n      "creation_datetime": "2018-02-12",\n      "modified_datetime": "2018-02-12",\n      "datasets": [\n        {\n          "dataset_id": "antarctic_omi_si_extent",\n          "dataset_name": "antarctic_omi_si_extent",\n          "services": [\n            {\n              "protocol": "ftp",\n              "uri": "ftp://my.cmems-du.eu/Core/ANTARCTIC_OMI_SI_extent/antarctic_omi_si_extent"\n            }\n          ],\n          "variables": []\n        }\n      ]\n    },\n    ...\n  ]\n}\n```\n\n### Command *login*\n\nCreate the configuration files for access to the copernicus marine service:\n\'.dodsrc\', \'.netrc\', \'.motuclient-python.ini\'.\nThe directory to store these configuration files can be modified by the user using the "config-file-directory" option\nbut beware as it should also be passed to the *subset* and *get* command afterwards.\nBy default, if the configuration files already exist, the user is asked for confirmation to overwrite them.\n\nExample:\n```\n> copernicus marine login\n< Username :\n< Password :\n> INFO     - root - Configuration files stored in ${HOME}\\.copernicus_marine_client\n```\n\n### Command *subset*\n\nDownload a dataset subset, based on dataset id, variable names and attributes slices:\n\n```txt\n> copernicus-marine subset -i METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2 -v analysed_sst -v sea_ice_fraction -t 2021-01-01 - T 2021-01-03 -x 0.0 -X 0.1 -y 0.0 -Y 0.1\n\n< Username:\n< Password:\n< Trying to download as one file...\n```\n\nFile downloaded to ./{dataset_id}.{nc/zarr} if not specified otherwise (through -o/--output-directory and -f/--output-filename options). If the output-filename argument ends with \'.nc\' suffix, the file will be downloaded as a netCDF file.\n\nOptions `--minimal-longitude FLOAT` and `--maximal-longitude FLOAT` work as follow:\n* `--minimal-longitude` must be lower or equal to `--maximal-longitude`\n* If `maximal-longitude - minimal-longitude >= 360`, return the full dataset.\n* Else:\n    - If the requested range **does not cross** the antemeridian, the result dataset will be between -180° and 180°.\n    - If it **does cross** the antemeridian, the result dataset will be between 0° and 360°.\n\nNote that you can request any longitudes you want. A modulus is applied to bring the result between -180° and 360°. For example, if you request [530°, 560°], the result dataset will be in [170°, 190°].\n\n\nThe `--vertical-dimension-as-originally-produced BOOLEAN` option is used to obtain a dataset whose vertical dimension (the z-axis) is as in the originally produced dataset. This dimension will be named `depth` with descending positive values. Its default value is `true`.\n\n### Command *get*\n\nDownload an originally produced file (or files), based on dataset id or path to files:\n\nExample:\n\n```txt\n> copernicus-marine get -u ftp://my.cmems-du.eu/Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/\n\n< Username:\n< Password:\n< You requested the download of the following files:\nCore/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202207.nc - 3.27 MB\nCore/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202208.nc - 3.29 MB\nCore/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202209.nc - 3.28 MB\nCore/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202210.nc - 3.26 MB\nCore/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202211.nc - 3.26 MB\nCore/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202212.nc - 3.26 MB\n\nTotal size of the download: 19.62 MB\n\n\nDo you want to proceed with download? [Y/n]:\n```\n\nFile(s) downloaded to ./{path}/{filename} if not specified otherwise:\n\n- "--output-path" specifies a directory to dump the files in\n- "--no-directories" to not recreate the folder structure\n\nIf not specified otherwise, after the header display with a summary of the request,\nthe user is asked for confirmation:\n\n- "--no-confirmation" to turn down the confirmation prompt\n- "--show-outputnames" to display the full paths of the outputs files\n\nOption `--filter TEXT` allows to specify a Unix shell-style wildcard pattern (see [fnmatch — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html)) and select specific files. It work with both `--dataset-id` and `--dataset-url` options.\n\nOption `--regex TEXT` allows to specify a regular expression and select specific files. It work with both `--dataset-id` and `--dataset-url` options.\n\nExample:\n```\n> copernicus-marine get -u ftp://my.cmems-du.eu/Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m --regex ".*2022(08|09|10).nc"\nPassword:\nYou requested the download of the following files:\nCore/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202208.nc - 3.29 MB\nCore/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202209.nc - 3.28 MB\nCore/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m/2022/metoffice_foam1_amm7_NWS_DIATO_CPWC_mm202210.nc - 3.26 MB\n\nTotal size of the download: 9.82 MB\n\n\nDo you want to proceed with download? [Y/n]:\n```\n\n### The overwrite option\n\nBoth `get` and `subset` commands provide an `--overwrite-ouput-data` option.\nWhen not provided (default behavior), once the download has been accepted (or if the `--force-download` option was provided), if the file already exists on destination, then a new one with a unique index will be created.\nOn the other hand, if the `--overwrite-ouput-data` option is provided and the file already exists, then it\'ll be overwritten.\n\n### The `--help` argument\n\nIn any case, please remember that you can call the `--help` argument on any CLI option. This may save you some time or find what you need.\n\n## Installation\n\nUsing pip, for example:\n\n```shell\npip install copernicus-marine-client\n```\n\n## Technical details\n\nThis module is organized around two capabilities:\n\n- a catalogue, parsed from web requests, that contains informations on the available datasets\n- a downloader, to simplify the download of dataset files or subsets\n\nThe catalogue can be displayed by the user and is used by the downloader to link the user\nrequests with files or subset of files to retrieve.\nThe downloader will help the user download the needed datasets.\n\nA rigid format, specified in "request_structure.py" is used to ensure conformity of the information passed between the CLI command and the python functions.\n\nFor subset command, the format is:\n\n```python\n@dataclass\nclass SubsetRequest:\n    dataset_url: Optional[str] = None\n    dataset_id: Optional[str] = None\n    variables: Optional[List[str]] = None\n    minimal_longitude: Optional[float] = None\n    maximal_longitude: Optional[float] = None\n    minimal_latitude: Optional[float] = None\n    maximal_latitude: Optional[float] = None\n    minimal_depth: Optional[float] = None\n    maximal_depth: Optional[float] = None\n    start_datetime: Optional[datetime] = None\n    end_datetime: Optional[datetime] = None\n    output_directory: Optional[str] = None\n    output_filename: Optional[str] = None\n    force_download: Optional[bool] = None\n    force_protocol: Optional[str] = None\n```\n',
    'author': 'Copernicus Marine User Support',
    'author_email': 'servicedesk.cmems@mercator-ocean.eu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
