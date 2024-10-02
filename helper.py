import string
import random
from api_data import ApiData


class Helper:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def create_random_registration_body():
        body = ApiData.BODY_USER_REGISTRATION.copy()
        random_name = Helper.generate_random_string(8)
        body['email'] = f'{random_name}.@example.com'
        body['name'] = random_name

        return body
