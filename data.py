class Url:
    BASE_PAGE = 'https://stellarburgers.nomoreparties.site'
    CREATE_ORDERS = '/api/orders'
    REGISTRATION_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    DELETE_USER = '/api/auth/user'
    INGREDIENTS = '/api/ingredients'


class CreateUserResponseAnswer:
    SUCCESS = [200, "user"]
    FAILED = [403, "Email, password and name are required fields"]
    USER_EXIST = [403, "User already exists"]


class LoginResponseAnswer:
    SUCCESS = [200, '"accessToken":"Bearer']
    UNAUTHORIZED = [401, '"email or password are incorrect"']


class CreateOrdersResponseAnswer:
    SUCCESS = [200, '"order"']
    BAD_REQUEST = [400, '"message": "Ingredient ids must be provided"']
    HASH_INCORRECT = [500, 'Internal Server Error']


class DeleteUserResponseAnswer:
    SUCCESS = [200, '']


class User:
    USER_WITHOUT_FIELD = (
        ['Robert Johnston MD', 'hp18m_Gk)M', None], ['Robert Johnston MD', None, 'Levi'], [None, 'hp18m_Gk)M', 'Levi'])
    DATA_LOGIN = ['Robert', 'hp18m_Gk)M']


class Ingredients:
    LIST_INGREDIENTS = ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa70',
                        '61c0c5a71d1f82001bdaaa71', '61c0c5a71d1f82001bdaaa72', '61c0c5a71d1f82001bdaaa6e',
                        '61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa6c',
                        '61c0c5a71d1f82001bdaaa75', '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa77',
                        '61c0c5a71d1f82001bdaaa78', '61c0c5a71d1f82001bdaaa79', '61c0c5a71d1f82001bdaaa7a']
