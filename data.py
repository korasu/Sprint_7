class Data:
    base_url = 'https://qa-scooter.praktikum-services.ru'

    success_status_code = 200
    create_status_code = 201
    bad_request_status_code = 400
    not_found_status_code = 404
    conflict_status_code = 409

    create_courier_success = '{"ok":true}'
    login_without_data = "Недостаточно данных для входа"
    login_with_incorrect_data = "Учетная запись не найдена"
    create_courier_without_data = "Недостаточно данных для создания учетной записи"
    create_courier_with_repeated_data = "Этот логин уже используется. Попробуйте другой."


class OrderData:
    scooter_color = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]
