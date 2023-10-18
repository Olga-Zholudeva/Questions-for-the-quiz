from fastapi import FastAPI
from core.config import settings
from api.endpoints import router

app = FastAPI(title=settings.app_title)

app.include_router(router)
