import pytest
from tests.models.response_models import GenericIsSuccessResponse
from tests.test_helpers.test_helpers import (
    assert_response_success_status,
    validate_response,
)
from tests.device_settings.settings import CHILLTIME_FINAL_BRIGHTNESS


@pytest.mark.smoke
def test_automation_task(client):
    initial_brightness_level = 9.0
    client.connect_to_a_random_device()

    response = client.set_brightness(value=initial_brightness_level)
    assert_response_success_status(response)

    response = client.execute_automation_task()
    validate_response(model=GenericIsSuccessResponse, response=response)
    assert_response_success_status(response)

    final_brightness_level = client.get_specific_state("brightness")

    assert final_brightness_level < initial_brightness_level


@pytest.mark.smoke
@pytest.mark.parametrize("initial_brightness_level", [10.0, 1.0, 5.0])
def test_automation_task_with_different_brightness_level(
    client, initial_brightness_level
):
    final_brightness_level = None
    expected_brightness_level = CHILLTIME_FINAL_BRIGHTNESS

    client.connect_to_a_random_device()

    response = client.set_brightness(value=initial_brightness_level)
    assert_response_success_status(response)

    if initial_brightness_level <= CHILLTIME_FINAL_BRIGHTNESS:
        expected_brightness_level = initial_brightness_level

    while initial_brightness_level > CHILLTIME_FINAL_BRIGHTNESS:
        initial_brightness_level = client.get_brightness_after_chilltime()

    final_brightness_level = client.get_brightness_after_chilltime()

    assert final_brightness_level == expected_brightness_level


def test_automation_task_without_connection(client):

    response = client.execute_automation_task()
    assert_response_success_status(response, success=False)
