import allure
import requests
from constants import *


@allure.story('Проверка авторизации курьера')
class TestAuthorizationCourier:

    @allure.title('Тест успешной авторизации курьера')
    def test_true_courier_authorization(self, register_new_courier_and_return_login_password):
        payload = {"login": register_new_courier_and_return_login_password[0],
                   "password": register_new_courier_and_return_login_password[1]}
        response = requests.post(Url.URL_LOGIN_COURIER, data=payload)
        assert response.status_code == 200 and "id" in response.text

    @allure.title('Попытка авторизации без login')
    def test_authorization_not_login(self, register_new_courier_and_return_login_password):
        payload = {"password": register_new_courier_and_return_login_password[1]}
        response = requests.post(Url.URL_LOGIN_COURIER, data=payload)
        assert response.text == ErrorMessage.ERROR_MESSAGE_400_2

    @allure.title('Попытка авторизации без password')
    def test_authorization_not_password(self, register_new_courier_and_return_login_password):
        payload = {"login": register_new_courier_and_return_login_password[0],
                   "password": ''}
        response = requests.post(Url.URL_LOGIN_COURIER, data=payload)
        assert response.text == ErrorMessage.ERROR_MESSAGE_400_2

    @allure.title('Попытка авторизации если неправильно указать логин или пароль')
    def test_12123214124235(self):
        payload = {"login": "login", "password": 'password'}
        response = requests.post(Url.URL_LOGIN_COURIER, data=payload)
        assert response.text == ErrorMessage.ERROR_MESSAGE_404



