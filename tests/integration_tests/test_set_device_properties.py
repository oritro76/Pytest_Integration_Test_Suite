import pytest
from tests.integration_tests.conftest import random_data
from tests.models.response_models import GenericIsSuccessResponse
from tests.test_helpers.test_helpers import (
    assert_response_success_status,
    validate_response,
    data_for_invalid_brightness_levels,
    data_for_invalid_colors,
    data_for_invalid_names,
)


@pytest.mark.smoke
@pytest.mark.parametrize("content_type", ["json", "form"])
def test_set_brightness(client, random_data, content_type):
    client.connect_to_a_random_device()
    value = random_data.random_brightness()
    response = client.set_brightness(value, content_type)

    validate_response(model=GenericIsSuccessResponse, response=response)

    assert_response_success_status(response)

    final_value = client.get_specific_state("brightness")

    assert value == final_value


@pytest.mark.parametrize(
    "content_type, invalid_brightness_level", data_for_invalid_brightness_levels()
)
def test_set_brightness_invalid(client, content_type, invalid_brightness_level):
    client.connect_to_a_random_device()
    response = client.set_brightness(invalid_brightness_level, content_type)
    assert_response_success_status(response, success=False)


@pytest.mark.smoke
@pytest.mark.parametrize("content_type", ["json", "form"])
def test_set_color(client, random_data, content_type):
    client.connect_to_a_random_device()
    value = random_data.random_color()
    response = client.set_color(value, content_type)

    validate_response(model=GenericIsSuccessResponse, response=response)

    assert_response_success_status(response)

    final_value = client.get_specific_state("color")

    assert value == final_value


@pytest.mark.parametrize("content_type, invalid_color", data_for_invalid_colors())
def test_set_color_invalid(client, content_type, invalid_color):
    client.connect_to_a_random_device()
    response = client.set_color(invalid_color, content_type)
    assert_response_success_status(response, success=False)


@pytest.mark.smoke
@pytest.mark.parametrize("content_type", ["json", "form"])
def test_set_name(client, random_data, content_type):
    client.connect_to_a_random_device()
    value = random_data.random_name()
    response = client.set_name(value, content_type)
    validate_response(model=GenericIsSuccessResponse, response=response)
    assert_response_success_status(response)

    final_value = client.get_specific_state("name")

    assert value == final_value


@pytest.mark.parametrize(
    "content_type, invalid_name",
    data_for_invalid_names(),
)
def test_set_name_invalid(client, content_type, invalid_name):
    client.connect_to_a_random_device()
    response = client.set_name(invalid_name, content_type)
    assert_response_success_status(response, success=False)


@pytest.mark.parametrize("content_type", ["json", "form"])
def test_set_brightness_without_connecting_to_a_device(
    client, random_data, content_type
):
    value = random_data.random_brightness()
    response = client.set_brightness(value, content_type)
    assert_response_success_status(response, success=False)


@pytest.mark.parametrize("content_type", ["json", "form"])
def test_set_name_without_connecting_to_a_device(client, random_data, content_type):
    value = random_data.random_name()
    response = client.set_name(value, content_type)
    assert_response_success_status(response, success=False)


@pytest.mark.parametrize("content_type", ["json", "form"])
def test_set_color_without_connecting_to_a_device(client, random_data, content_type):
    value = random_data.random_color()
    response = client.set_color(value, content_type)
    assert_response_success_status(response, success=False)
