import pytest
from models.response_models import StateResponse
from test_helpers.test_helpers import (
    assert_response_success_status,
    validate_response,
)


@pytest.mark.smoke
def test_get_state(client):
    #arrange
    client.connect_to_a_random_device()

    #act
    response = client.get_device_state()

    #assert
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
    #act
    response = client.get_device_state()

    #assert
    assert_response_success_status(response, success=False)

def test_get_state_after_disconnecting_to_a_device(client):
    #arrange
    client.connect_to_a_random_device()
    client.disconnect_device()

    #act
    response = client.get_device_state()

    #assert
    assert_response_success_status(response, success=False)


def test_get_state_with_invalid_body(client, random_data):
    #act
    response = client.get_device_state(data=random_data.random_json())

    #assert
    assert response.status_code == 400
