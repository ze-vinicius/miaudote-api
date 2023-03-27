from enum import Enum
from typing import Optional
from pydantic import BaseModel

from app.schemas.address import Address

class PetShelterBase(BaseModel):
    name: str
    phone: str
    email: str
    description: str

    instagram_address: Optional[str]
    facebook_address: Optional[str]
    twitter_address: Optional[str]

class PetShelterCreate(PetShelterBase):
    account_id: int

class PetShelterInDb(PetShelterCreate):
    id: int
    address: Address

    class Config:
        orm_mode = True

class PetShelter(PetShelterInDb):
    pass