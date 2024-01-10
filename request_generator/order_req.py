import requests
from data import Data
from endpoints import Endpoints

class OrderReq:
    def create_order_request(self, order_data):
        response = requests.post(Data.base_url + Endpoints.create_orders_endpoint, data=order_data,
                                 headers={"Content-Type": "text/plain"})

        return response

    def order_list_request(self):
        response = requests.get(Data.base_url + Endpoints.create_orders_endpoint, headers={"Content-Type": "text/plain"})

        return response
