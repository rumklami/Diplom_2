import random

from faker import Faker

from data import Ingredients

faker = Faker()


def generate_user():
    email = f"{faker.email()}"
    password = f"{faker.password()}"
    name = f"{faker.first_name()}"
    return email, password, name


def generate_ingredient():
    return random.choice(Ingredients.LIST_INGREDIENTS)


def generate_order(ingredient1=generate_ingredient(), ingredient2=generate_ingredient()):
    return {
        "ingredients": [f"{ingredient1}", f"{ingredient2}"]
    }
