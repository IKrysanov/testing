import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL_SERVICE")

# endpoints REST API
API_USERS = "/api/v1/users"

API_WAREHOUSES = "/api/v1/warehouses"

API_WAREHOUSES_CHECK = "/api/v1/warehouses/check"
API_WAREHOUSES_AMOUNT = "/api/v1/warehouses/amount"