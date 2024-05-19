import pytest

from tests.api_client.device_api_client import DeviceAPIClient
from tests.random_data.random_data import RandomDataGenerator
from tests.utils.utils import generate_combinations

BASE_URL = "http://localhost:8081"

@pytest.fixture(scope='function')
def client():
    client = DeviceAPIClient(BASE_URL)
    yield client
    client.disconnect_device() 

@pytest.fixture(scope='module')
def random_data():
    return RandomDataGenerator()