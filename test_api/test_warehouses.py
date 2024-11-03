from utils.client import Client
import allure
from http import HTTPMethod, HTTPStatus
import data
from configuration import URL, API_WAREHOUSES
from schemas.warehouses import schema_warehouses


class TestWarehousesPositive:
    @allure.title("Проверка получения списка складов")
    def test_get_warehouses(self, create_user):
        Client.custom_requests(
            HTTPMethod.GET,
            f"{URL}{API_WAREHOUSES}",
            headers=data.headers,
            schema=schema_warehouses,
            expected_status_code=HTTPStatus.OK,
        )
