import pytest

from utils.constants import ApiConstants

from api.api_user import ApiUser
from utils.helpers import register_new_courier_and_return_login_password


@pytest.fixture(scope='function')
def create_random_user():
    login_pass = register_new_courier_and_return_login_password()
    yield login_pass
    response = ApiUser.login_user(login_pass[0], login_pass[1])
    token = response.json()['accessToken']
    ApiUser.delete_user(token)


@pytest.fixture(scope='function')
def create_static_user():
    login_pass = ApiConstants.STATIC_USER
    yield login_pass
    response = ApiUser.login_user(login_pass[0], login_pass[1])
    token = response.json()['accessToken']
    ApiUser.delete_user(token)
