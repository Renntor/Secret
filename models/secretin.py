from pydantic import BaseModel


class SecretGet(BaseModel):
    password: str


class SecretPost(SecretGet):
    secret: str


class Secret(SecretPost):
    secret_key: str
