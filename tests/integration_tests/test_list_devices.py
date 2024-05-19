import pytest

@pytest.mark.smoke
@pytest.mark.parametrize("expected_status_code", [200])
def test_list_devices(client, expected_status_code):
    response = client.list_devices()
    assert response.status_code == expected_status_code
    devices = response.json()
    assert isinstance(devices, list)
    for device in devices:
        assert 'name' in device
        assert 'ip' in device
        assert device.get('name') is not None
        assert device.get('ip') is not None