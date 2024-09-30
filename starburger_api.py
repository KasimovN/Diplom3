import requests

from api_data import ApiData

class StarburgerApi:
    @staticmethod
    def user_registration(body):
        registration_response = requests.post(ApiData.URL + ApiData.USER_REGISTRATION_API, json=body)
        return registration_response

    @staticmethod
    def delete_user(accesstoken):
        delete_response = requests.delete(ApiData.URL + ApiData.USER_API, headers={'Authorization': accesstoken})
        return delete_response

    @staticmethod
    def create_order(accesstoken, body):
        order_response = requests.post(ApiData.URL + ApiData.OREDER_API, json=body,
                                       headers={'Authorization': accesstoken})
        return order_response