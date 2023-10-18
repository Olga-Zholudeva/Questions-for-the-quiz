from sqlalchemy import Column, Integer, String, Date

from app.core.db import Base

class QuestionsNum(Base):
    count = Column(Integer, nullable=False)


class Questions(Base):
    id = Column(Integer, unique=True, nullable=False)
    question = Column(String, nullable=False)
    ancwer = Column(String, nullable=False)
    created = Column(Date, nullable=False)