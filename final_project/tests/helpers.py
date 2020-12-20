import random
import string


def get_random_string(length=5):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_correct_name():
    return get_random_string(10)


def get_correct_email():
    return get_random_string(7) + "@mail.ru"


def get_default_password():
    return "1"


def get_incorrect_email():
    return get_random_string(7) + "@mail.ru@"


def get_incorrect_name():
    return get_random_string(4)


def get_data(name=get_correct_name, email=get_correct_email, password=get_default_password):
    return name(), email(), password()
