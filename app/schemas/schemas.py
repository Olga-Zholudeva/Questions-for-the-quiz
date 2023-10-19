from pydantic import BaseModel


class QuestionsNumCreate(BaseModel):
    """Схема для запроса количества вопросов."""
    count: int