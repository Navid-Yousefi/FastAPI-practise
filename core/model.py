from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime


enrollments = Table(
    'student_course', Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('course_id', Integer, ForeignKey('courses.id')),
    Column('enrolled_date', DateTime, default=datetime.now),
    UniqueConstraint('user_id', 'course_id', name='unique_user_course_enrolled')
)



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)

    username = Column(String(length=30))
    email = Column(String(), nullable=True)
    password = Column(Integer)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    addresses = relationship("Address", backref='user')
    profile = relationship('Profile', backref='user', uselist=False)
    posts = relationship('Post', backref='user')
    courses = relationship('Course', secondary=enrollments, back_populates='attendees')


    def __repr__(self):
        return f"User(id={self.id},username={self.username},email={self.email})"



class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    

    city = Column(String(length=100))
    state = Column(String())
    zip_code = Column(Integer)
    
    def __repr__(self):
        return f"Address(id={self.id}, user_id{self.user_id} , city={self.city}, state={self.state})"



class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)

    first_name = Column(String(length=30))
    last_name = Column(String(length=30))
    bio = Column(Text, nullable=True)

    def __repr__(self):
        return f'Profile(id={self.id}, first_name={self.first_name}, last_name={self.last_name}'



class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    comments = relationship('Comment', backref='post')

    title = Column(String)
    content = Column(Text)
    created_date = Column(DateTime, default=datetime.now)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title})"


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    parent_id = Column(Integer, ForeignKey('comments.id'), nullable=True)

    parent = relationship('Comment', back_populates='children', remote_side=[id])
    children = relationship('Comment', back_populates='parent', remote_side=[parent_id])

    content = Column(Text)
    created_date = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f'Comment(id={self.id}, post_id={self.post_id}, user_id={self.user_id}, content={self.content})'




class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=300))
    description = Column(Text)

    attendees = relationship('User', secondary=enrollments, back_populates='courses')
    

    created_date = Column(DateTime, default=datetime.now)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'Course(id={self.id}, title={self.title})'



    