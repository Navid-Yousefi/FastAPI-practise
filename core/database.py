import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

# env_path = Path(__file__).parent.parent / '.env'
# load_dotenv(dotenv_path=env_path)
# DATABASE_URL = os.getenv('DATABASE_URL')


engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False}
)



SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


Base = declarative_base()

Base.metadata.create_all(engine)


session = SessionLocal()


class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return f"Person(id={self.id}, name={self.name})"



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()