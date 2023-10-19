from fastapi import APIRouter

from app.crud import get_last, get_questions
from app.models import Questions
from app.schemas import QuestionsNumCreate

router = APIRouter()

LINK = "https://jservice.io/api/random"


@router.post("/questions_num")
async def create_new_question_num(
    question_num: QuestionsNumCreate,
):
    """
    Контроллер принимает POST запрос с количеством вопросов.
    Запрашивает вопросы с публичного API.
    Сохраняет новые запросы в БД.
    Осуществляет повторный/е запрос/ы к API для вопросов, которые есть в БД.
    Возвращает предпоследнюю запись из БД либо Null в случае если в БД 1 запись.
    """
    count_recurring_questions = await get_questions(LINK, question_num.count)
    while count_recurring_questions > 0:
        count_recurring_questions = await get_questions(LINK, count_recurring_questions)

    last_question = await get_last(Questions)
    if last_question:
        return last_question
    else:
        return None
