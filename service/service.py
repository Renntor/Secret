from random import shuffle

from dotenv import load_dotenv
from cryptography.fernet import Fernet
import os

load_dotenv()


def random_secret_key(password: str) -> str:
    """
    generator secret_key
    :return:
    """
    secret_key = list(password[3:])
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


def decrypto_secret(data: bytes) -> dict:
    """
    decrypto secret
    :param data:
    :return:
    """
    fernet = Fernet(os.environ.get('HASH_KEY'))
    return {'secret': fernet.decrypt(data).decode()}
