from datetime import datetime

import httpx
from sqlalchemy import exists, select

from app.models import Questions
from app.core.db import AsyncSessionLocal


async def create_question(new_question: str) -> Questions:
    """Создание записи в БД"""
    db_question = Questions(
        question_id=new_question["id"],
        question=new_question["question"],
        ancwer=new_question["answer"],
        created=datetime.strptime(
            new_question["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ"
        ).date(),
    )
    async with AsyncSessionLocal() as session:
        session.add(db_question)
        await session.commit()
        await session.refresh(db_question)
    return db_question


async def get_questions(link: str, count: int) -> int:
    """Получение вопросов с публичного API."""
    async with httpx.AsyncClient() as client:
        response = await client.get(link, params={"count": count})
    question_data = response.json()
    counter = 0
    for question in question_data:
        async with AsyncSessionLocal() as session:
            exists_result = await session.execute(
                select(exists().where(Questions.question_id == question["id"]))
            )
            if exists_result.scalar():
                counter += 1
            else:
                await create_question(question)
    return counter


async def get_last(model: Questions) -> Questions:
    """Получение предпоследней записи из БД."""
    async with AsyncSessionLocal() as session:
        questions = await session.execute(
            select(model).order_by(model.id.desc()).offset(1).limit(1)
        )
        return questions.scalars().first()
