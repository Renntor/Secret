from fastapi import APIRouter
from models.secret import Secret
from config.db import collection_name
from starlette.requests import Request
from schemas.secret import secretEntity
from service.service import random_secret_key


router = APIRouter()


@router.get('/ping')
async def ping():
    return {"Success": True}


@router.post('/generate')
async def post_secret(secret: Secret):
    secret.secret_key = random_secret_key()
    id = collection_name.insert_one((dict(secret))).inserted_id
    return secretEntity(collection_name.find_one({'_id': id}))['secret_key']

