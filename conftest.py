import os
import pytest
import allure
from http import HTTPMethod
from configuration import URL, API_USERS
from http import HTTPStatus

from utils.client import Client



@allure.title("Создание пользователя")
@pytest.fixture(scope="session")
def create_user():
    response = Client.custom_requests(
            HTTPMethod.POST,
            f"{URL}{API_USERS}",
            expected_status_code=HTTPStatus.CREATED,
            json={
                "firstName": "Григорий",
                "email": "warmachine1996@mail.ru",
                "phone": "+74441237887",
                "comment": "Ребёнок спит, не шумите",
                "address": "г. Москва, ул. Хохотушкина, д. 16",
            },
            validator=False,
        )
    
    return response