
from pydantic import BaseModel, field_validator, field_serializer, Field


class BasePersonSchema(BaseModel):
    name: str = Field(..., description='Enter Persons name')

    @field_validator
    def validate_name(cls, value):
        if len(value) > 32:
            raise ValueError('Name must not exceed 32 characters')
        if not value.isalpha():
            raise ValueError('Name must contain only alphabetic characters')
        return value

    @field_serializer('name')
    def serializer_name(value):
        return value.title()

class PersonCreateSchema(BaseModel):
    pass


class PersonResponseSchema(BaseModel):
    id: int = Field(..., description='Unique user identifier')



class PersonUpdateSchema(BaseModel):
    pass