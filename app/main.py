from fastapi import FastAPI

from core.config import settings

app = FastAPI(title=settings.app_title)


# @app.get('/')
# def read_root():
#     return {'Hello': 'FastAPI'}

# @app.on_event("startup")
# async def startup():
#     if not database.is_connected:
#         await database.connect()
#     # await QuestionsNum.objects.get_or_create(questions_num=1)


# @app.on_event("shutdown")
# async def shutdown():
#     if database.is_connected:
#         await database.disconnect()