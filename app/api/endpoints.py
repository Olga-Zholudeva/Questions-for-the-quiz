import asyncio
from fastapi import APIRouter
from crud.crud import create_question_num, create_question, get_last
from schemas.schemas import QuestionsNumCreate
from models.models import Questions
from sqlalchemy import exists, select
from core.db import AsyncSessionLocal

import httpx

router = APIRouter()

@router.post('/questions_num')
async def create_new_question_num(
    question_num: QuestionsNumCreate
):
    async with httpx.AsyncClient() as client:
        for _ in range(question_num.count):
            while True:
                response = await client.get('https://jservice.io/api/random')
            
                if response.status_code == 200:
                    question = response.json()[0]
                    
                    async with AsyncSessionLocal() as session:
                        exists_query = select(exists().where(Questions.question_id == question['id']))
                        exists_result = await session.execute(exists_query)
                        
                        if not exists_result.scalar():  # Если вопрос не существует в БД
                            new_question = await create_question(question)
                            print(new_question)
                        else:  # Если вопрос уже существует в БД, делаем новый запрос к API
                            continue
                await asyncio.sleep(1)  # Подождать 1 секунду перед следующим запросом API

        last_question = await get_last(Questions)
        if last_question:
            return last_question
        else:
            return None

# @router.post('/questions_num')
# async def create_new_question_num(
#     question_num: QuestionsNumCreate,
# ):
#     async with httpx.AsyncClient() as client:
#         response = await client.get('https://jservice.io/api/random', params={'count': question_num.count})
    
#     if response.status_code == 200:
#         question_data = response.json()
#         for question in question_data:
#             exists_query = select(exists().where(Questions.question_id == question['question_id']))
#             async with AsyncSessionLocal() as session:
#                 exists_result = await session.execute(exists_query)
#                 if exists_result.scalar():
#                     async with httpx.AsyncClient() as client:
#                         response = await client.get('https://jservice.io/api/random', params={'count': question_num.count})
                        
#                 else:
#                     new_question = await create_question(question)
#                     print(new_question.question)
#     last_question = await get_last(Questions)
#     if last_question:
#         return last_question
#     else:
#         return None