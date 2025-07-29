import allure
import pytest

from api_methods import UserMethods
from data import CreateUserResponseAnswer, User


class TestRegisterUser:
    @allure.title('Регистрация уникального пользователя')
    def test_register_unique_user(self, user):
        with allure.step('Выполняется POST запрос "/api/auth/register" на регистрацию нового пользователя'):
            user_response = UserMethods.register_user(user)
        assert user_response.status_code == CreateUserResponseAnswer.SUCCESS[0] and CreateUserResponseAnswer.SUCCESS[
            1] in user_response.text, f'Пользователь {user} не является уникальным'

    @allure.title('Регистрация существующего пользователя')
    def test_register_exist_user(self, user):
        with allure.step('Выполняется POST запрос "/api/auth/register" на регистрацию нового пользователя'):
            UserMethods.register_user(user)
        with allure.step('Выполняется POST запрос "/api/auth/register" на регистрацию существующего пользователя'):
            user_response = UserMethods.register_user(user)
        assert user_response.status_code == CreateUserResponseAnswer.USER_EXIST[0] and \
               CreateUserResponseAnswer.USER_EXIST[
                   1] in user_response.text, f'При регистрации существующего пользователя {user} некорректный статус или текст ответа'

    @allure.title('Регистрация пользователя без заполнения одного обязательного поля')
    @pytest.mark.parametrize('email, password, name', User.USER_WITHOUT_FIELD)
    def test_register_user_without_required_field(self, email, password, name):
        with allure.step('Выполняется POST запрос "/api/auth/register" на регистрацию нового пользователя'):
            user_response = UserMethods.register_user_with_param(email=email, password=password, name=name)
        assert user_response.status_code == CreateUserResponseAnswer.FAILED[0] and CreateUserResponseAnswer.FAILED[
            1] in user_response.text, f'Внимание! Выполнена регистрация пользователя {[name, email]} без заполнения 1 обязательного поля'
