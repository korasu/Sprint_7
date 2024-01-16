import allure
from request_generator.order_req import OrderReq
from data import StatusCode


class TestOrderList:
    @allure.title("Получение списка заказов")
    @allure.description("Получение всего списка заказов")
    def test_taken_order_list(self):
        order = OrderReq()
        response = order.order_list_request()
        r = response.json()

        assert response.status_code == StatusCode.success_status_code and r["orders"] != []
