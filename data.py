from constants import *

import requests
import json


def create_login():
    login = Faker().first_name()
    return login


def create_password():
    password = Faker().password()
    return password


def create_first_name():
    first_name = Faker().first_name()
    return first_name


def get_order_list():
    response = requests.get(Url.URL_ORDER_LIST)
    return response.json()


def create_order(color):
    InformationForOrder.info_for_order["color"] = color
    payload = InformationForOrder.info_for_order
    response = requests.post(Url.URL_ORDER_LIST, data=json.dumps(payload))
    return response.json()
#
# def delite_courier(id_courier):
#     response = requests.delete(f"{Url.DELITE_COURIER}{id_courier}")
#     return response.json()