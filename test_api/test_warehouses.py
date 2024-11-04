from utils.client import Client
import allure
from http import HTTPMethod, HTTPStatus
import data
from configuration import API_WAREHOUSES, API_WAREHOUSES_CHECK
from schemas.warehouses import schema_warehouses


class TestWarehousesPositive:
    @allure.title("Проверка получения списка складов")
    def test_get_warehouses(self, create_user):
        Client.custom_requests(
            HTTPMethod.GET,
            API_WAREHOUSES, # /api/v1/warehouses
            headers=data.headers,
            schema=schema_warehouses,
            expected_status_code=HTTPStatus.OK,
        )

    @allure.title("Проверка продукта на складе")
    def test_post_warehouses_check(self, create_user):
        Client.custom_requests(
            HTTPMethod.POST,
            API_WAREHOUSES_CHECK, # /api/v1/warehouses/check
            headers=data.headers,
            json=data.products_body,
            validator=False
        )

    @allure.title("Проверка продукта на складе")
    def test_post_warehouses_amount(self, create_user):
        Client.custom_requests(
            HTTPMethod.POST,
            API_WAREHOUSES_CHECK, # /api/v1/warehouses/amount
            headers=data.headers,
            json=data.amount_body,
            validator=False
        )