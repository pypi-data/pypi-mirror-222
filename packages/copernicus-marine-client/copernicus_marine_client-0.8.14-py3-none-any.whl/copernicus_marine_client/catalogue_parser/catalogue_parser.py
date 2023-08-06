import asyncio
import logging
import logging.config
from copy import deepcopy
from dataclasses import dataclass
from itertools import groupby
from json import loads
from multiprocessing import Pool
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    TypeVar,
    cast,
)

import aiohttp
import requests
from cachier import cachier

from copernicus_marine_client.services_utils import (
    CommandName,
    ServiceName,
    check_if_name_in_services_names_by_command,
    get_service_name_from_alias_and_command,
    get_services_names_intersection,
    translate_describe_service_name_to_service_name,
    translate_service_name_to_describe_service_name,
)
from copernicus_marine_client.utils import DEFAULT_CLIENT_BASE_DIRECTORY


@dataclass
class CopernicusMarineDatasetService:
    service_name: str
    uri: str


@dataclass
class CopernicusMarineDatasetCoordinates:
    coordinates_id: str
    units: str
    minimum_value: float
    maximum_value: float
    step: Optional[float]
    values: Optional[str]


@dataclass
class CopernicusMarineDatasetVariable:
    short_name: str
    standard_name: str
    units: str
    bbox: Tuple[float, float, float, float]
    coordinates: list[CopernicusMarineDatasetCoordinates]


@dataclass
class CopernicusMarineProductDataset:
    dataset_id: str
    dataset_name: str
    services: list[CopernicusMarineDatasetService]
    variables: list[CopernicusMarineDatasetVariable]

    def get_available_services(self) -> list[str]:
        return list(map(lambda service: service.service_name, self.services))


@dataclass
class CopernicusMarineProductProvider:
    name: str
    roles: list[str]
    url: str
    email: str


@dataclass
class CopernicusMarineProduct:
    title: str
    product_id: str
    thumbnail_url: str
    description: str
    production_center: str
    creation_datetime: str
    modified_datetime: Optional[str]
    keywords: dict[str, str]
    datasets: list[CopernicusMarineProductDataset]


@dataclass
class CopernicusMarineCatalogue:
    products: list[CopernicusMarineProduct]

    def filter(self, tokens: list[str]):
        return filter_catalogue_with_strings(self, tokens)


_S = TypeVar("_S")
_T = TypeVar("_T")


def map_parallel(
    function: Callable[[_S], _T], iterable: Iterable[_S]
) -> list[_T]:
    parallel_processes = 20
    with Pool(parallel_processes) as pool:
        return pool.map(function, iterable)


def map_reject_none(
    function: Callable[[_S], Optional[_T]], iterable: Iterable[_S]
) -> Iterable[_T]:
    return (element for element in map(function, iterable) if element)


def parse_catalogue(
    overwrite_metadata_cache: bool,
    no_metadata_cache: bool,
) -> CopernicusMarineCatalogue:
    return parse_dissemination_unit_catalogue(
        overwrite_metadata_cache=overwrite_metadata_cache,
        no_metadata_cache=no_metadata_cache,
    )


async def _async_fetch_raw_product(session, product_id: str):
    async with session.get(product_url(product_id)) as resp:
        text_response = await resp.text()
        return loads(text_response)


async def _async_fetch_raw_products(product_ids: List[str]):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for product_id in product_ids:
            tasks.append(
                asyncio.ensure_future(
                    _async_fetch_raw_product(session, product_id)
                )
            )

        return await asyncio.gather(*tasks)


@cachier(cache_dir=DEFAULT_CLIENT_BASE_DIRECTORY)
def _fetch_raw_products() -> list[dict[str, Any]]:
    response = requests.post(
        "https://data-be-prd.marine.copernicus.eu/api/datasets",
        json={"size": 1000, "includeOmis": True},
    )
    assert response.ok, response.text
    raw_catalogue: dict[str, Any] = loads(response.text)

    results = asyncio.run(
        _async_fetch_raw_products(raw_catalogue["datasets"].keys())
    )
    return results


def product_url(product_id: str) -> str:
    return (
        f"https://data-be-prd.marine.copernicus.eu/api/dataset/{product_id}"
        + "?variant=detailed-v2"
    )


def variable_title_to_standard_name(variable_title: str) -> str:
    return variable_title.lower().replace(" ", "_")


def variable_to_pick(layer: dict[str, Any]) -> bool:
    return (
        layer["variableId"] != "__DEFAULT__"
        and layer["subsetVariableIds"]
        and len(layer["subsetVariableIds"]) == 1
    )


