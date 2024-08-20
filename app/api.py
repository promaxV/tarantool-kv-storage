from fastapi import APIRouter, Depends, HTTPException
from models import LoginRequest, LoginResponse, WriteRequest, WriteResponse, ReadRequest, ReadResponse
from connect import write_data, read_data
from auth import authenticate_user, create_access_token, get_current_user

api_router = APIRouter()

@api_router.post("/api/login", response_model=LoginResponse)
async def login(login_request: LoginRequest):
    user = await authenticate_user(login_request.username, login_request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token = create_access_token(data={"user_id": user["user_id"]})
    return LoginResponse(token=access_token)

@api_router.post("/api/write", response_model=WriteResponse)
async def write(write_request: WriteRequest, user_id: int = Depends(get_current_user)):
    await write_data(write_request.data)
    return WriteResponse(status="success")

@api_router.post("/api/read", response_model=ReadResponse)
async def read(read_request: ReadRequest, user_id: int = Depends(get_current_user)):
    data = await read_data(read_request.keys)
    return ReadResponse(data=data)