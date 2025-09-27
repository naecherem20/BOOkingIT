from sqlmodel import SQLModel , Field
from uuid import UUID, uuid4
from pydantic import EmailStr
from datetime import datetime
from enum import Enum


class RoleStatus(str, Enum):
    user="user"
    admin="admin" 

class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    name:str
    email: str = Field(index=True, unique=True)
    password:str
    role:str= Field(default=RoleStatus.user)
    created_at: datetime

class Service(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    booking_id:UUID= Field(foreign_key="user.id")
    title:str
    description:str
    price:str
    duration_minutes:str
    is_active:bool= Field(default=True)
    created_at: datetime= Field(default_factory=datetime.utcnow)

class BookingStatus(str, Enum):
    pending="pending"
    confirmed="confirmed" 
    cancelled="cancelled"
    completed="completed"

class Booking(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    user_id: UUID = Field(foreign_key="user.id")
    service_id: UUID= Field(foreign_key="service.id")
    start_time:datetime
    end_time: datetime
    status: str=Field(default=BookingStatus.pending)
    created_at:datetime = Field(default_factory=datetime.utcnow)

class Review(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    booking_id:UUID =Field(foreign_key="booking.id")
    rating:int = Field(max_length=5)
    comment:str
    created_at: datetime= Field(default_factory=datetime.utcnow)
