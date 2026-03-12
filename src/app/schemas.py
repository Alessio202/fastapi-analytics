from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    age: int
    city: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    registration_date: datetime
    class Config:
        from_attributes = True