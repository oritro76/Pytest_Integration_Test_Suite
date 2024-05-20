import pytest
from test_helpers.test_helpers import validate_response
from models.response_models import DevicesResponse


@pytest.mark.smoke
def test_list_devices(client):
    #act
    response = client.list_devices()

    #assert
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
    #act
    response = client.list_devices(data=random_data.random_json())

    #assert
    assert response.status_code == 400
