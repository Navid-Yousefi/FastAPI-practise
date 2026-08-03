# from database import SessionLocal, Base, engine
# from model import User, Address, Profile, Post, Comment, Course, enrollments

# Base.metadata.create_all(engine)


# session = SessionLocal()

# session.add(User(username='navid', email='navid@example.com', password='password123'))
# session.commit()

# user = session.query(User).filter_by(username='navid').first()

# post = session.query(Post).filter_by(user_id=user.id).first()

# courses = session.query(Course).filter_by(title='title').one()


# courses.attendees.append(user)
# session.commit()

# session.add(Profile(user_id=user.id, first_name='Navid', last_name='Yousefi', bio='This is a sample bio'))
# session.commit()

# session.add(Address(user_id=user.id, city='New York', state='NY', zip_code='10001'))
# session.commit()

# session.add(Post(user_id=user.id, title='this is a sample title', content='this is a sample content'))
# session.commit()
# posts = user.posts[0]

# parent_comment = posts.comments[0]
# print(parent_comment)

# session.add(Comment(user_id=user.id, post_id=posts.id, parent_id=posts.id , content='this is a replay sample comment'))
# session.commit()


# childer = session.query(Comment).filter_by(id=2).first()

# session.add(Comment(user_id=user.id, post_id=posts.id, parent_id=childer.id , content='this is a replay sample comment'))
# session.commit()

# session.add(Course(title='title', description='Python is d best'))
# session.commit()





