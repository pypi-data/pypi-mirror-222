from enum import Enum
from typing import List


class ServiceDoesNotExist(Exception):
    ...


class CommandName(Enum):
    SUBSET = "subset"
    GET = "get"


class ServiceName(Enum):
    MOTU = "motu"
    OPENDAP = "opendap"
    GEOSERIES = "geoseries"
    TIMESERIES = "timeseries"
    FILES = "files"
    FTP = "ftp"


SERVICES_BY_COMMAND_NAME = {
    CommandName.SUBSET: {
        ServiceName.MOTU: ["motu"],
        ServiceName.OPENDAP: ["opendap"],
        ServiceName.GEOSERIES: ["arco-geo-series", "geoseries"],
        ServiceName.TIMESERIES: ["arco-time-series", "timeseries"],
    },
    CommandName.GET: {
        ServiceName.FILES: ["original-files", "files"],
        ServiceName.FTP: ["ftp"],
    },
}

SERVICES_NAMES_EQUIVALENTS = {
    "motu": "motu",
    "opendap": "opendap",
    "arco-geo-series": "timeChunked",
    "geoseries": "timeChunked",
    "arco-time-series": "geoChunked",
    "timeseries": "geoChunked",
    "files": "native",
    "original-files": "native",
    "ftp": "ftp",
}


def get_service_aliases(service_name: ServiceName) -> List[str]:
    for command_name in CommandName:
        if service_name in SERVICES_BY_COMMAND_NAME[command_name]:
            return SERVICES_BY_COMMAND_NAME[command_name][service_name]
    return []


def _get_services_aliases_by_command(command_name: CommandName) -> List[str]:
    return [
        item
        for sublist in SERVICES_BY_COMMAND_NAME[command_name]
        for item in SERVICES_BY_COMMAND_NAME[command_name][sublist]
    ]


def get_subset_services_aliases() -> List[str]:
    return _get_services_aliases_by_command(CommandName.SUBSET)


def get_get_services_aliases() -> List[str]:
    return _get_services_aliases_by_command(CommandName.GET)


def get_services_names_by_command(
    command_name: CommandName,
) -> List[ServiceName]:
    return list(SERVICES_BY_COMMAND_NAME[command_name].keys())


def get_service_name_from_alias_and_command(
    alias: str, command_name: CommandName
) -> ServiceName:
    for service in SERVICES_BY_COMMAND_NAME[command_name].keys():
        if alias in SERVICES_BY_COMMAND_NAME[command_name][service]:
            return service
    raise ServiceDoesNotExist


def check_if_name_in_services_names_by_command(
    name: str, command_name: CommandName
) -> bool:
    for service_name in SERVICES_BY_COMMAND_NAME[command_name].keys():
        if service_name.value == name:
            return True
    return False


def get_services_names_intersection(
    dataset_services: List[str], command_name: CommandName
) -> List[str]:
    services_names_intersection = []
    for dataset_service in dataset_services:
        if check_if_name_in_services_names_by_command(
            dataset_service, command_name
        ):
            services_names_intersection.append(dataset_service)
    return services_names_intersection


def translate_service_name_to_describe_service_name(name: str) -> str:
    if name in SERVICES_NAMES_EQUIVALENTS:
        return SERVICES_NAMES_EQUIVALENTS[name]
    return name


def translate_describe_service_name_to_service_name(name: str) -> str:
    for key, value in SERVICES_NAMES_EQUIVALENTS.items():
        if value == name:
            return key
    return name
