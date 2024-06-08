import allure
import requests

from utils.constants import ApiConstants


class ApiUser:
    @staticmethod
    @allure.step('Создать пользователя')
    def create_user(email, password, name):
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        return requests.post(ApiConstants.REGISTRATION_USER_URL, data=payload)

    @staticmethod
    @allure.step('Удалить пользователя')
    def delete_user(token):
        headers = {"Authorization": token}
        response = requests.delete(ApiConstants.USER_URL, headers=headers)
        return response

    @staticmethod
    @allure.step('Войти пользователем')
    def login_user(email, password):
        payload = {
            'email': email,
            'password': password
        }
        response = requests.post(ApiConstants.USER_LOGIN_URL, data=payload)
        return response

    @staticmethod
    @allure.step('Изменить данные пользователя')
    def modify_user_data(email, password, name, token):
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        headers = {'Authorization': token}
        response = requests.patch(ApiConstants.USER_URL, data=payload, headers=headers)
        return response

    @staticmethod
    @allure.step('Получение пользовательского токена')
    def get_token(email, password):
        response = ApiUser.login_user(email, password)
        token = response.json()['accessToken']
        return token
