import random
import string


def generate_random_first_name():
    return ''.join(
        random.choices(string.ascii_uppercase, k=1) + random.choices(string.ascii_lowercase, k=5)
    )


def generate_random_last_name():
    return ''.join(
        random.choices(string.ascii_uppercase, k=1) + random.choices(string.ascii_lowercase, k=5)
    )