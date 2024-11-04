import requests
from requests import Response
import logging
from jsonschema import validate
import allure
from http import HTTPStatus
from configuration import URL

from typing import Optional

logger = logging.getLogger("api")


class Client:
    @staticmethod
    @allure.step("Запрос {method} {url}")
    def custom_requests(method: str,
                        url: str,
                        url_service: str = URL,
                        schema: Optional[dict] = None,
                        expected_status_code: bool = HTTPStatus.OK,
                        validator: bool = True,
                        **kwargs) -> Response:
        """
        Request method
        method: метод для нового запроса: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
        url: endpoint API RESTful
        url_service: ссылка на экземпляр веб-приложяения(Default value: URL)
        schema: JSON schema для валидации типов данных
        expected_status_code: ожидаемый статус код в теле ответа(Default value - 200 OK)
        validator: переключатель для валидации типов данных(Default value: True). True - валидация типов данных включена,
        False - валидация для запроса будет отключена.
        **kwargs:
            params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request.
        """

        # Запрос на сервер
        response = requests.request(method, f"{url_service}{url}", **kwargs)
        # Проверка статус кода
        with allure.step(f"Ожидаемый статус код - {expected_status_code}"):
            assert response.status_code == expected_status_code
        # Логирование
        logger.info(response.status_code)
        logger.info(response.text)
        # Валидация типов данных
        if validator:
            with allure.step("Валидация типов данных"):
                validate(instance=response.json(), schema=schema)
        return response
