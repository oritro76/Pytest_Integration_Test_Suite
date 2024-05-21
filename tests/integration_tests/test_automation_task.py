import pytest
from models.response_models import GenericIsSuccessResponse
from test_helpers.test_helpers import (
    assert_response_success_status,
    validate_response,
)
from device_settings.settings import CHILLTIME_FINAL_BRIGHTNESS


@pytest.mark.smoke
def test_automation_task(client):
    """
    Tests the automation task execution with an initial brightness level.

    This test connects to a random device, sets its brightness to an initial level,
    executes the automation task, and verifies that the final brightness level is less than the initial level.

    Args:
        client: The DeviceAPIClient fixture.

    Assertions:
        - The response from setting the brightness is successful.
        - The response from executing the automation task is successful and matches the expected response model.
        - The final brightness level is less than the initial brightness level.
    """
    # Arrange
    initial_brightness_level = 9.0
    client.connect_to_a_random_device()

    response = client.set_brightness(value=initial_brightness_level)
    assert_response_success_status(response)

    # Act
    response = client.execute_automation_task()

    # Assert
    validate_response(model=GenericIsSuccessResponse, response=response)
    assert_response_success_status(response)

    final_brightness_level = client.get_specific_state("brightness")

    assert final_brightness_level < initial_brightness_level


@pytest.mark.smoke
@pytest.mark.parametrize(
    "initial_brightness_level", [10.0, 1.0, CHILLTIME_FINAL_BRIGHTNESS, 5.0]
)
def test_automation_task_with_different_brightness_level(client, initial_brightness_level):
    """
    Tests the automation task execution with various initial brightness levels.

    This test connects to a random device, sets its brightness to various initial levels,
    executes the automation task, and verifies that the final brightness level matches the expected brightness level.

    Args:
        client: The DeviceAPIClient fixture.
        initial_brightness_level: The initial brightness level to set.

    Assertions:
        - The response from setting the brightness is successful.
        - The final brightness level matches the expected brightness level.
    """
    # Arrange
    final_brightness_level = None
    expected_brightness_level = CHILLTIME_FINAL_BRIGHTNESS

    client.connect_to_a_random_device()

    response = client.set_brightness(value=initial_brightness_level)
    assert_response_success_status(response)

    if initial_brightness_level <= CHILLTIME_FINAL_BRIGHTNESS:
        expected_brightness_level = initial_brightness_level

    # Act
    while initial_brightness_level > CHILLTIME_FINAL_BRIGHTNESS:
        initial_brightness_level = client.get_brightness_after_chilltime()

    final_brightness_level = client.get_brightness_after_chilltime()

    # Assert
    assert final_brightness_level == expected_brightness_level


def test_automation_task_without_connection(client):
    """
    Tests the automation task execution without an active device connection.

    This test attempts to execute the automation task without connecting to a device
    and verifies that the operation fails.

    Args:
        client: The DeviceAPIClient fixture.

    Assertions:
        - The response from executing the automation task is unsuccessful.
    """
    # Act
    response = client.execute_automation_task()

    # Assert
    assert_response_success_status(response, success=False)
