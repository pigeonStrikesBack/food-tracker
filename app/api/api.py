from fastapi import FastAPI, APIRouter
from app.api.user import user_router

api_router = APIRouter(prefix="/api")
api_router.include_router(user_router)