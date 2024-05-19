import pytest
from tests.test_helpers.test_helpers import assert_response_success_status

@pytest.mark.smoke
@pytest.mark.parametrize("content_type", ['json', 'form'])
def test_connect_device(client, random_data, content_type):
    device = client.get_random_connected_device()
    device_ip = device.get("ip")
    response = client.connect_device(device_ip, content_type)
    assert_response_success_status(response)


@pytest.mark.parametrize("content_type", ['json', 'form'])
def test_connect_device_invalid_ip(client, random_data, content_type):
    ip = random_data.random_private_ip()
    response = client.connect_device(ip, content_type)
    assert_response_success_status(response, success=False)


@pytest.mark.parametrize("content_type", ['json', 'form'])
def test_connect_device_to_already_connected_device(client, random_data, content_type):
    ip = random_data.random_private_ip()
    response = client.connect_device(ip, content_type)
    assert_response_success_status(response, success=True)

    response = client.connect_device(ip, content_type)
    assert_response_success_status(response, success=False)