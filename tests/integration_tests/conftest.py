import pytest
from api_client.device_api_client import DeviceAPIClient
from random_data.random_data import RandomDataGenerator
from settings import APP_BASE_URL

@pytest.fixture(scope='function')
def client():
    """
    Provides a DeviceAPIClient instance for each test function.

    This fixture initializes a DeviceAPIClient with the base URL of the application.
    Before yielding the client to the test, it ensures any existing connection is disconnected.
    After the test function completes, it disconnects the client again to ensure a clean state.

    Yields:
        DeviceAPIClient: An instance of the DeviceAPIClient.
    """
    client = DeviceAPIClient(APP_BASE_URL)
    client.disconnect_device() 
    yield client
    client.disconnect_device()

@pytest.fixture(scope='module')
def random_data():
    """
    Provides a RandomDataGenerator instance for the entire test module.

    This fixture initializes a RandomDataGenerator that can be used to generate random
    test data. The same instance is shared across all test functions within the module.

    Returns:
        RandomDataGenerator: An instance of the RandomDataGenerator.
    """
    return RandomDataGenerator()
