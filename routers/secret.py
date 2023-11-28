from fastapi import APIRouter
from models.secret import Secret, SecretPost, SecretGet
from config.db import collection_name
from schemas.secret import secretEntity, secret_keyEntity
from service.service import random_secret_key, crypto_secret, decrypto_secret
from passlib.context import CryptContext
from datetime import datetime


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter()


@router.post('/generate', tags=['post_secret'])
async def post_secret(secret: SecretPost) -> dict:
    """
    Post secret with password
    """
    secret_key = random_secret_key()
    password = pwd_context.hash(secret.password)
    secret = crypto_secret(secret.secret)
    new_secret = Secret(secret=secret, secret_key=secret_key, password=password, inserted=datetime.utcnow())
    id_document = collection_name.insert_one((dict(new_secret))).inserted_id
    return secret_keyEntity(collection_name.find_one({'_id': id_document}))


@router.post('/secrets/{secret_key}', tags=['get_secret'])
async def get_secret(password: SecretGet, secret_key: str) -> dict:
    """
    Get secret and delete him
    """
    secret = collection_name.find_one({'secret_key': secret_key})
    try:
        # password verification
        verification = pwd_context.verify(password.password, secretEntity(secret)['password'])
        if secret is not None and verification:
            collection_name.delete_one({'secret_key': secret_key})
            return decrypto_secret(secretEntity(secret)['secret'])
    except (ValueError, TypeError):
        return {'secret': None}
