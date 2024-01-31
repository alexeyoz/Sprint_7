import allure
import data


@allure.story('Проверка получения списка заказов')
class TestOrderList:

    @allure.title('Тест получения списка заказов')
    def test_order_list(self):
        response = data.get_order_list()
        assert "orders" in response
