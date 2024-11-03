import os
from dotenv import load_dotenv

load_dotenv()


URL = os.getenv("URL_SERVICE")

API_USERS = "/api/v1/users"