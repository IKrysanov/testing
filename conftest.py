import pytest
import allure
from http import HTTPMethod
from configuration import URL, API_USERS
from http import HTTPStatus
import data
from utils.client import Client


@allure.title("Создание пользователя")
@pytest.fixture(scope="session")
def create_user():
    response = Client.custom_requests(
        HTTPMethod.POST,
        f"{URL}{API_USERS}",
        expected_status_code=HTTPStatus.CREATED,
        json=data.user_body,
        validator=False,
    )

    data.headers["Authorization"] = f"Bearer {response.json()["authToken"]}"

    return response
