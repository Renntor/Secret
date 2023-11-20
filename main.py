from fastapi import FastAPI
from routers.secret import secret

app = FastAPI()

app.include_router(router=secret)