import pytest
from models.response_models import GenericIsSuccessResponse
from test_helpers.test_helpers import (
    assert_response_success_status,
    validate_response,
)


@pytest.mark.smoke
@pytest.mark.parametrize("content_type", ["json", "form"])
def test_connect_device(client, random_data, content_type):
    """
    Tests the connection to a device using different content types.

    This test retrieves a random connected device, attempts to connect to it using
    the specified content type, and verifies that the connection is successful.

    Args:
        client: The DeviceAPIClient fixture.
        random_data: The RandomDataGenerator fixture.
        content_type: The content type for the request ("json" or "form").

    Assertions:
        - The response from connecting to the device matches the expected response model.
        - The response from connecting to the device is successful.
    """
    # Arrange
    device = client.get_random_connected_device()
    device_ip = device.get("ip")

    # Act
    response = client.connect_device(device_ip, content_type)
    
    # Assert
    validate_response(model=GenericIsSuccessResponse, response=response)
    assert_response_success_status(response)


@pytest.mark.parametrize("content_type", ["json", "form"])
def test_connect_device_invalid_ip(client, random_data, content_type):
    """
    Tests the connection to a device with an invalid IP address using different content types.

    This test generates a random private IP address, attempts to connect to it using
    the specified content type, and verifies that the connection fails.

    Args:
        client: The DeviceAPIClient fixture.
        random_data: The RandomDataGenerator fixture.
        content_type: The content type for the request ("json" or "form").

    Assertions:
        - The response from connecting to the device is unsuccessful.
    """
    # Arrange
    ip = random_data.random_private_ip()

    # Act
    response = client.connect_device(ip, content_type)

    # Assert
    assert_response_success_status(response, success=False)


@pytest.mark.parametrize("content_type", ["json", "form"])
def test_connect_device_to_already_connected_device(client, random_data, content_type):
    """
    Tests the connection to an already connected device using different content types.

    This test connects to a random device, then attempts to connect to the same device
    again using the specified content type, and verifies that the second connection attempt fails.

    Args:
        client: The DeviceAPIClient fixture.
        random_data: The RandomDataGenerator fixture.
        content_type: The content type for the request ("json" or "form").

    Assertions:
        - The response from the second connection attempt is unsuccessful.
    """
    # Arrange
    ip = client.connect_to_a_random_device()

    # Act
    response = client.connect_device(ip, content_type)

    # Assert
    assert_response_success_status(response, success=False)
