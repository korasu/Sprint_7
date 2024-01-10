import random

import allure

from helpers.remove_added_courier import *
from request_generator.courier_req import CourierReq
from data import Data


class TestLoginCourier:
    @allure.title('Успешная авторизация на портале')
    @allure.description('Провести успешную авторизацию на портале')
    def test_successful_courier_login(self, register_new_courier_and_return_login_password):
        requests = CourierReq()
        response = requests.courier_login(register_new_courier_and_return_login_password)

        assert response.status_code == Data.success_status_code

        delete_created_courier(register_new_courier_and_return_login_password)

    @allure.title('Успешная авторизация на портале')
    @allure.description('Провести успешную авторизацию на портале со всеми необходимыми параметрами')
    def test_successful_courier_login_with_required_fields(self, register_new_courier_and_return_login_password):
        requests = CourierReq()
        response = requests.courier_login({"login": register_new_courier_and_return_login_password['login'],
                                           "password": register_new_courier_and_return_login_password['password']})

        assert response.status_code == Data.success_status_code

        delete_created_courier({"login": register_new_courier_and_return_login_password['login'],
                                "password": register_new_courier_and_return_login_password['password']})

    @allure.title('Авторизация без логина')
    @allure.description('Проверить корректность вывода ошибки и кода ошибки')
    def test_login_courier_without_login(self, register_new_courier_and_return_login_password):
        requests = CourierReq()
        response = requests.courier_login({"login": "",
                                           "password": register_new_courier_and_return_login_password["password"]})
        r = response.json()

        assert r["message"] == Data.login_without_data and response.status_code == Data.bad_request_status_code

    @allure.title('Авторизация без пароля')
    @allure.description('Проверить корректность вывода ошибки и кода ошибки')
    def test_login_courier_without_password(self, register_new_courier_and_return_login_password):
        requests = CourierReq()
        response = requests.courier_login({"login": register_new_courier_and_return_login_password["login"],
                                           "password": ""})
        r = response.json()

        assert r["message"] == Data.login_without_data and response.status_code == Data.bad_request_status_code

    @allure.title('Авторизация курьера для получения id')
    @allure.description('Проверяем, что в теле ответа приходит id')
    def test_login_courier_answer_body_have_id(self, register_new_courier_and_return_login_password):
        requests = CourierReq()
        response = requests.courier_login({"login": register_new_courier_and_return_login_password["login"],
                                           "password": register_new_courier_and_return_login_password["password"]})
        r = response.json()

        assert len(str(r["id"])) > 0

        delete_created_courier({"login": register_new_courier_and_return_login_password["login"],
                                "password": register_new_courier_and_return_login_password["password"]})

    @allure.title('Авторизация не существующего курьера')
    @allure.description('Проверяем, что в случае не существующего курьера, будет ошибка')
    def test_login_courier_answer_body_have_id(self, register_new_courier_and_return_login_password):
        requests = CourierReq()
        response = requests.courier_login(
            {"login": (register_new_courier_and_return_login_password["login"] + str(random.randint(1, 10))),
             "password": register_new_courier_and_return_login_password["password"]})
        r = response.json()

        assert r["message"] == Data.login_with_incorrect_data and response.status_code == Data.not_found_status_code

        delete_created_courier({"login": register_new_courier_and_return_login_password["login"],
                                "password": register_new_courier_and_return_login_password["password"]})
