import random
import requests
from tests.utils.utils import log_request, log_response
from tests.random_data.random_data import RandomDataGenerator


class DeviceAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.hooks["response"] = [log_request, log_response]

    def list_devices(self):
        url = f"{self.base_url}/devices"
        response = self.session.get(url)
        return response

    def connect_device(self, ip, content_type="json"):
        url = f"{self.base_url}/connect"
        headers = (
            {"Content-Type": "application/json"}
            if content_type == "json"
            else {"Content-Type": "application/x-www-form-urlencoded"}
        )
        data = {"ip": ip}
        response = self.session.post(url, data=data, headers=headers)
        return response

    def get_device_state(self):
        url = f"{self.base_url}/state"
        response = self.session.get(url)
        return response

    def set_brightness(self, value, content_type="json"):
        url = f"{self.base_url}/brightness"
        headers = (
            {"Content-Type": "application/json"}
            if content_type == "json"
            else {"Content-Type": "application/x-www-form-urlencoded"}
        )
        data = {"brightness": value}
        response = self.session.post(url, data=data, headers=headers)
        return response

    def set_color(self, value, content_type="json"):
        url = f"{self.base_url}/color"
        headers = (
            {"Content-Type": "application/json"}
            if content_type == "json"
            else {"Content-Type": "application/x-www-form-urlencoded"}
        )
        data = {"color": value}
        response = self.session.post(url, data=data, headers=headers)
        return response

    def set_name(self, value, content_type="json"):
        url = f"{self.base_url}/name"
        headers = (
            {"Content-Type": "application/json"}
            if content_type == "json"
            else {"Content-Type": "application/x-www-form-urlencoded"}
        )
        data = {"name": value}
        response = self.session.post(url, data=data, headers=headers)
        return response

    def execute_automation_task(self):
        url = f"{self.base_url}/chilltime"
        response = self.session.post(url)
        return response

    def disconnect_device(self):
        url = f"{self.base_url}/disconnect"
        response = self.session.post(url)
        return response
    
    def get_random_connected_device(self):
        response = self.list_devices()
        print(response.json())
        device_list = response.json()
        device = random.choice(device_list)
        return device

    def connect_to_a_random_device(self):
        device = self.get_random_connected_device()
        device_ip = device.get("ip")
        self.connect_device(ip=device_ip)

        return device_ip
    
    def get_specific_state(self, state_name="brightness"):
        response = self.get_device_state()
        device_states = (response.json())
        state = device_states.get(state_name)

        return state
    
    def get_brightness_after_chilltime(self):
        self.execute_automation_task()
        brightness_level = self.get_specific_state('brightness')

        return brightness_level
    

