from pydantic import BaseModel


class Secret(BaseModel):
    secret: str
    secret_key: str
    password: str


class SecretPost(BaseModel):
    secret: str
    password: str


class SecretGet(BaseModel):
    password: str