def to_datasets(
    raw_services: dict[str, dict[str, str]],
    layers: dict[str, dict[str, Any]],
    stac_items: dict,
) -> list[CopernicusMarineProductDataset]:
    def to_service(
        service_uri: Tuple[str, str]
    ) -> CopernicusMarineDatasetService:
        return CopernicusMarineDatasetService(
            service_name=service_uri[0], uri=service_uri[1]
        )

    def to_variable(layer: dict[str, Any]) -> CopernicusMarineDatasetVariable:
        def to_coordinates(
            subset_attributes: Tuple[str, dict[str, Any]]
        ) -> CopernicusMarineDatasetCoordinates:
            coordinate_name = subset_attributes[0]
            values: Optional[str]
            if coordinate_name == "depth":
                values = layer.get("zValues")
            elif coordinate_name == "time":
                values = layer.get("tValues")
            else:
                values = None
            return CopernicusMarineDatasetCoordinates(
                coordinates_id=subset_attributes[0],
                units=subset_attributes[1]["units"],
                minimum_value=subset_attributes[1]["min"],
                maximum_value=subset_attributes[1]["max"],
                step=subset_attributes[1].get("step"),
                values=values,
            )

        return CopernicusMarineDatasetVariable(
            short_name=layer["variableId"],
            standard_name=variable_title_to_standard_name(
                layer["variableTitle"]
            ),
            units=layer["units"],
            bbox=layer["bbox"],
            coordinates=list(
                map(to_coordinates, layer["subsetAttrs"].items())
            ),
        )

    def to_service_stac(asset) -> Optional[CopernicusMarineDatasetService]:
        service = asset[0]
        service_uri = asset[1]["href"]
        if service != "omi":
            return CopernicusMarineDatasetService(
                service_name=service, uri=service_uri
            )
        else:
            return None

    @dataclass
    class DistinctDataset:
        dataset_id: str
        layer_elements: Iterable
        raw_services: Dict
        stac_items_values: Optional[Dict]

    def to_dataset(
        distinct_dataset: DistinctDataset,
    ) -> CopernicusMarineProductDataset:
        dataset_id = distinct_dataset.dataset_id
        layer_elements = list(distinct_dataset.layer_elements)
        services_portal = list(
            map(to_service, distinct_dataset.raw_services.items())
        )
        services_stac = (
            list(
                filter(
                    lambda x: x is not None,
                    map(
                        to_service_stac,
                        distinct_dataset.stac_items_values["assets"].items(),
                    ),
                )
            )
            if distinct_dataset.stac_items_values
            else []
        )

        services = services_portal + cast(
            List[CopernicusMarineDatasetService], services_stac
        )

        return CopernicusMarineProductDataset(
            dataset_id=dataset_id,
            dataset_name=layer_elements[0]["subdatasetTitle"],
            services=services,
            variables=list(
                map(to_variable, filter(variable_to_pick, layer_elements))
            ),
        )

    def construct_unique_dataset(group_layer) -> DistinctDataset:
        dataset_id_from_layer = group_layer[0]
        dataset_layer_elements = group_layer[1]
        dataset_raw_services = raw_services[dataset_id_from_layer]

        for stac_dataset_id, stac_items_values in stac_items.items():
            if stac_dataset_id.startswith(dataset_id_from_layer):
                if (
                    "--ext--"
                    in stac_dataset_id.split(dataset_id_from_layer)[-1]
                ):
                    continue
                else:
                    return DistinctDataset(
                        dataset_id=dataset_id_from_layer,
                        layer_elements=dataset_layer_elements,
                        raw_services=dataset_raw_services,
                        stac_items_values=stac_items_values,
                    )
        else:
            return DistinctDataset(
                dataset_id=dataset_id_from_layer,
                layer_elements=dataset_layer_elements,
                raw_services=dataset_raw_services,
                stac_items_values=None,
            )

    groups_layers = groupby(
        layers.values(), key=lambda layer: layer["subdatasetId"]
    )
    distinct_datasets = map(construct_unique_dataset, groups_layers)

    return sorted(
        map(to_dataset, distinct_datasets),
        key=lambda distinct_dataset: distinct_dataset.dataset_id,
    )


def _parse_product(raw_product: dict[str, Any]) -> CopernicusMarineProduct:
    return CopernicusMarineProduct(
        title=raw_product["title"],
        product_id=raw_product["id"],
        thumbnail_url=raw_product["thumbnailUrl"],
        description=raw_product["abstract"],
        production_center=raw_product["originatingCenter"],
        creation_datetime=raw_product["creationDate"],
        modified_datetime=raw_product.get("modifiedDate"),
        keywords=raw_product["keywords"],
        datasets=to_datasets(
            raw_product["services"],
            raw_product["layers"],
            raw_product["stacItems"],
        ),
    )


def parse_dissemination_unit_catalogue(
    overwrite_metadata_cache: bool,
    no_metadata_cache: bool,
) -> CopernicusMarineCatalogue:
    raw_products: list[dict[str, Any]] = _fetch_raw_products(
        overwrite_cache=overwrite_metadata_cache,
        ignore_cache=no_metadata_cache,
    )

    return CopernicusMarineCatalogue(
        products=sorted(
            map(_parse_product, raw_products),
            key=lambda product: product.product_id,
        ),
    )


# ---------------------------------------
# --- Utils function on any catalogue ---
# ---------------------------------------


class ServiceNotAvailable(Exception):
    ...


