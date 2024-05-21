import pytest
from test_helpers.test_helpers import validate_response
from models.response_models import DevicesResponse


@pytest.mark.smoke
def test_list_devices(client):
    """
    Tests listing the devices on the network.

    This test sends a request to list all devices on the network, verifies that the response
    status code is 200, and checks that the response matches the expected DevicesResponse model.
    It also verifies that the response contains a list of devices with the expected attributes.

    Args:
        client: The DeviceAPIClient fixture.

    Assertions:
        - The response status code is 200.
        - The response matches the expected DevicesResponse model.
        - The response contains a list of devices.
        - Each device in the list contains the "name" and "ip" attributes, and they are not None.
    """
    # Act
    response = client.list_devices()

    # Assert
    assert response.status_code == 200
    validate_response(model=DevicesResponse, response=response)

    devices = response.json()
    assert isinstance(devices, list)
    for device in devices:
        assert "name" in device
        assert "ip" in device
        assert device.get("name") is not None
        assert device.get("ip") is not None


def test_list_devices_with_invalid_body(client, random_data):
    """
    Tests listing the devices with an invalid request body.

    This test sends a request to list devices with an invalid JSON body and verifies
    that the response status code is 400 (Bad Request).

    Args:
        client: The DeviceAPIClient fixture.
        random_data: The RandomDataGenerator fixture.

    Assertions:
        - The response status code is 400 (Bad Request).
    """
    # Act
    response = client.list_devices(data=random_data.random_json())

    # Assert
    assert response.status_code == 400
