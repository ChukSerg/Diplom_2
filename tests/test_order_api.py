import allure

from api.api_order import ApiOrder
from api.api_user import ApiUser
from utils.constants import ApiConstants


class TestOrderApi:
    @allure.title('Проверка создания заказа без авторизации с ингрeдиентами')
    def test_create_order_ingredients_non_authorization(self):
        ingredients = ApiOrder.get_random_ingredients()
        response = ApiOrder.create_order(ingredients)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка создания заказа с авторизацией и ингрeдиентами')
    def test_create_order_ingredients_with_authorization(self, create_random_user):
        user = create_random_user
        ingredients = ApiOrder.get_random_ingredients()
        token = ApiUser.get_token(user[0], user[1])
        response = ApiOrder.create_order(ingredients, token)
        assert response.status_code == 200 and response.json()['order']['owner']['name'] == user[2]

    @allure.title('Проверка создания заказа без авторизации, без ингредиентов')
    def test_create_order_non_ingredients_non_authorization(self):
        ingredients = []
        response = ApiOrder.create_order(ingredients)
        assert (response.status_code == 400 and
                response.json()['message'] == ApiConstants.EMPTY_INGREDIENTS_MESSAGE)

    @allure.title('Проверка создания заказа с авторизацией, без ингрeдиентов')
    def test_create_order_ingredients_with_authorization(self, create_random_user):
        user = create_random_user
        ingredients = []
        token = ApiUser.get_token(user[0], user[1])
        response = ApiOrder.create_order(ingredients, token)
        assert (response.status_code == 400 and
                response.json()['message'] == ApiConstants.EMPTY_INGREDIENTS_MESSAGE)

    @allure.title('Проверка создания заказа с авторизацией, с неверным хэшем ингредиентов')
    def test_create_order_ingredients_with_authorization(self, create_random_user):
        user = create_random_user
        ingredients = ["61c0c5a71d1f82001bdaaa61", "61c0c5a71d1f82001bdaaa18"]
        token = ApiUser.get_token(user[0], user[1])
        response = ApiOrder.create_order(ingredients, token)
        assert (response.status_code == 400 and
                response.json()['message'] == ApiConstants.BAD_HASH_INGREDIENT_MESSAGE)

    @allure.title('Проверка получения списка заказов пользователя с авторизацией')
    def test_get_orders_with_authorization(self, create_random_user):
        user = create_random_user
        ingredients = ApiOrder.get_random_ingredients()
        token = ApiUser.get_token(user[0], user[1])
        ApiOrder.create_order(ingredients, token)
        ingredients2 = ApiOrder.get_random_ingredients()
        ApiOrder.create_order(ingredients2, token)
        response = ApiOrder.get_users_orders(token)
        assert response.status_code == 200 and len(response.json()['orders']) == 2

    @allure.title('Проверка получения списка заказов пользователя без авторизации')
    def test_get_orders_with_authorization(self, create_random_user):
        ingredients = ApiOrder.get_random_ingredients()
        ApiOrder.create_order(ingredients)
        response = ApiOrder.get_users_orders()
        assert (response.status_code == 401 and
                response.json()['message'] == ApiConstants.NON_AUTHORIZATION_MESSAGE)

