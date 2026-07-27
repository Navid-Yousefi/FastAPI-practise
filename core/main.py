from fastapi import FastAPI, Query, status, Body, HTTPException, Form
import random
from contextlib import asynccontextmanager

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

@app.get("/names", status_code=status.HTTP_200_OK)
def retrieve_names_list(
    q: str | None = Query(
        default=None,
        alias="Search",
        description="it will be searched with title you provided",
        max_length=250,
    )
):
    if q:
        return [i for i in name_list if i["name"] == q]
    return name_list



@app.post('/create', status_code=status.HTTP_201_CREATED)
def create_name(name: str = Body(embed=True)):
    name_obj = {"id": random.randint(1, 999), "name": name}
    name_list.append(name_obj)
    return name_obj


@app.put('/update/{name_id}', status_code=status.HTTP_200_OK)
def update_name_list(name_id: int, name: str):
    for item in name_list:
        if item['id'] == name_id:
            item['name'] == name
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)



@app.delete('/delete/{user_id}', status_code=status.HTTP_200_OK)
def delete_name(user_id: int):
    for item in name_list:
        if item['id'] == user_id:
            name_list.remove(item)
            return {'detail': 'object removed successfally'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)






    