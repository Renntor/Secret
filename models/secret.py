from datetime import datetime
from pydantic import BaseModel


class SecretGet(BaseModel):
    password: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "password": "MySecretPassword",
                }
            ]
        }
    }


class SecretPost(SecretGet):
    secret: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "password": "MySecretPassword",
                    "secret": "Create my secret"
                }
            ]
        }
    }


class Secret(SecretPost):
    secret_key: str
    inserted: datetime
