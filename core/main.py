from fastapi import FastAPI, Query, status, Body, HTTPException, Form, Path
from contextlib import asynccontextmanager
from dataclasses import dataclass
from schema import PersonCreateSchema, PersonResponseSchema, PersonUpdateSchema
import random
from typing import List



@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Application startup')

    yield
    print('Application shutdown')



app = FastAPI(lifespan=lifespan)




name_list = [
    {"id": 1, "name": "navid"},
    {"id": 2, "name": "ali"},
    {"id": 3, "name": "reza"},
    {"id": 4, "name": "saman"},
    {"id": 5, "name": "aghil"},
]

@app.get("/names", status_code=status.HTTP_200_OK, response_model=List[PersonResponseSchema])
def retrieve_names_list():
    return name_list


@app.get('/names/{name_id}', status_code=status.HTTP_200_OK, response_model=PersonResponseSchema)
def retrive_name_detail(name_id:int = Path(..., title='Object id' , description='the id of name in name_list')):
    for item in name_list:
        if item['id'] == name_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Object not found')




@app.post('/create', status_code=status.HTTP_201_CREATED, response_model=PersonResponseSchema)
def create_name(person: PersonCreateSchema):
    name_obj = {"id": random.randint(1, 999), "name": person.name}
    name_list.append(name_obj)
    return name_obj


@app.put('/update/{name_id}', status_code=status.HTTP_200_OK, response_model=PersonResponseSchema)
def update_name_list(person: PersonUpdateSchema, name_id: int = Path):
    for item in name_list:
        if item['id'] == name_id:
            item['name'] = person.name
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)



@app.delete('/delete/{user_id}', status_code=status.HTTP_200_OK)
def delete_name(user_id: int):
    for item in name_list:
        if item['id'] == user_id:
            name_list.remove(item)
            return {'detail': 'object removed successfally'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)






    