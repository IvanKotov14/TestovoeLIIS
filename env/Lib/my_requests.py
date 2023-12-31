import requests
from Lib.logger import Logger
import allure
from environment import ENV_OBJECT


class MyRequests:
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None, json: dict = None, auth=None):
        with allure.step(f"POST request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, json, auth, 'POST')

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None, json: dict = None, auth: dict = None):
        with allure.step(f"GET request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, json, auth, 'GET')

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None, json: dict = None, auth: dict = None):
        with allure.step(f"PUT request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, json, auth, 'PUT')

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None, json: dict = None, auth: dict = None):
        with allure.step(f"DELETE request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, json, auth, 'DELETE')

    @staticmethod
    def patch(url: str, data: dict = None, headers: dict = None, cookies: dict = None, json: dict = None, auth: dict = None):
        with allure.step(f"PATCH request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, json, auth, 'PATCH')

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, json: dict, auth: dict, method: str):
        url = f"{ENV_OBJECT.get_base_url()}{url}"
        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}
        if json is None:
            json = {}
        if auth is None:
            json = {}

        Logger.add_request(url, data, headers, cookies, method)

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies, json=json, auth=auth)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, cookies=cookies, json=json, auth=auth)
        elif method == 'PUT':
            response = requests.put(url, params=data, headers=headers, cookies=cookies, json=json, auth=auth)
        elif method == 'DELETE':
            response = requests.delete(url, params=data, headers=headers, cookies=cookies, json=json, auth=auth)
        elif method == 'PATCH':
            response = requests.patch(url, params=data, headers=headers, cookies=cookies, json=json, auth=auth)
        else:
            raise Exception(f"Не верный HTTP метод '{method}' был получен")

        Logger.add_response(response)

        return response
