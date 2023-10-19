from fastapi import APIRouter
from crud.crud import get_last, get_questions
from schemas.schemas import QuestionsNumCreate
from models.models import Questions


router = APIRouter()

LINK = 'https://jservice.io/api/random' 

@router.post('/questions_num')
async def create_new_question_num(
    question_num: QuestionsNumCreate,
):
    count_recurring_questions = await get_questions(LINK, question_num.count)
    while count_recurring_questions >0:
        count_recurring_questions = await get_questions(LINK, count_recurring_questions)

    last_question = await get_last(Questions)
    if last_question:
        return last_question
    else:
        return None