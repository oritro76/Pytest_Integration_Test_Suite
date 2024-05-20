import pytest

from tests.api_client.device_api_client import DeviceAPIClient
from tests.random_data.random_data import RandomDataGenerator
from tests.settings import APP_BASE_URL

@pytest.fixture(scope='function')
def client():
    client = DeviceAPIClient(APP_BASE_URL)
    client.disconnect_device() 
    yield client
    client.disconnect_device() 

@pytest.fixture(scope='module')
def random_data():
    return RandomDataGenerator()