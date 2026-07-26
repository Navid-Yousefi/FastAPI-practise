from fastapi import FastAPI, Query, status, Body, HTTPException, Form
import random

app = FastAPI()


name_list = [
    {"id": 1, "name": "navid"},
    {"id": 2, "name": "ali"},
    {"id": 3, "name": "reza"},
    {"id": 4, "name": "saman"},
    {"id": 5, "name": "aghil"},
]

@app.get("/names")
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



@app.post('/create')
def create_name(name: str = Form()):
    name_obj = {"id": random.randint(1, 999), "name": name}
    name_list.append(name_obj)
    return name_obj


@app.put('/update/{name_id}')
def update_name_list(name_id: int, name: str):
    for item in name_list:
        if item['id'] == name_id:
            item['name'] == name
            return item
    return {'detail': 'object not found'}






    