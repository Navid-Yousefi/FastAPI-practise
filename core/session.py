from database import SessionLocal, Base, engine
from model import User, Address, Profile, Post, Comment

Base.metadata.create_all(engine)


session = SessionLocal()
