from request_generator.courier_req import CourierReq


def delete_created_courier(courier_data):
    courier = courier_data

    c = CourierReq()

    login_response = c.courier_login(courier)
    delete_response = c.courier_delete(login_response.json()['id'])

    return delete_response
