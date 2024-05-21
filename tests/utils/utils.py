from typing import Any, List, Tuple
from itertools import product
from loguru import logger


def log_request(response: Any, *args: Any, **kwargs: Any) -> None:
    """
    Logs the details of an HTTP request.

    This function logs the HTTP method, URL, headers, and body of the request associated with the given response object.

    Args:
        response (Any): The response object containing the request information.
        *args (Any): Additional arguments (unused in this function).
        **kwargs (Any): Additional keyword arguments (unused in this function).
    """
    logger.debug(f"Request: {response.request.method} {response.request.url}")
    logger.debug(f"Headers: {response.request.headers}")
    logger.debug(f"Body: {response.request.body}")


def log_response(response: Any, *args: Any, **kwargs: Any) -> None:
    """
    Logs the details of an HTTP response.

    This function logs the status code, headers, and body of the given response object.

    Args:
        response (Any): The response object containing the response information.
        *args (Any): Additional arguments (unused in this function).
        **kwargs (Any): Additional keyword arguments (unused in this function).
    """
    logger.debug(f"Response Status Code: {response.status_code}")
    logger.debug(f"Response Headers: {response.headers}")
    logger.debug(f"Response Body: {response.text}")

def generate_combinations(tuple_list: List[Tuple[Any, ...]]) -> List[Tuple[Any, ...]]:
    """
    Generates the Cartesian product of a list of tuples.

    This function takes a list of tuples and returns a list containing the Cartesian product of these tuples.

    Args:
        tuple_list (List[Tuple[Any, ...]]): A list of tuples to combine.

    Returns:
        List[Tuple[Any, ...]]: A list of tuples representing the Cartesian product of the input tuples.
    """
    return list(product(*tuple_list))
