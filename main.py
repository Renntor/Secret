from fastapi import FastAPI
from routers.secret import router

app = FastAPI()

app.include_router(router=router)
