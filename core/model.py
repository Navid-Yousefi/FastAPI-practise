from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)

    first_name = Column(String(length=30))
    last_name = Column(String(length=30))
    age = Column(Integer)

    def __repr__(self):
        return f"User(id={self.id},first_name={self.first_name},age={self.age})"