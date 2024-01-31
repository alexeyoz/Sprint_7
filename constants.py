from faker import Faker


class ErrorMessage:  # сообщения об ошибках
    ERROR_MESSAGE_409 = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    ERROR_MESSAGE_400_1 = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    ERROR_MESSAGE_400_2 = '{"code":400,"message":"Недостаточно данных для входа"}'
    ERROR_MESSAGE_404 = '{"code":404,"message":"Учетная запись не найдена"}'


class InformationForOrder:  # данные для заказа
    info_for_order = {
        "firstName": Faker().first_name(),
        "lastName": Faker().last_name(),
        "address": Faker().address(),
        "metroStation": int(Faker().random_number(2)),
        "phone": Faker().phone_number(),
        "rentTime": int(Faker().random_number(2)),
        "deliveryDate": Faker().date(),
        "comment": Faker().text(),
        "color": []
    }


class Url:  # url
    URL_BASE = 'http://qa-scooter.praktikum-services.ru'

    URL_LOGIN_COURIER = URL_BASE + '/api/v1/courier/login'
    URL_CREATE_COURIER = URL_BASE + '/api/v1/courier'
    URL_ORDER_LIST = URL_BASE + '/api/v1/orders'
    URL_DELETE_COURIER = URL_BASE + '/api/v1/courier/:id'

COLORS = ['[]', '["BLACK"]', '["GREY"]', '["BLACK", "GREY"]']



#    URL_ORDER_FINISH = URL_BASE + '/api/v1/orders/finish/:id'
#    URL_ORDER_CANCEL = URL_BASE + '/api/v1/orders/cancel'
#    URL_GET_ORDER_BY_NUMBER = URL_BASE + '/api/v1/orders/track'
#    URL_ACCEPT_ = URL_BASE + '/api/v1/orders/accept/:id'
#    URL_CREATE_ORDER = URL_BASE + '/api/v1/orders'
#    URL_DELETE_COURIER = URL_BASE + '/api/v1/courier/:id'  #
#    URL_GET_QUANTITY_ORDER = URL_BASE + '/api/v1/courier/:id/ordersCount'
