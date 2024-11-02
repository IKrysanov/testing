import pytest
import allure
import requests

@allure.title("Позитивный тест расчёта")
def test_main():
    response = requests.get("https://www.google.com")
    with allure.step("Один всегда равно одному"):
        assert 1 == 1

