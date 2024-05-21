import pytest
from integration_tests.conftest import random_data
from models.response_models import GenericIsSuccessResponse
from test_helpers.test_helpers import (
    assert_response_success_status,
    validate_response,
    data_for_invalid_brightness_levels,
    data_for_invalid_colors,
    data_for_invalid_names,
)


@pytest.mark.smoke
@pytest.mark.parametrize("content_type", ["json", "form"])
def test_set_brightness(client, random_data, content_type):
    """
    Tests setting the brightness of a connected device using different content types.

    This test connects to a random device, sets its brightness to a random value,
    and verifies that the brightness is set correctly.

    Args:
        client: The DeviceAPIClient fixture.
        random_data: The RandomDataGenerator fixture.
        content_type: The content type for the request ("json" or "form").

    Assertions:
        - The response from setting the brightness matches the expected response model.
        - The response from setting the brightness is successful.
        - The final brightness value matches the set value.
    """
    # Arrange
    client.connect_to_a_random_device()
    
    # Act
    value = random_data.random_brightness()
    response = client.set_brightness(value, content_type)
    
    # Assert
    validate_response(model=GenericIsSuccessResponse, response=response)
    assert_response_success_status(response)
    final_value = client.get_specific_state("brightness")
    assert value == final_value


@pytest.mark.parametrize(
    "content_type, invalid_brightness_level", data_for_invalid_brightness_levels()
)
def test_set_brightness_invalid(client, content_type, invalid_brightness_level):
    """
    Tests setting an invalid brightness level for a connected device.

    This test connects to a random device, attempts to set its brightness to an invalid value,
    and verifies that the operation fails.

    Args:
        client: The DeviceAPIClient fixture.
        content_type: The content type for the request ("json" or "form").
        invalid_brightness_level: The invalid brightness level to set.

    Assertions:
        - The response from setting the brightness is unsuccessful.
    """
    # Arrange
    client.connect_to_a_random_device()
    
    # Act
    response = client.set_brightness(invalid_brightness_level, content_type)
    
    # Assert
    assert_response_success_status(response, success=False)


@pytest.mark.smoke
@pytest.mark.parametrize("content_type", ["json", "form"])
def test_set_color(client, random_data, content_type):
    """
    Tests setting the color of a connected device using different content types.

    This test connects to a random device, sets its color to a random value,
    and verifies that the color is set correctly.

    Args:
        client: The DeviceAPIClient fixture.
        random_data: The RandomDataGenerator fixture.
        content_type: The content type for the request ("json" or "form").

    Assertions:
        - The response from setting the color matches the expected response model.
        - The response from setting the color is successful.
        - The final color value matches the set value.
    """
    # Arrange
    client.connect_to_a_random_device()
    value = random_data.random_color()

    # Act
    response = client.set_color(value, content_type)
    
    # Assert
    validate_response(model=GenericIsSuccessResponse, response=response)
    assert_response_success_status(response)
    final_value = client.get_specific_state("color")
    assert value == final_value


@pytest.mark.parametrize("content_type, invalid_color", data_for_invalid_colors())
def test_set_color_invalid(client, content_type, invalid_color):
    """
    Tests setting an invalid color for a connected device.

    This test connects to a random device, attempts to set its color to an invalid value,
    and verifies that the operation fails.

    Args:
        client: The DeviceAPIClient fixture.
        content_type: The content type for the request ("json" or "form").
        invalid_color: The invalid color value to set.

    Assertions:
        - The response from setting the color is unsuccessful.
    """
    # Arrange
    client.connect_to_a_random_device()

    # Act
    response = client.set_color(invalid_color, content_type)

    # Assert
    assert_response_success_status(response, success=False)


@pytest.mark.smoke
@pytest.mark.parametrize("content_type", ["json", "form"])
def test_set_name(client, random_data, content_type):
    """
    Tests setting the name of a connected device using different content types.

    This test connects to a random device, sets its name to a random value,
    and verifies that the name is set correctly.

    Args:
        client: The DeviceAPIClient fixture.
        random_data: The RandomDataGenerator fixture.
        content_type: The content type for the request ("json" or "form").

    Assertions:
        - The response from setting the name matches the expected response model.
        - The response from setting the name is successful.
        - The final name value matches the set value.
    """
    # Arrange
    client.connect_to_a_random_device()
    value = random_data.random_name()

    # Act
    response = client.set_name(value, content_type)

    # Assert
    validate_response(model=GenericIsSuccessResponse, response=response)
    assert_response_success_status(response)
    final_value = client.get_specific_state("name")
    assert value == final_value


@pytest.mark.parametrize(
    "content_type, invalid_name",
    data_for_invalid_names(),
)
def test_set_name_invalid(client, content_type, invalid_name):
    """
    Tests setting an invalid name for a connected device.

    This test connects to a random device, attempts to set its name to an invalid value,
    and verifies that the operation fails.

    Args:
        client: The DeviceAPIClient fixture.
        content_type: The content type for the request ("json" or "form").
        invalid_name: The invalid name value to set.

    Assertions:
        - The response from setting the name is unsuccessful.
    """
    # Arrange
    client.connect_to_a_random_device()

    # Act
    response = client.set_name(invalid_name, content_type)

    # Assert
    assert_response_success_status(response, success=False)


@pytest.mark.parametrize("content_type", ["json", "form"])
def test_set_brightness_without_connecting_to_a_device(client, random_data, content_type):
    """
    Tests setting the brightness of a device without connecting to it first.

    This test attempts to set the brightness of a device without connecting to it,
    and verifies that the operation fails.

    Args:
        client: The DeviceAPIClient fixture.
        random_data: The RandomDataGenerator fixture.
        content_type: The content type for the request ("json" or "form").

    Assertions:
        - The response from setting the brightness is unsuccessful.
    """
    # Arrange
    value = random_data.random_brightness()

    # Act
    response = client.set_brightness(value, content_type)

    # Assert
    assert_response_success_status(response, success=False)


@pytest.mark.parametrize("content_type", ["json", "form"])
def test_set_name_without_connecting_to_a_device(client, random_data, content_type):
    """
    Tests setting the name of a device without connecting to it first.

    This test attempts to set the name of a device without connecting to it,
    and verifies that the operation fails.

    Args:
        client: The DeviceAPIClient fixture.
        random_data: The RandomDataGenerator fixture.
        content_type: The content type for the request ("json" or "form").

    Assertions:
        - The response from setting the name is unsuccessful.
    """
    # Arrange
    value = random_data.random_name()

    # Act
    response = client.set_name(value, content_type)

    # Assert
    assert_response_success_status(response, success=False)


@pytest.mark.parametrize("content_type", ["json", "form"])
def test_set_color_without_connecting_to_a_device(client, random_data, content_type):
    """
    Tests setting the color of a device without connecting to it first.

    This test attempts to set the color of a device without connecting to it,
    and verifies that the operation fails.

    Args:
        client: The DeviceAPIClient fixture.
        random_data: The RandomDataGenerator fixture.
        content_type: The content type for the request ("json" or "form").

    Assertions:
        - The response from setting the color is unsuccessful.
    """
    # Arrange
    value = random_data.random_color()

    # Act
    response = client.set_color(value, content_type)

    # Assert
    assert_response_success_status(response, success=False)
