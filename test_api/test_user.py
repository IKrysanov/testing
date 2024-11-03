import allure


class TestUserPozitive:
    @allure.title("Проверка создания пользователя")
    def test_create_user(self, create_user):
        assert isinstance(create_user.json()["authToken"], str)

