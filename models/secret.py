from pydantic import BaseModel


class Secret(BaseModel):
    secret: str
    secret_key: str
    password: str
