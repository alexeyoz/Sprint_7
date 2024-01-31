Sprint_7
Тестирование Яндекс самокат
Основа для написания авто тестов — фреймворк pytest.
Установить зависимости — pip install -r requirements.txt.
Команда для запуска — pytest -v.
Команда для формирования отчетов Allure — allure serve allure_results

test_authorization_courier.py

test_true_courier_authorization - проверка авторизации курьера
test_authorization_not_login - Попытка авторизации без login
test_authorization_not_password - Попытка авторизации без password
test_courier_authorization_incorrect - Попытка авторизации с неверными данными

test_create_courier.py

test_successfully_create_courier - Курьер успешно создан
test_creating_courier_not_login - Не создается курьер без обязательного поля login
test_cannot_create_two_identical_couriers - Не создается курьер с повторяющимися логинами и паролями

test_create_order.py

test_successful_order_creation_with_color - Тест вариантов заказа: один цвет, два цвета, не указан цвет

test_get_order_list.py

test_order_list - Тест получения списка заказов

conftest.py

register_new_courier_and_return_login_password - метод создания курьера

constants.py

ErrorMessage - возможные ошибки
InformationForOrder - данные для заказа рандомные
Url - используемые ссылки
COLORS - цвета в заказ

data.py

create_login - метод создания login
create_password - метод создания password
create_first_name - метод создания first_name
get_order_list - метод создания password
create_order - метод создания заказа