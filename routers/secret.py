from fastapi import APIRouter
from models.secret import Secret
from config.db import conn
from starlette.requests import Request
from schemas.secret import secretEntity, secretsEntity

secret = APIRouter()


@secret.get('/ping')
async def ping():
    return {"Success": True}


@secret.post('/generate')
async def post_secret(request: Request):
    pass