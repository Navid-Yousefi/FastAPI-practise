from fastapi import FastAPI, Query, status, Body, HTTPException, Form, Path, Depends
from contextlib import asynccontextmanager
from dataclasses import dataclass
from schemas import PersonCreateSchema, PersonResponseSchema, PersonUpdateSchema
import random
from typing import List
from database import Base, Person, engine
from database import get_db
from sqlalchemy.orm import Session



@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Application startup')
    Base.metadata.create_all(engine)

    yield
    print('Application shutdown')



app = FastAPI(lifespan=lifespan)



@app.get("/names", status_code=status.HTTP_200_OK, response_model=List[PersonResponseSchema])
def retrieve_names_list(db: Session = Depends(get_db)):
    query = db.query(Person).all()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No objects found')
    return query


@app.get('/name', status_code=status.HTTP_200_OK, response_model=PersonResponseSchema)
def retrive_name_detail( db: Session = Depends(get_db), q:int = Query(..., title='Object id' , description='the id of name in name_list')):
    query = db.query(Person).filter_by(name=q).one_or_none()
    if query is not None:
        return query

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Object not found')




@app.post('/create', status_code=status.HTTP_201_CREATED, response_model=PersonResponseSchema)
def create_name(person: PersonCreateSchema, db: Session = Depends(get_db)):
    query = db.query(Person).filter_by(name=person.name).one_or_none()
    if query is None:
        new_person = Person(name=person.name)
        db.add(new_person)
        db.commit()
        db.refresh(new_person)
        return new_person
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='this name alredy exist')


@app.put('/update/{name_id}', status_code=status.HTTP_200_OK, response_model=PersonResponseSchema)
def update_name_list(request: PersonUpdateSchema, name_id: int = Path(), db: Session = Depends(get_db)):
    person = db.query(Person).filter_by(id=name_id).first()
    if person:
        person.name = request.name
        db.commit()
        db.refresh(person)
        return person
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)



@app.delete('/delete/{user_id}', status_code=status.HTTP_200_OK)
def delete_name(name_id: int, db: Session = Depends(get_db)):
    person = db.query(Person).filter_by(id=name_id).one_or_none()
    if person:
        db.delete(person)
        db.commit()
        return {'message': 'object is deleted'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)






    