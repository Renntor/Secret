from fastapi import APIRouter
from models.secret import Secret
from config.db import collection_name
from starlette.requests import Request
from schemas.secret import secretEntity, secretsEntity

router = APIRouter()


@router.get('/ping')
async def ping():
    return {"Success": True}


@router.post('/generate')
async def post_secret(secret: Secret):
    collection_name.insert_one((dict(secret)))
    return secretsEntity(collection_name.find())

