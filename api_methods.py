import requests

from data import Url


class UserMethods:
    @staticmethod
    def register_user(register_list):
        email, password, name = register_list
        payload = {"email": email, "password": password, "name": name}
        new_user = requests.post(f'{Url.BASE_PAGE}{Url.REGISTRATION_USER}', json=payload)
        return new_user

    @staticmethod
    def login(login_list):
        email, password = login_list
        payload = {"email": email, "password": password}
        authorization = requests.post(f'{Url.BASE_PAGE}{Url.LOGIN_USER}', json=payload)
        return authorization

    @staticmethod
    def register_user_with_param(email=None, password=None, name=None):
        payload = {"email": email, "password": password, "name": name}
        new_user = requests.post(f'{Url.BASE_PAGE}{Url.REGISTRATION_USER}', json=payload)
        return new_user

    @staticmethod
    def delete_user(token):
        headers = {'Authorization': token}
        requests.delete(f'{Url.BASE_PAGE}{Url.DELETE_USER}', headers=headers)


class OrderMethods:
    @staticmethod
    def create_orders(order_list, token=""):
        payload = order_list
        headers = {'Authorization': token}
        new_order = requests.post(f'{Url.BASE_PAGE}{Url.CREATE_ORDERS}', json=payload, headers=headers)
        return new_order

    @staticmethod
    def get_ingredients():
        ingredients = requests.get(f'{Url.BASE_PAGE}{Url.INGREDIENTS}').json()
        list_ingredients = [item["_id"] for item in ingredients["data"]]
        return list_ingredients
