from fastapi import FastAPI

from app.core.config import settings
from app.endpoints import router

app = FastAPI(title=settings.app_title)

app.include_router(router)
