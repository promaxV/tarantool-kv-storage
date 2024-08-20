from typing import Dict, Any
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    token: str

class WriteRequest(BaseModel):
    data: Dict[str, Any]

class WriteResponse(BaseModel):
    status: str

class ReadRequest(BaseModel):
    keys: list[str]

class ReadResponse(BaseModel):
    data: Dict[str, Any]