import logging
import pathlib
from typing import Optional

import click
import xarray as xr
import zarr

from copernicus_marine_client.catalogue_parser.request_structure import (
    SubsetRequest,
)
from copernicus_marine_client.download_functions.subset_parameters import (
    DepthParameters,
    GeographicalParameters,
    LatitudeParameters,
    LongitudeParameters,
    TemporalParameters,
)
from copernicus_marine_client.download_functions.subset_xarray import subset
from copernicus_marine_client.utils import (
    FORCE_DOWNLOAD_CLI_PROMPT_MESSAGE,
    get_unique_filename,
)


def get_optimized_chunking(subset_request: SubsetRequest) -> str:
    """Function to calculate the optimized type of chunking,
    based on a subset_request.
    Returns a str: "map" if time-chunking is optimized,
    "timeserie" if geo-chunking is optimized
    """
    logging.info(
        "THIS CHUNKING OPTIMIZATION FUNCTION IS "
        + "A PLACEHOLDER, DO NOT RELY ON IT!!"
    )
    chunking_selected = "map"
    if (
        isinstance(subset_request.minimal_latitude, float)
        and isinstance(subset_request.maximal_latitude, float)
        and isinstance(subset_request.minimal_longitude, float)
        and isinstance(subset_request.maximal_longitude, float)
    ):
        surface = abs(
            subset_request.maximal_longitude - subset_request.minimal_longitude
        ) * abs(
            subset_request.maximal_latitude - subset_request.minimal_latitude
        )

        if surface < 20:
            chunking_selected = "timeserie"
    return chunking_selected


def download_dataset(
    username: str,
    password: str,
    geographical_parameters: GeographicalParameters,
    temporal_parameters: TemporalParameters,
    depth_parameters: DepthParameters,
    dataset_url: str,
    output_directory: pathlib.Path,
    output_filename: pathlib.Path,
    variables: Optional[list[str]],
    force_download: bool = False,
    overwrite: bool = False,
):
    dataset = xr.open_zarr(dataset_url)
    dataset = subset(
        dataset=dataset,
        variables=variables,
        geographical_parameters=geographical_parameters,
        temporal_parameters=temporal_parameters,
        depth_parameters=depth_parameters,
    )
    dataset = dataset.chunk(chunks="auto")

    output_path = pathlib.Path(output_directory, output_filename)

    if not force_download:
        logger = logging.getLogger("blank_logger")
        logger.warn(dataset)
        click.confirm(
            FORCE_DOWNLOAD_CLI_PROMPT_MESSAGE, default=True, abort=True
        )

    output_path = get_unique_filename(
        filepath=output_path, overwrite_option=overwrite
    )

    write_mode = "w"
    if output_filename.suffix == ".nc":
        if not output_directory.is_dir():
            pathlib.Path.mkdir(output_directory, parents=True)
        dataset.to_netcdf(output_path, mode=write_mode)
    else:
        store = zarr.DirectoryStore(output_path)
        dataset.to_zarr(store=store, mode=write_mode)

    logging.info(f"Successfully downloaded to {output_path}")


def download_zarr(
    username: str,
    password: str,
    subset_request: SubsetRequest,
):
    geographical_parameters = GeographicalParameters(
        latitude_parameters=LatitudeParameters(
            minimal_latitude=subset_request.minimal_latitude,
            maximal_latitude=subset_request.maximal_latitude,
        ),
        longitude_parameters=LongitudeParameters(
            minimal_longitude=subset_request.minimal_longitude,
            maximal_longitude=subset_request.maximal_longitude,
        ),
    )
    temporal_parameters = TemporalParameters(
        start_datetime=subset_request.start_datetime,
        end_datetime=subset_request.end_datetime,
    )
    depth_parameters = DepthParameters(
        minimal_depth=subset_request.minimal_depth,
        maximal_depth=subset_request.maximal_depth,
        vertical_dimension_as_originally_produced=subset_request.vertical_dimension_as_originally_produced,  # noqa
    )
    dataset_url = str(subset_request.dataset_url)
    output_directory = (
        subset_request.output_directory
        if subset_request.output_directory
        else pathlib.Path(".")
    )
    output_filename = (
        subset_request.output_filename
        if subset_request.output_filename
        else pathlib.Path("data.zarr")
    )
    variables = subset_request.variables
    force_download = subset_request.force_download

    download_dataset(
        username=username,
        password=password,
        geographical_parameters=geographical_parameters,
        temporal_parameters=temporal_parameters,
        depth_parameters=depth_parameters,
        dataset_url=dataset_url,
        output_directory=output_directory,
        output_filename=output_filename,
        variables=variables,
        force_download=force_download,
        overwrite=subset_request.overwrite,
    )
    return pathlib.Path(output_directory, output_filename)
