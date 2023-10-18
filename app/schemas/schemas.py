from pydantic import BaseModel


class QuestionsNumCreate(BaseModel):
    """Схема для запроса с количеством вопросов."""
    count: int