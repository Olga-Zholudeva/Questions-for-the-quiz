from typing import Optional

from pydantic import BaseModel


class QuestionsNumCreate(BaseModel):
    questions_num: int