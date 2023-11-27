from string import digits, ascii_letters
from random import sample, shuffle
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import os

load_dotenv()


def random_secret_key() -> str:
    """
    generator secret_key
    :return:
    """
    symbol = tuple(digits + ascii_letters)
    secret_key = sample(symbol, counts=[5]*62, k=50)
    shuffle(secret_key)
    return ''.join(secret_key)


def crypto_secret(text: str) -> bytes:
    """
    encrypto secret
    :param text:
    :return:
    """
    fernet = Fernet(os.environ.get('HASH_KEY').encode())
    return fernet.encrypt(bytes(text.encode()))


def decrypto_secret(data: bytes) -> str:
    fernet = Fernet(os.environ.get('HASH_KEY'))
    return fernet.decrypt(data).decode()
