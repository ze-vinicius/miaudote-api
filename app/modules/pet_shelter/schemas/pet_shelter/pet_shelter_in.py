from typing import Optional

from pydantic import BaseModel, EmailStr

from app.modules.pet_shelter.schemas.address import AddressIn


class PetShelterIn(BaseModel):
    name: str
    phone: str
    email: EmailStr
    description: str

    instagram_address: Optional[str] = None
    facebook_address: Optional[str] = None
    twitter_address: Optional[str] = None

    address: AddressIn

    password: str
