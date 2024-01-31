from data import *
from constants import ErrorMessage
import allure


@allure.story('Проверка создания курьера')
class TestCreateCourier:

    @allure.title('Курьер успешно создан')
    def test_successfully_create_courier(self):
        payload = {'login': create_login, 'password': create_password, 'firstName': create_first_name}
        response = requests.post(Url.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Не создается курьер без обязательного поля login')
    def test_creating_courier_not_login(self):
        payload = {'password': create_password, 'firstName': create_first_name}
        response = requests.post(Url.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 400 and response.text == ErrorMessage.ERROR_MESSAGE_400_1

    @allure.title('Не создается курьер с повторяющимися логинами и паролями')
    def test_cannot_create_two_identical_couriers(self, register_new_courier_and_return_login_password):
        payload = {"login": register_new_courier_and_return_login_password[0],
                   "password": register_new_courier_and_return_login_password[1],
                   "firstName": register_new_courier_and_return_login_password[2]}
        response = requests.post(Url.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 409 and response.text == ErrorMessage.ERROR_MESSAGE_409

