from pydantic import BaseModel


class Secret(BaseModel):
    secret: str
    url: str
    password: str
