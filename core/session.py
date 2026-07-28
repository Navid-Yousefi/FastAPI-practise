from database import SessionLocal, Base, engine
from model import User

Base.metadata.create_all(engine)


session = SessionLocal()


