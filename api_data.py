class ApiData:
    URL = 'https://stellarburgers.nomoreparties.site/'
    USER_REGISTRATION_API = 'api/auth/register'
    BODY_USER_REGISTRATION = {
        "email": "test-data@yandex.ru",
        "password": "password",
        "name": "Username"
    }
    USER_API = 'api/auth/user'
    OREDER_API = 'api/orders'
    DODY_CREATE_ORDER = {"ingredients": ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6d"]}