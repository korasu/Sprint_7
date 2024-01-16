import allure
import pytest

from helpers.generate_order_data import *
from data import OrderData, StatusCode
from request_generator.order_req import OrderReq


class TestCreateOrdering:
    @allure.title('Создание заказа на самокат')
    @allure.description('Проверка различных вариантов создания заказов по цветам скутеров')
    @pytest.mark.parametrize('color_data', OrderData.scooter_color)
    def test_create_success_ordering(self, color_data):
        order_data = generate_order_data()
        order_data["color"] = color_data
        order = OrderReq()
        response = order.create_order_request(order_data)

        assert response.status_code == StatusCode.create_status_code

    @allure.title('Создание заказа на самокат')
    @allure.description('Проверяем, что после заказа выдается track')
    def test_create_success_ordering_with_track_body(self):
        order_data = generate_order_data()
        order = OrderReq()
        response = order.create_order_request(order_data)
        r = response.json()

        assert len(str(r['track'])) > 0
