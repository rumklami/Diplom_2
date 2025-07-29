import allure
import pytest

from api_methods import UserMethods
from helper import generate_user


@pytest.fixture
def login_user():
    email, password, name = generate_user()
    with allure.step('Выполняется POST запрос "/api/auth/register" на регистрацию нового пользователя'):
        new_user = UserMethods.register_user((email, password, name)).json()
    user_token = new_user["accessToken"]
    yield email, password, user_token
    with allure.step('Выполняется DELETE запрос "/api/auth/user" на удаление пользователя'):
        UserMethods.delete_user(user_token)

@pytest.fixture
def user():
    return generate_user()
