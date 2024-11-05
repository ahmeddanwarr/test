from pydantic import BaseModel
from uuid import UUID

class ProductCreate(BaseModel):
    guid: UUID
    price: float

class ProductResponse(BaseModel):
    guid: UUID
    price: float

    class Config:
        from_attributes = True 
