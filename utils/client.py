import requests
from requests import Response
import logging
from jsonschema import validate
import allure
from http import HTTPStatus

from typing import Optional

logger = logging.getLogger("api")


class Client:
    @staticmethod
    @allure.step("Запрос {method} {url}")
    def custom_requests(method: str, 
                        url: str,
                        schema: Optional[dict] = None,
                        expected_status_code: bool = HTTPStatus.OK,
                        validator: bool = True,
                        **kwargs) -> Response:
        """
        Request method
        method: method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
        url – URL for the new Request object.
        **kwargs:
            params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request.
        """

        response = requests.request(method, url, **kwargs)
        with allure.step(f"Ожидаемый статус код - {expected_status_code}"):
            assert response.status_code == expected_status_code
        logger.info(response.status_code)
        logger.info(response.text)
        if validator:
            with allure.step("Валидация типов данных"):
                validate(instance=response.json(), schema=schema)
        return response
