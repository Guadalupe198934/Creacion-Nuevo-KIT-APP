from requests import Response

import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def auth_token_user():
    user_response= post_new_user(data.user_body)
    token_new= user_response.json()
    token=token_new['authToken']
    return token

def post_new_client_kit(kit_body):
    auth_token = auth_token_user()
    headers_with_auth= data.headers.copy()
    headers_with_auth["Authorization"]= f"Bearer{auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers_with_auth)
    return response