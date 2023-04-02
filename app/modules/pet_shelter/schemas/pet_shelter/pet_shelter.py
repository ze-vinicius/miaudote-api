from typing import Optional

from pydantic import BaseModel, EmailStr

from app.modules.pet_shelter.schemas.address import Address


class PetShelter(BaseModel):
    id: int
    name: str
    phone: str
    email: EmailStr
    description: str

    instagram_address: Optional[str]
    facebook_address: Optional[str]
    twitter_address: Optional[str]

    account_id: int
    address: Address

    class Config:
        orm_mode = True
