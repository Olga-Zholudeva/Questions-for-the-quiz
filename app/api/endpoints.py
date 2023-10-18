from fastapi import APIRouter
from crud.crud import create_question_num, create_question
from schemas.schemas import QuestionsNumCreate

import httpx

router = APIRouter()

@router.post('/questions_num')
async def create_new_question_num(
    question_num: QuestionsNumCreate,
):
    new_question_num = await create_question_num(question_num)
    async with httpx.AsyncClient() as client:
        response = await client.get('https://jservice.io/api/random', params={'count': question_num.count})
    
    if response.status_code == 200:
        question_data = response.json()
        for question in question_data: 
            new_question = await create_question(question)
            print(new_question)
    return new_question_num