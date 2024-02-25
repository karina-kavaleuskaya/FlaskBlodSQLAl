from sqlalchemy import TIMESTAMP, Column, Integer, String, create_engine, URL
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func



Base = declarative_base()


class PostModel(Base):
    __tablename__= 'posts'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created = Column(TIMESTAMP, nullable=False, default=func.current_timestamp())


class EngineDB:
    url_obj = URL.create(
        "****",
        username="****",
        password="****",
        host="*****",
        port=****,
        database="****"
    )


    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = create_engine(url=cls.url_obj)
        return cls.__instance