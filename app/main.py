from fastapi import FastAPI
from api import api_router
from auth import authenticate_user, get_current_user
from config import TARANTOOL_HOST, TARANTOOL_PORT

app = FastAPI()
app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    from connect import init_tarantool_connection
    init_tarantool_connection(TARANTOOL_HOST, TARANTOOL_PORT)

app.dependency_overrides = {
    authenticate_user: get_current_user,
}