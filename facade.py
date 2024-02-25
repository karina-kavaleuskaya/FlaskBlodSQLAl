from sqlalchemy import delete, insert, select, update
from db import PostModel


class PostFacade:

    def __init__(self, engine_db):
        self.__connection = engine_db.connect()
        self.__model = PostModel

    def get_all_posts(self):
        query = select(self.__model)
        cursor = self.__connection.execute(query)
        return cursor.mappings().all()

    def create_post(self,title, content):
        query = insert(self.__model).values(title=title, content=content)
        self.__connection.execute(query)
        self.__connection.commit()

    def get_post(self, post_id):
        query = select(self.__model).where(self.__model.id == post_id)
        cursor = self.__connection.execute(query)
        return cursor.mappings().one()

    def update(self, post_id, title, content):
        query = update(self.__model).where(self.__model.id == post_id).values(title=title, content=content)
        self.__connection.execute(query)
        self.__connection.commit()

    def delete_post(self, post_id):
        query = delete(self.__model).where(self.__model.id == post_id)
        self.__connection.execute(query)
        self.__connection.commit()