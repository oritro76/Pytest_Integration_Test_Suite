import pytest
from typing import List, Tuple, Any
from requests import Response
from random_data.random_data import RandomDataGenerator
from utils.utils import generate_combinations


def assert_response_success_status(response: Response, success: bool = True) -> None:
    assert response.status_code == 200
    isSuccess = response.json()
    assert isSuccess.get("success") == success

def data_for_invalid_names() -> List[Tuple[Any, ...]]:
    random_data = RandomDataGenerator()
    return generate_combinations(
        [
            ("json", "form"),
            random_data.invalid_names(),
        ]
    )

def data_for_invalid_colors() -> List[Tuple[Any, ...]]:
    random_data = RandomDataGenerator()
    return generate_combinations(
        [
            ("json", "form"),
            random_data.invalid_colors(),
        ]
    )

def data_for_invalid_brightness_levels() -> List[Tuple[Any, ...]]:
    random_data = RandomDataGenerator()
    return generate_combinations(
        [
            ("json", "form"),
            (
                random_data.random_invalid_brightness_greater_than_max_val(),
                random_data.random_invalid_brightness_lower_than_min_val(),
                "",
                random_data.random_name(),
                None
             ),
        ]
    )

def validate_response(model: Any, response: Response) -> Any:
    try:
        return model.model_validate(response.json())
    except Exception as e:
        pytest.fail(f"Response validation failed: {e}")
