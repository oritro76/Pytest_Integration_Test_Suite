import pytest
from tests.test_helpers.test_helpers import assert_response_success_status

@pytest.mark.smoke

def test_disconnect(client):
    client.connect_to_a_random_device()

    response = client.disconnect_device()
    assert_response_success_status(response)
