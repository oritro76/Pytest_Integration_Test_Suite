import pytest
from tests.models.response_models import GenericIsSuccessResponse
from tests.test_helpers.test_helpers import (
    assert_response_success_status,
    validate_response,
)


@pytest.mark.smoke
def test_disconnect(client):
    client.connect_to_a_random_device()

    response = client.disconnect_device()

    validate_response(model=GenericIsSuccessResponse, response=response)

    assert_response_success_status(response)

def test_disconnect_with_invalid_body(client, random_data):
    client.connect_to_a_random_device()
    response = client.disconnect_device(data=random_data.random_json())
    assert response.status_code == 400
