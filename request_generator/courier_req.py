import requests
from endpoints import Endpoints


class CourierReq:
    def courier_create(self, courier_data):
        response = requests.post(Endpoints.base_url + Endpoints.create_courier, data=courier_data)
        return response

    def courier_login(self, courier_data):
        response = requests.post(Endpoints.base_url + Endpoints.login_endpoint,
                                 data=courier_data)
        return response

    def courier_delete(self, courier_id):
        response = requests.delete(Endpoints.base_url + Endpoints.delete_courier_endpoint + str(courier_id))
        return response
