import pytest

from api_methods import UserMethods
from helper import generate_user


@pytest.fixture
def login_user():
    email, password, name = generate_user()
    new_user = UserMethods.register_user((email, password, name)).json()
    user_token = new_user["accessToken"]
    yield email, password, user_token
    UserMethods.delete_user(user_token)
