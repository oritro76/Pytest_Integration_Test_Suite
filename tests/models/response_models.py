from pydantic import BaseModel, Field, RootModel
from typing import List, Optional

class Device(BaseModel):
    """
    Represents a device with a name and IP address.

    Attributes:
        name (str): The name of the device.
        ip (str): The IP address of the device.
    """
    name: str
    ip: str

class ConnectResponse(BaseModel):
    """
    Represents the response for a connect operation.

    Attributes:
        success (bool): Indicates whether the connect operation was successful.
    """
    success: bool

class StateResponse(BaseModel):
    """
    Represents the state response of a device.

    Attributes:
        name (str): The name of the device.
        ip (str): The IP address of the device.
        color (str): The color setting of the device.
        brightness (float): The brightness level of the device.
    """
    name: str
    ip: str
    color: str
    brightness: float

class GenericIsSuccessResponse(BaseModel):
    """
    Represents a generic response indicating success status.

    Attributes:
        success (bool): Indicates whether the operation was successful.
    """
    success: bool

class DevicesResponse(RootModel):
    """
    Represents a response containing a list of devices.

    Attributes:
        root (List[Device]): A list of devices.
    """
    root: List[Device]

class ChillTimeResponse(BaseModel):
    """
    Represents the response for a chill time operation.

    Attributes:
        success (bool): Indicates whether the chill time operation was successful.
    """
    success: bool
