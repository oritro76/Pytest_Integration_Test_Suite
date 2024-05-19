from typing import Any, List, Tuple
from itertools import product
from loguru import logger


def log_request(response: Any, *args: Any, **kwargs: Any) -> None:

    logger.debug(f"Request: {response.request.method} {response.request.url}")
    logger.debug(f"Headers: {response.request.headers}")
    logger.debug(f"Body: {response.request.body}")


def log_response(response: Any, *args: Any, **kwargs: Any) -> None:

    logger.debug(f"Response Status Code: {response.status_code}")
    logger.debug(f"Response Headers: {response.headers}")
    logger.debug(f"Response Body: {response.text}")

def generate_combinations(tuple_list: List[Tuple[Any, ...]]) -> List[Tuple[Any, ...]]:

    return list(product(*tuple_list))
