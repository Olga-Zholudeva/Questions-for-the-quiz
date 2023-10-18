from core.db import AsyncSessionLocal
from models.models import QuestionsNum, Questions
from schemas.schemas import QuestionsNumCreate
from datetime import datetime
from sqlalchemy import select


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


async def create_question(
        new_question: str
) -> Questions:
    db_question = Questions(
        question_id=new_question['id'],
        question=new_question['question'],
        ancwer=new_question['answer'],
        created=datetime.strptime(new_question['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ").date()
    )
    async with AsyncSessionLocal() as session:
        session.add(db_question)
        await session.commit()
        await session.refresh(db_question)
    return db_question

async def get_last(
        model: Questions
):
    async with AsyncSessionLocal() as session:
        query = select(model).order_by(model.id.desc()).offset(1).limit(1)
        questions = await session.execute(query)
        return questions.scalars().first()

