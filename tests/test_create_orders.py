import allure
import pytest

from api_methods import OrderMethods
from data import CreateOrdersResponseAnswer
from helper import generate_order, generate_ingredient


class TestCreateOrders:
    @allure.title('Создание заказа с авторизацией с ингридиентами и без')
    @pytest.mark.parametrize("ingredient, expect", ([generate_ingredient(), CreateOrdersResponseAnswer.SUCCESS],
                                                    [("", ""), CreateOrdersResponseAnswer.BAD_REQUEST]))
    def test_create_order_authorized(self, login_user, ingredient, expect):
        with allure.step('Выполняется POST запрос "/api/orders" на создание заказа'):
            order = OrderMethods.create_orders(generate_order(ingredient), login_user[2])
        assert order.status_code == expect[0] and expect[1] in order.text

    @allure.title('Создание заказа без авторизаци с ингридиентами и без')
    @pytest.mark.parametrize("ingredient, expect", ([generate_ingredient(), CreateOrdersResponseAnswer.SUCCESS],
                                                    [("", ""), CreateOrdersResponseAnswer.BAD_REQUEST]))
    def test_create_order_unauthorized(self, ingredient, expect):
        with allure.step('Выполняется POST запрос "/api/orders" на создание заказа'):
            order = OrderMethods.create_orders(generate_order(ingredient))
        assert order.status_code == expect[0] and expect[1] in order.text

    @allure.title('Создание заказа с неверным хешем ингридиентов')
    def test_create_order_invalid_hash(self, login_user):
        with allure.step('Выполняется POST запрос "/api/orders" на создание заказа'):
            order = OrderMethods.create_orders(generate_order(generate_ingredient() + '3f'), login_user[2])
        assert order.status_code == CreateOrdersResponseAnswer.HASH_INCORRECT[0] and \
               CreateOrdersResponseAnswer.HASH_INCORRECT[1] in order.text