def service_not_available_error(
    dataset_id: str, services: list[ServiceName]
) -> ServiceNotAvailable:
    return ServiceNotAvailable(
        f"Available services for dataset {dataset_id}: "
        f"{[service.value for service in services]}"
    )


def get_dataset_service(
    catalogue: CopernicusMarineCatalogue,
    dataset_id: str,
    force_service: Optional[str],
    command: CommandName,
) -> CopernicusMarineDatasetService:
    dataset = get_dataset_from_id(catalogue=catalogue, dataset_id=dataset_id)
    if force_service:
        service_name = get_service_name_from_alias_and_command(
            force_service, command
        )
        translated_service = translate_service_name_to_describe_service_name(
            service_name.value
        )
        for service in dataset.services:
            if service.service_name == translated_service:
                service.service_name = force_service
                return service
    else:
        for service in dataset.services:
            translated_service = (
                translate_describe_service_name_to_service_name(
                    service.service_name
                )
            )
            if check_if_name_in_services_names_by_command(
                translated_service, command
            ):
                service.service_name = translated_service
                return service
    available_dataset_services = [
        service.service_name for service in dataset.services
    ]
    available_services = get_services_names_intersection(
        available_dataset_services, command
    )
    raise ServiceNotAvailable(
        f"Available services for dataset {dataset_id}: {available_services}"
    )


def get_dataset_from_id(
    catalogue: CopernicusMarineCatalogue, dataset_id: str
) -> CopernicusMarineProductDataset:
    for product in catalogue.products:
        for dataset in product.datasets:
            if dataset_id == dataset.dataset_id:
                return dataset
    error = KeyError(
        f"The requested dataset '{dataset_id}' was not found in the catalogue,"
        " you can use 'copernicus-marine describe --include-datasets "
        "-c <search_token>' to find the dataset id"
    )
    logging.error(error)
    raise error


def get_product_from_url(
    catalogue: CopernicusMarineCatalogue, dataset_url: str
) -> CopernicusMarineProduct:
    """
    Return the product object, with its dataset list filtered
    """
    filtered_catalogue = filter_catalogue_with_strings(
        catalogue, [dataset_url]
    )
    if filtered_catalogue is None:
        error = TypeError("filtered catalogue is empty")
        raise error
    return filtered_catalogue.products[0]


def get_service_name_from_url(dataset_url) -> ServiceName:
    if dataset_url.startswith("ftp://"):
        service = ServiceName.FTP
    elif "/motu-web/Motu" in dataset_url:
        service = ServiceName.MOTU
    elif "/thredds/dodsC/" in dataset_url:
        service = ServiceName.OPENDAP
    elif "/mdl-arco-time/" in dataset_url:
        service = ServiceName.TIMESERIES
    elif "/mdl-arco-geo/" in dataset_url:
        service = ServiceName.GEOSERIES
    elif "/mdl-native/" in dataset_url:
        service = ServiceName.FILES
    else:
        exception = ValueError(f"No service matching url: {dataset_url}")
        logging.error(exception)
        raise exception
    return service


def get_service_url(
    dataset: CopernicusMarineProductDataset, service_name: ServiceName
) -> str:
    service_urls = iter(
        [
            service.uri
            for service in dataset.services
            if service.service_name == service_name
        ]
    )
    return next(service_urls, "")


def get_dataset_url_from_id(
    catalogue: CopernicusMarineCatalogue, dataset_id: str, service: ServiceName
) -> str:
    dataset = get_dataset_from_id(catalogue, dataset_id)
    return get_service_url(dataset, service)


def filter_catalogue_with_strings(
    catalogue: CopernicusMarineCatalogue, tokens: list[str]
) -> Optional[CopernicusMarineCatalogue]:
    filtered_catalogue = deepcopy(catalogue)
    return find_match_object(filtered_catalogue, tokens)


def find_match_object(value: Any, tokens: list[str]) -> Any:
    match: Any
    if isinstance(value, str):
        match = find_match_string(value, tokens)
    elif isinstance(value, list):
        match = find_match_list(value, tokens)
    elif hasattr(value, "__dict__"):
        match = find_match_dict(value, tokens)
    else:
        match = None
    return match


def find_match_string(string: str, tokens: list[str]) -> Optional[str]:
    return string if any(token in string for token in tokens) else None


def find_match_list(object_list: list[Any], tokens) -> Optional[list[Any]]:
    def find_match(element: Any) -> Optional[Any]:
        return find_match_object(element, tokens)

    filtered_list: list[Any] = list(map_reject_none(find_match, object_list))
    return filtered_list if filtered_list else None


def find_match_dict(
    structure: dict[str, Any], tokens
) -> Optional[dict[str, Any]]:
    filtered_dict = {
        key: find_match_object(value, tokens)
        for key, value in structure.__dict__.items()
        if find_match_object(value, tokens)
    }

    found_match = any(filtered_dict.values())
    if found_match:
        new_dict = dict(structure.__dict__, **filtered_dict)
        structure.__dict__ = new_dict
    return structure if found_match else None
