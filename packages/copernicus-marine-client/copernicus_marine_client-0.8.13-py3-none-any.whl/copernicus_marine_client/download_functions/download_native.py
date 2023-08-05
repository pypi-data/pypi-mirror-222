import logging
import pathlib
from sys import exit
from typing import Callable, List, Tuple

import click

from copernicus_marine_client.catalogue_parser.request_structure import (
    GetRequest,
)
from copernicus_marine_client.utils import FORCE_DOWNLOAD_CLI_PROMPT_MESSAGE


def download_native(
    username: str,
    password: str,
    get_request: GetRequest,
    download_header: Callable,
    create_filenames_out: Callable,
) -> Tuple[List[str], List[pathlib.Path], str]:
    message, endpoint_url, filenames_in, total_size = download_header(
        str(get_request.dataset_url),
        get_request.regex,
        username,
        password,
    )
    filenames_out = create_filenames_out(
        filenames_in=filenames_in,
        output_directory=get_request.output_directory,
        no_directories=get_request.no_directories,
        overwrite=get_request.overwrite,
    )
    logging.info(message)
    if not total_size:
        logging.info("No data to download")
        exit(1)
    if get_request.show_outputnames:
        logging.info("Output filenames:")
        for filename_out in filenames_out:
            logging.info(filename_out)
    if not get_request.force_download:
        click.confirm(
            FORCE_DOWNLOAD_CLI_PROMPT_MESSAGE, default=True, abort=True
        )
    return (filenames_in, filenames_out, endpoint_url)
