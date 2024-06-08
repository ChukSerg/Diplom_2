import allure
import requests
import random
import string

from utils.constants import ApiConstants


def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    name = generate_random_string(6)
    email = generate_random_string(6) + '@yandex.ru'
    password = generate_random_string(6)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(ApiConstants.REGISTRATION_USER_URL, data=payload)

    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)

    return login_pass
