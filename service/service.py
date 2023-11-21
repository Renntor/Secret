from string import digits, ascii_letters
from random import sample, shuffle


def random_secret_key() -> str:
    """
    generator secret_key
    :return:
    """
    symbol = tuple(digits + ascii_letters)
    secret_key = sample(symbol, counts=[5]*62, k=50)
    shuffle(secret_key)
    return ''.join(secret_key)
