from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import declared_attr

from app.core.db import Base


class Questions(Base):
    """Модель для хранения вопросов для викторин."""

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, unique=True, nullable=False)
    question = Column(String, nullable=False)
    ancwer = Column(String, nullable=False)
    created = Column(Date, nullable=False)
