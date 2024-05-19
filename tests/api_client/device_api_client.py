import json
import random
import requests
from urllib.parse import urlencode
from tests.utils.utils import log_request, log_response
from tests.random_data.random_data import RandomDataGenerator


class DeviceAPIClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = timeout
        self.session.hooks["response"] = [log_request, log_response]

    def list_devices(self, data=None, params=None):
        headers = None
        url = f"{self.base_url}/devices"
        if data is not None:
            headers = {"Content-Type": "application/json"}
        response = self.session.get(url, headers=headers, data=data, params=params)
        return response

    def connect_device(self, ip, content_type="json"):
        url = f"{self.base_url}/connect"
        headers = (
            {"Content-Type": "application/json"}
            if content_type == "json"
            else {"Content-Type": "application/x-www-form-urlencoded"}
        )
        data = {"ip": ip}
        
        if content_type == "json":
            data = json.dumps(data)
        else:
            data = urlencode(data)

        response = self.session.post(url, data=data, headers=headers, timeout=self.timeout)
        return response

    def get_device_state(self, data=None, params=None):
        headers = None
        url = f"{self.base_url}/state"
        if data is not None:
            headers = {"Content-Type": "application/json"}
        response = self.session.get(url, headers=headers, data=data, params=params)

        return response

    def set_brightness(self, value, content_type="json"):
        url = f"{self.base_url}/brightness"
        headers = (
            {"Content-Type": "application/json"}
            if content_type == "json"
            else {"Content-Type": "application/x-www-form-urlencoded"}
        )
        data = {"brightness": value}
        if content_type == "json":
            data = json.dumps(data)
        else:
            data = urlencode(data)
        response = self.session.post(url, data=data, headers=headers, timeout=self.timeout)
        return response

    def set_color(self, value, content_type="json"):
        url = f"{self.base_url}/color"
        headers = (
            {"Content-Type": "application/json"}
            if content_type == "json"
            else {"Content-Type": "application/x-www-form-urlencoded"}
        )
        data = {"color": value}
        if content_type == "json":
            data = json.dumps(data)
        else:
            data = urlencode(data)
        response = self.session.post(url, data=data, headers=headers, timeout=self.timeout)
        return response

    def set_name(self, value, content_type="json"):
        url = f"{self.base_url}/name"
        headers = (
            {"Content-Type": "application/json"}
            if content_type == "json"
            else {"Content-Type": "application/x-www-form-urlencoded"}
        )
        data = {"name": value}
        
        if content_type == "json":
            data = json.dumps(data)
        else:
            data = urlencode(data)

        response = self.session.post(url, data=data, headers=headers, timeout=self.timeout)
        return response

    def execute_automation_task(self):
        url = f"{self.base_url}/chilltime"
        response = self.session.post(url, timeout=self.timeout)
        return response

    def disconnect_device(self):
        url = f"{self.base_url}/disconnect"
        response = self.session.post(url, timeout=self.timeout)
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
        state = device_states[state_name]

        return state
    
    def get_brightness_after_chilltime(self):
        self.execute_automation_task()
        brightness_level = self.get_specific_state('brightness')

        return brightness_level
    

