from core.db import AsyncSessionLocal
from models.models import QuestionsNum
from schemas.schemas import QuestionsNumCreate


async def create_question_num(
        new_question_num: QuestionsNumCreate
) -> QuestionsNum:
    
    new_question_num_data = new_question_num.dict()
    db_question_num = QuestionsNum(**new_question_num_data)
    async with AsyncSessionLocal() as session:
        session.add(db_question_num)
        await session.commit()
        await session.refresh(db_question_num)
    return db_question_num