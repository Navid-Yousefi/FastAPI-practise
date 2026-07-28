import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
DATABASE_URL = os.getenv('DATABASE_URL')


engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False}
)



SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


Base = declarative_base()