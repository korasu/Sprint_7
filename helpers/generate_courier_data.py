import random
import string


def generate_courier_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = {}
    login_pass['login'] = generate_random_string(10)
    login_pass['password'] = generate_random_string(10)
    login_pass['firsName'] = generate_random_string(10)

    return login_pass
