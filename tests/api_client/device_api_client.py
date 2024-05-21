import json
import random
import requests
from typing import Optional, Dict, Any
from urllib.parse import urlencode
from requests import Response
from utils.utils import log_request, log_response
from test_helpers.test_helpers import assert_response_success_status
from random_data.random_data import RandomDataGenerator


class DeviceAPIClient:
    def __init__(self, base_url: str, timeout: int = 10) -> None:
        """
        Initializes the DeviceAPIClient with the given base URL and timeout.

        Args:
            base_url (str): The base URL of the device API.
            timeout (int, optional): The timeout for API requests. Defaults to 10.
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = timeout
        self.session.hooks["response"] = [log_request, log_response]

    def list_devices(self, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Response:
        """
        Lists the devices available on the network.

        Args:
            data (Optional[Dict[str, Any]], optional): Data to send in the request body. Defaults to None.
            params (Optional[Dict[str, Any]], optional): Query parameters to include in the request. Defaults to None.

        Returns:
            Response: The response from the server.
        """
        headers = None
        url = f"{self.base_url}/devices"
        if data is not None:
            headers = {"Content-Type": "application/json"}
        response = self.session.get(url, headers=headers, data=data, params=params)
        return response

    def connect_device(self, ip: str, content_type: str = "json") -> Response:
        """
        Connects to a device given its IP address.

        Args:
            ip (str): The IP address of the device to connect to.
            content_type (str, optional): The content type for the request. Defaults to "json".

        Returns:
            Response: The response from the server.
        """
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

    def get_device_state(self, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Response:
        """
        Retrieves the state of the device.

        Args:
            data (Optional[Dict[str, Any]], optional): Data to send in the request body. Defaults to None.
            params (Optional[Dict[str, Any]], optional): Query parameters to include in the request. Defaults to None.

        Returns:
            Response: The response from the server.
        """
        headers = None
        url = f"{self.base_url}/state"
        if data is not None:
            headers = {"Content-Type": "application/json"}
        response = self.session.get(url, headers=headers, data=data, params=params)
        return response

    def set_brightness(self, value: float, content_type: str = "json") -> Response:
        """
        Sets the brightness of the device.

        Args:
            value (float): The brightness level to set.
            content_type (str, optional): The content type for the request. Defaults to "json".

        Returns:
            Response: The response from the server.
        """
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

    def set_color(self, value: str, content_type: str = "json") -> Response:
        """
        Sets the color of the device.

        Args:
            value (str): The color to set.
            content_type (str, optional): The content type for the request. Defaults to "json".

        Returns:
            Response: The response from the server.
        """
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

    def set_name(self, value: str, content_type: str = "json") -> Response:
        """
        Sets the name of the device.

        Args:
            value (str): The name to set.
            content_type (str, optional): The content type for the request. Defaults to "json".

        Returns:
            Response: The response from the server.
        """
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

    def execute_automation_task(self) -> Response:
        """
        Executes an automation task on the device.

        Returns:
            Response: The response from the server.
        """
        url = f"{self.base_url}/chilltime"
        response = self.session.post(url, timeout=self.timeout)
        return response

    def disconnect_device(self, data: dict = None) -> Response:
        """
        Disconnects the device.

        Args:
            data (dict, optional): Additional data to send in the request. Defaults to None.

        Returns:
            Response: The response from the server.
        """
        url = f"{self.base_url}/disconnect"
        headers = {"Content-Type": "application/json"}
        response = self.session.post(url, headers=headers, data=data, timeout=self.timeout)
        return response
    
    def get_random_connected_device(self) -> Dict[str, Any]:
        """
        Retrieves a random connected device from the list of devices.

        Returns:
            Dict[str, Any]: The details of a random connected device.
        """
        response = self.list_devices()
        assert response.status_code == 200
        device_list = response.json()

        device = random.choice(device_list)
        return device

    def connect_to_a_random_device(self) -> str:
        """
        Connects to a randomly selected device from the list of devices.

        Returns:
            str: The IP address of the connected device.
        """
        device = self.get_random_connected_device()
        device_ip = device.get("ip")
        response = self.connect_device(ip=device_ip)
        assert_response_success_status(response)

        return device_ip
    
    def get_specific_state(self, state_name: str = "brightness") -> Any:
        """
        Retrieves the specific state of the device.

        Args:
            state_name (str, optional): The name of the state to retrieve. Defaults to "brightness".

        Returns:
            Any: The value of the specified state.
        """
        response = self.get_device_state()
        assert response.status_code == 200

        device_states = response.json()
        state = device_states[state_name]

        return state
    
    def get_brightness_after_chilltime(self) -> float:
        """
        Executes the automation task and retrieves the brightness level.

        Returns:
            float: The brightness level after the automation task.
        """
        response = self.execute_automation_task()
        assert_response_success_status(response)

        brightness_level = self.get_specific_state('brightness')

        return brightness_level
