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


def generate_random_email():
    return ''.join(
        random.choices(string.ascii_lowercase, k=5) + ["@gmail.com"]
    )


def generate_random_phone():
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # random.shuffle(numbers)
    return''.join(
        [str(6511)] + [' '] + [str(random.randint(0, 9))] + [str(random.randint(0, 9))] + [str(random.randint(0, 9))] + [str(random.randint(0, 9))] + [str(random.randint(0, 9))]
    )

def generate_random_company_name():
    return ''.join(
        random.choices(string.ascii_uppercase, k=1) + random.choices(string.ascii_lowercase, k=10)
    )


def generate_random_alternate_name():
    return ''.join(
        random.choices(string.ascii_uppercase, k=4)
    )


def generate_random_website():
    return ''.join(
        random.choices(string.ascii_lowercase, k=5) + [".com"]
    )

def generate_random_month():
    return''.join(
        [str(random.randint(0, 12))]
    )

def generate_random_day():
    return''.join(
        [str(random.randint(0, 28))]
    )

def generate_random_year():
    return''.join(
        [str(random.randint(2000, 2024))]
    )
