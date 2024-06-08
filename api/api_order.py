import allure
import requests
from random import choice

from utils.constants import ApiConstants


class ApiOrder:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(ingredients, token=''):
        payload = {'ingredients': ingredients}
        headers = {'Authorization': token}
        response = requests.post(ApiConstants.ORDER_URL, data=payload, headers=headers)
        return response

    @staticmethod
    @allure.step('Получение списка ингредиентов')
    def get_random_ingredients():
        response = requests.get(ApiConstants.INGREDIENTS_URL)
        ingredients = []
        for i in response.json()['data']:
            ingredients.append(i['_id'])
        random_ingredients = []
        for i in range(3):
            random_ingredients.append(choice(ingredients))
        return random_ingredients

    @staticmethod
    @allure.step('Получение списка заказов пользователя')
    def get_users_orders(token=''):
        headers = {'Authorization': token}
        response = requests.get(ApiConstants.ORDER_URL, headers=headers)
        return response


