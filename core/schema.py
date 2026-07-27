
from pydantic import BaseModel


class BasePersonSchema(BaseModel):
    name: str

class PersonCreateSchema(BaseModel):
    pass


class PersonResponseSchema(BaseModel):
    id: int



class PersonUpdateSchema(BaseModel):
    pass