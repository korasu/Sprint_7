import random
import string
from datetime import datetime, timedelta


def generate_order_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_date():
        start_date = datetime(2017, 1, 1)
        end_date = datetime.now()

        random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
        formatted_date = random_date.strftime('%Y-%m-%d')
        return formatted_date

    order_data = {}

    order_data["firstName"] = generate_random_string(10)
    order_data["lastName"] = generate_random_string(10)
    order_data["address"] = generate_random_string(10) + '' + generate_random_string(10) + '' + str(
        random.randint(1, 150))
    order_data["metroStation"] = random.randint(1, 20)
    order_data["phone"] = '+7' + str(random.randint(100, 999)) + str(random.randint(100, 999)) + str(
        random.randint(1000, 9999))
    order_data["rentTime"] = random.randint(1, 5)
    order_data["deliveryDate"] = generate_random_date()
    order_data["comment"] = generate_random_string(22)
    order_data["color"] = []

    return order_data
