import allure
import data
import pytest


@allure.story('Проверка создания заказа')
class TestCreatingOrder:

    @allure.title('Тест вариантов: один цвет, два цвета, не указан цвет')
    @pytest.mark.parametrize('color', data.COLORS)
    def test_successful_order_creation_with_color(self, color):
        response = data.create_order(color)
        assert "track" in response
