from fastapi import FastAPI
from routers.secret import router

tags_metadata = [
    {
        "name": "post_secret",
        "description": "The operation of creating a secret.",
    },
    {
        "name": "get_secret",
        "description": "Obtaining the secret.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

app.include_router(router=router)
