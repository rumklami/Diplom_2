import requests

from data import Endpoints


class UserMethods:
    @staticmethod
    def register_user(register_list):
        email, password, name = register_list
        payload = {"email": email, "password": password, "name": name}
        new_user = requests.post(f'{Endpoints.REGISTRATION_USER}', json=payload)
        return new_user

    @staticmethod
    def login(login_list):
        email, password = login_list
        payload = {"email": email, "password": password}
        authorization = requests.post(f'{Endpoints.LOGIN_USER}', json=payload)
        return authorization

    @staticmethod
    def register_user_with_param(email=None, password=None, name=None):
        payload = {"email": email, "password": password, "name": name}
        new_user = requests.post(f'{Endpoints.REGISTRATION_USER}', json=payload)
        return new_user

    @staticmethod
    def delete_user(token):
        headers = {'Authorization': token}
        requests.delete(f'{Endpoints.DELETE_USER}', headers=headers)


class OrderMethods:
    @staticmethod
    def create_orders(order_list, token=""):
        payload = order_list
        headers = {'Authorization': token}
        new_order = requests.post(f'{Endpoints.CREATE_ORDERS}', json=payload, headers=headers)
        return new_order

    @staticmethod
    def get_ingredients():
        ingredients = requests.get(f'{Endpoints.INGREDIENTS}').json()
        list_ingredients = [item["_id"] for item in ingredients["data"]]
        return list_ingredients
