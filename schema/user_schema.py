from pydantic import BaseModel, EmailStr
from datetime import  datetime
from uuid import uuid4,UUID




class UserCreate(BaseModel):
    id: UUID
    name:str
    email:EmailStr
    password:str
    role:str
    created_at: datetime

class UserReturn(BaseModel):
    name:str
    email:EmailStr
    role:str
    created_at: datetime

    class Config:
        orm_mode = True

