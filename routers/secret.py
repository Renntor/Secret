from fastapi import APIRouter
from models.secretin import Secret
from config.db import collection_name
from schemas.secret import secretEntity
from service.service import random_secret_key


router = APIRouter()


@router.get('/ping')
async def ping():
    return {"Success": True}


@router.post('/generate')
async def post_secret(secret: str, password: str):
    secret_key = random_secret_key()
    new_secret = Secret(secret=secret, secret_key=secret_key, password=password)
    id = collection_name.insert_one((dict(new_secret))).inserted_id
    return secretEntity(collection_name.find_one({'_id': id}))['secret_key']


@router.post('/secrets/{secret_key}')
async def get_secret(password: str, secret_key: str):
    secret = collection_name.find_one({'password': password, 'secret_key': secret_key})
    if secret is not None:
        return secretEntity(secret)['secret']
    return secret
