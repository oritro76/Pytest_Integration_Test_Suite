import pytest
from models.response_models import GenericIsSuccessResponse
from test_helpers.test_helpers import (
    assert_response_success_status,
    validate_response,
)


@pytest.mark.smoke
@pytest.mark.parametrize("content_type", ["json", "form"])
def test_connect_device(client, random_data, content_type):
    #arrange
    device = client.get_random_connected_device()
    device_ip = device.get("ip")

    #act
    response = client.connect_device(device_ip, content_type)
    
    #assert
    validate_response(model=GenericIsSuccessResponse, response=response)
    assert_response_success_status(response)


@pytest.mark.parametrize("content_type", ["json", "form"])
def test_connect_device_invalid_ip(client, random_data, content_type):
    #arrange
    ip = random_data.random_private_ip()

    #act
    response = client.connect_device(ip, content_type)

    #assert
    assert_response_success_status(response, success=False)


@pytest.mark.parametrize("content_type", ["json", "form"])
def test_connect_device_to_already_connected_device(client, random_data, content_type):
    #arrange
    ip = client.connect_to_a_random_device()

    #act
    response = client.connect_device(ip, content_type)

    #assert
    assert_response_success_status(response, success=False)
