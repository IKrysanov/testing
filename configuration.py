import os
from dotenv import load_dotenv

load_dotenv()


URL = os.getenv("URL_SERVICE")

# endpoints REST API
API_USERS = "/api/v1/users"

API_WAREHOUSES = "/api/v1/warehouses"