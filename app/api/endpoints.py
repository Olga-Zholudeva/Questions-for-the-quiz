from fastapi import APIRouter
from crud.crud import create_question_num
from schemas.schemas import QuestionsNumCreate

router = APIRouter()

@router.post('/questions_num')
async def create_new_question_num(
    question_num: QuestionsNumCreate,
):
   new_question_num = await create_question_num(question_num)
   return new_question_num