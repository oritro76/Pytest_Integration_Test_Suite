import pytest
from tests.test_helpers.test_helpers import assert_response_success_status

@pytest.mark.smoke
def test_get_state(client):
    client.connect_to_a_random_device()
    response = client.get_device_state()
    assert response.status_code == 200
    result = response.json()
    
    assert 'name' in result
    assert 'ip' in result
    assert 'color' in result
    assert 'brightness' in result
    assert result.get('name') is not None
    assert result.get('ip') is not None
    assert result.get('color') is not None
    assert result.get('brightness') is not None


def test_get_state_without_connecting_to_a_device(client):
    response = client.get_device_state()
    assert_response_success_status(response, success=False)
    