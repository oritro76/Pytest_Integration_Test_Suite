import pytest
from tests.test_helpers.test_helpers import validate_response
from tests.models.response_models import DevicesResponse


@pytest.mark.smoke
@pytest.mark.parametrize("expected_status_code", [200])
def test_list_devices(client, expected_status_code):
    response = client.list_devices()
    assert response.status_code == expected_status_code

    validate_response(model=DevicesResponse, response=response)

    devices = response.json()
    assert isinstance(devices, list)
    for device in devices:
        assert "name" in device
        assert "ip" in device
        assert device.get("name") is not None
        assert device.get("ip") is not None
