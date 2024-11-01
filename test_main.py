import pytest
import allure 

@allure.title("Позитивный тест расчёта")
def test_main():
    with allure.step("Один всегда равно одному"):
        assert 1 == 1