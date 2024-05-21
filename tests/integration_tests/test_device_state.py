import pytest
from models.response_models import StateResponse
from test_helpers.test_helpers import (
    assert_response_success_status,
    validate_response,
)


@pytest.mark.smoke
def test_get_state(client):
    """
    Tests retrieving the state of a connected device.

    This test connects to a random device, retrieves its state, and verifies that the state response contains
    the expected attributes and matches the expected response model.

    Args:
        client: The DeviceAPIClient fixture.

    Assertions:
        - The response status code is 200.
        - The response matches the expected StateResponse model.
        - The response contains the "name", "ip", "color", and "brightness" attributes, and they are not None.
    """
    # Arrange
    client.connect_to_a_random_device()

    # Act
    response = client.get_device_state()

    # Assert
    assert response.status_code == 200
    result = response.json()

    validate_response(model=StateResponse, response=response)
    assert "name" in result
    assert "ip" in result
    assert "color" in result
    assert "brightness" in result
    assert result.get("name") is not None
    assert result.get("ip") is not None
    assert result.get("color") is not None
    assert result.get("brightness") is not None


def test_get_state_without_connecting_to_a_device(client):
    """
    Tests retrieving the state of a device without connecting to it.

    This test attempts to retrieve the state of a device without first connecting to it
    and verifies that the operation fails.

    Args:
        client: The DeviceAPIClient fixture.

    Assertions:
        - The response from getting the device state is unsuccessful.
    """
    # Act
    response = client.get_device_state()

    # Assert
    assert_response_success_status(response, success=False)


def test_get_state_after_disconnecting_from_a_device(client):
    """
    Tests retrieving the state of a device after disconnecting from it.

    This test connects to a random device, disconnects from it, and then attempts to retrieve its state,
    verifying that the operation fails.

    Args:
        client: The DeviceAPIClient fixture.

    Assertions:
        - The response from getting the device state is unsuccessful.
    """
    # Arrange
    client.connect_to_a_random_device()
    client.disconnect_device()

    # Act
    response = client.get_device_state()

    # Assert
    assert_response_success_status(response, success=False)


def test_get_state_with_invalid_body(client, random_data):
    """
    Tests retrieving the state of a device with an invalid request body.

    This test attempts to retrieve the state of a device using an invalid JSON body
    and verifies that the response status code is 400 (Bad Request).

    Args:
        client: The DeviceAPIClient fixture.
        random_data: The RandomDataGenerator fixture.

    Assertions:
        - The response status code is 400 (Bad Request).
    """
    # Act
    response = client.get_device_state(data=random_data.random_json())

    # Assert
    assert response.status_code == 400
