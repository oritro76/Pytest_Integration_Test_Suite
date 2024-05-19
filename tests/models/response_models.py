from pydantic import BaseModel, Field, RootModel
from typing import List, Optional

class Device(BaseModel):
    name: str
    ip: str

class ConnectResponse(BaseModel):
    success: bool

class StateResponse(BaseModel):
    name: str
    ip: str
    color: str
    brightness: float

class GenericIsSuccessResponse(BaseModel):
    success: bool

class DevicesResponse(RootModel):
    root: List[Device]

class ChillTimeResponse(BaseModel):
    success: bool