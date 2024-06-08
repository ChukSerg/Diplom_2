import allure
import pytest

from api.api_user import ApiUser
from utils.constants import ApiConstants


class TestUserApi:
    @allure.title('Проверка создания пользователя со всеми данными')
    def test_create_user_correct_data(self, create_static_user):
        user = create_static_user
        response = ApiUser.create_user(*user)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка повторной регистрации пользователя')
    def test_negative_creation_two_same_users(self, create_random_user):
        user = create_random_user
        response = ApiUser.create_user(user[0], user[1], user[2])
        assert (response.status_code == 403 and
                response.json()['message'] == ApiConstants.CREATE_TWO_SAME_MESSAGE)

    @allure.title('Проверка регистрации пользователя без одного из обязательных полей')
    @pytest.mark.parametrize('email, password, name', [
        (ApiConstants.STATIC_USER[0], ApiConstants.STATIC_USER[1], ''),
        (ApiConstants.STATIC_USER[0], '', ApiConstants.STATIC_USER[2]),
        ('', ApiConstants.STATIC_USER[1], ApiConstants.STATIC_USER[2]),
    ])
    def test_negative_creation_user_without_one_required_field(self, email, password, name):
        response = ApiUser.create_user(email, password, name)
        assert (response.status_code == 403 and
                response.json()['message'] == ApiConstants.CREATE_WITHOUT_FIELD_MESSAGE)

    @allure.title('Проверка успешного входа')
    def test_correct_login_success(self, create_random_user):
        user = create_random_user
        response = ApiUser.login_user(user[0], user[1])
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка входа с неверным email')
    def test_wrong_login_with_bad_email(self, create_random_user):
        user = create_random_user
        response = ApiUser.login_user('bad_email@yandex.ru', user[1])
        assert (response.status_code == 401 and
                response.json()['message'] == ApiConstants.BAD_VALUE_FIELD_MESSAGE)

    @allure.title('Проверка входа с неверным паролем')
    def test_wrong_login_with_bad_password(self, create_random_user):
        user = create_random_user
        response = ApiUser.login_user(user[0], 'bad_password', )
        assert (response.status_code == 401 and
                response.json()['message'] == ApiConstants.BAD_VALUE_FIELD_MESSAGE)

    @allure.title('Проверка изменения данных авторизованного пользователя')
    @pytest.mark.parametrize('data, value', [
        [0, 'new_email_static_abc123456@yandex.ru'],
        [1, 'new_password_static_abc123456'],
        [2, 'PeterPen']
    ])
    def test_modify_email_authorization_user_success(self, create_random_user, data, value):
        user = create_random_user
        token = ApiUser.get_token(user[0], user[1])
        user[data] = value
        response = ApiUser.modify_user_data(user[0], user[1], user[2], token)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка изменения email без авторизации')
    def test_modify_email_non_authorization_user_error(self, create_random_user):
        user = create_random_user
        token = ''
        new_email = 'new_email_static_abc123456@yandex.ru'
        response = ApiUser.modify_user_data(new_email, user[1], user[2], token)
        assert response.status_code == 401 and response.json()['success'] is False

    @allure.title('Проверка изменения password без авторизации')
    def test_modify_email_non_authorization_user_error(self, create_random_user):
        user = create_random_user
        token = ''
        new_password = 'new_password_static_abc123'
        response = ApiUser.modify_user_data(user[0], new_password, user[2], token)
        assert response.status_code == 401 and response.json()['success'] is False

    @allure.title('Проверка изменения password без авторизации')
    def test_modify_email_non_authorization_user_error(self, create_random_user):
        user = create_random_user
        token = ''
        new_name = 'PeterPen'
        response = ApiUser.modify_user_data(user[0], user[1], new_name, token)
        assert response.status_code == 401 and response.json()['success'] is False
