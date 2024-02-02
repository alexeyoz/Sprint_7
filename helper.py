import allure

from constants import *

import requests
import json


@allure.step('Создаем Login')
def create_login():
    login = Faker().first_name()
    return login


@allure.step('Создаем Password')
def create_password():
    password = Faker().password()
    return password


@allure.step('Создаем Имя')
def create_first_name():
    first_name = Faker().first_name()
    return first_name


@allure.step('Получаем список заказов')
def get_order_list():
    response = requests.get(Url.URL_ORDER_LIST)
    return response.json()


@allure.step('Создаем заказ')
def create_order(color):
    InformationForOrder.info_for_order["color"] = color
    payload = InformationForOrder.info_for_order
    response = requests.post(Url.URL_ORDER_LIST, data=json.dumps(payload))
    return response.json()
