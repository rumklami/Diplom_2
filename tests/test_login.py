import allure

from api_methods import UserMethods
from data import LoginResponseAnswer


class TestLogin:
    @allure.title('Авторизация под существующим пользователем')
    def test_login_success(self, login_user):
        authorization = UserMethods.login((login_user[0], login_user[1]))
        assert authorization.status_code == LoginResponseAnswer.SUCCESS[0] and LoginResponseAnswer.SUCCESS[
            1] in authorization.text, f'Авторизация пользователя {login_user[0], login_user[1]} не выполнена'

    @allure.title('Авторизация с неверным логином или паролем')
    def test_login_incorrect_field(self, login_user):
        email, password = (login_user[0], login_user[1])
        login_user = email + 'jj', password
        authorization = UserMethods.login(login_user)
        assert authorization.status_code == LoginResponseAnswer.UNAUTHORIZED[0] and LoginResponseAnswer.UNAUTHORIZED[
            1] in authorization.text, f'Авторизация пользователя {login_user} прошла успешно с некорректным логином или паролем'
