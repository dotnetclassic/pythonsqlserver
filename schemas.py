from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    age: int
    city: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True