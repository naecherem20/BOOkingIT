from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Services(BaseModel):
    title:str
    description:str
    price:str
    duration_minutes:str
    is_active:bool
    created_at: datetime