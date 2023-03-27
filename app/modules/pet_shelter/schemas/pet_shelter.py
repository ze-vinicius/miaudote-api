from typing import Optional
from pydantic import  BaseModel, EmailStr

from app.modules.pet_shelter.schemas.address import Address

class PetShelterBase(BaseModel):
    name: str
    phone: str
    email: EmailStr
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