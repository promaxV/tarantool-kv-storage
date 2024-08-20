import os

SECRET_KEY = "enter_your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

TARANTOOL_HOST = os.environ.get("TARANTOOL_HOST", "tarantool")
TARANTOOL_PORT = int(os.environ.get("TARANTOOL_PORT", "3301"))

DEFAULT_USERNAME = os.environ.get("DEFAULT_USERNAME", "admin")
DEFAULT_PASSWORD = os.environ.get("DEFAULT_PASSWORD", "presale")