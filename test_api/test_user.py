import pytest
import allure
import requests
from http import HTTPMethod, HTTPStatus
from utils.client import Client
import time


@allure.title("Проверка создания пользователя")
def test_user(create_user):
    print(create_user.text)

