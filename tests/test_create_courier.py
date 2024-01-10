import allure
import pytest

from helpers.generate_courier_data import *
from helpers.remove_added_courier import *
from request_generator.courier_req import CourierReq
from data import Data


class TestCreateCourier:
    @allure.title('Успешное создание курьера')
    @allure.description('Проверяем, что курьер создан успешно')
    def test_successful_courier_created(self):
        courier_data = generate_courier_data()

        c = CourierReq()
        response = c.courier_create(courier_data)

        assert response.status_code == Data.create_status_code and response.text == Data.create_courier_success

        delete_created_courier(courier_data)

    @allure.title('Успешное создание курьера')
    @allure.description('Проверяем, что курьер создан успешно возвращается верный код ответа 201')
    def test_successful_courier_created_with_correct_status_code(self):
        courier_data = generate_courier_data()

        c = CourierReq()
        response = c.courier_create(courier_data)

        assert response.status_code == Data.create_status_code

        delete_created_courier(courier_data)

    @allure.title('Успешное создание курьера')
    @allure.description('Проверяем, что курьер создан успешно, возвращается верный тело ответа')
    def test_successful_courier_created_with_correct_response_body(self):
        courier_data = generate_courier_data()

        c = CourierReq()
        response = c.courier_create(courier_data)

        assert response.text == Data.create_courier_success

        delete_created_courier(courier_data)

    @allure.title('Успешное создание курьера только с обязательными данными')
    @allure.description('Проверяем, что курьер создан успешно только с обязательными данными')
    def test_successful_courier_created_only_with_required_fields(self):
        courier_data = generate_courier_data()

        c = CourierReq()
        response = c.courier_create({"login": courier_data['login'], "password": courier_data['password']})

        assert response.status_code == Data.create_status_code and response.text == Data.create_courier_success

        delete_created_courier(courier_data)

    @allure.title('Попытка создания курьера не со всеми обязательными параметрами')
    @allure.description('Проверяем, что курьер не создается без обязательных параметров')
    @pytest.mark.parametrize('courier_data', [{"login": generate_courier_data()['login']},
                                              {"password": generate_courier_data()['password']}])
    def test_created_courier_without_all_required_fields(self, courier_data):
        c = CourierReq()
        response = c.courier_create(courier_data)
        r = response.json()

        assert response.status_code == Data.bad_request_status_code and Data.create_courier_without_data == r["message"]

    @allure.title('Попытка создания курьера с уже существующем логином')
    @allure.description('Проверяем, что курьер не создается при вводе существующего логина')
    def test_created_courier_with_repeated_login(self, register_new_courier_and_return_login_password):
        courier_data = generate_courier_data()

        c = CourierReq()
        response = c.courier_create({"login": register_new_courier_and_return_login_password['login'], "password": courier_data['password']})
        r = response.json()

        assert response.status_code == Data.conflict_status_code and Data.create_courier_with_repeated_data == r["message"]

        delete_created_courier(register_new_courier_and_return_login_password)

    @allure.title('Попытка создания курьера уже существующего в системе')
    @allure.description('Проверяем, что курьер не создается при вводе существующего логина')
    def test_created_courier_twice(self, register_new_courier_and_return_login_password):
        c = CourierReq()
        response = c.courier_create(register_new_courier_and_return_login_password)
        r = response.json()

        assert response.status_code == Data.conflict_status_code and Data.create_courier_with_repeated_data == r["message"]

        delete_created_courier(register_new_courier_and_return_login_password)
