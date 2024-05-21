import pytest
from models.response_models import GenericIsSuccessResponse
from test_helpers.test_helpers import (
    assert_response_success_status,
    validate_response,
)


@pytest.mark.smoke
def test_disconnect(client):
    """
    Tests disconnecting from a connected device.

    This test connects to a random device, attempts to disconnect from it,
    and verifies that the disconnection is successful.

    Args:
        client: The DeviceAPIClient fixture.

    Assertions:
        - The response from disconnecting from the device matches the expected response model.
        - The response from disconnecting from the device is successful.
    """
    # Arrange
    client.connect_to_a_random_device()

    # Act
    response = client.disconnect_device()

    # Assert
    validate_response(model=GenericIsSuccessResponse, response=response)
    assert_response_success_status(response)


def test_disconnect_with_invalid_body(client, random_data):
    """
    Tests disconnecting from a device with an invalid request body.

    This test connects to a random device, attempts to disconnect from it using
    an invalid JSON body, and verifies that the response from disconnecting from the device is unsuccessful.

    Args:
        client: The DeviceAPIClient fixture.
        random_data: The RandomDataGenerator fixture.

    Assertions:
        - The response from disconnecting from the device is unsuccessful.
    """
    # Arrange
    client.connect_to_a_random_device()

    # Act
    response = client.disconnect_device(data=random_data.random_json())

    # Assert
    assert_response_success_status(response, success=False)
