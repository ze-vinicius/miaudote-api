from typing import Optional
from pydantic import BaseModel, EmailStr

from app.modules.pet_shelter.schemas.address import AddressIn


class PetShelterIn(BaseModel):
    name: str
    phone: str
    email: EmailStr
    description: str

    instagram_address: Optional[str]
    facebook_address: Optional[str]
    twitter_address: Optional[str]
    
    address: AddressIn
    password: str
