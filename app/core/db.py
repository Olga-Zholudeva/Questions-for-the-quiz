# import databases
# import ormar
# import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr
from core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import Column, Integer


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.database_url)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# database = databases.Database(settings.database_url)
# metadata = sqlalchemy.MetaData()

# class BaseMeta(ormar.ModelMeta):
#     metadata = metadata
#     database = database

# class QuestionsNum(ormar.Model):
#     class Meta(BaseMeta):
#         tablename = "Questions_num"
#     id: int = ormar.Integer(primary_key=True)
#     questions_num: int = ormar.Integer()


# engine = sqlalchemy.create_engine(settings.database_url)
# metadata.create_all(engine)

