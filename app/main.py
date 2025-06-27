from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI()

@api_router.get("/ping")
def ping():
    return {"message": "pong"}

app.include_router(api_router)
