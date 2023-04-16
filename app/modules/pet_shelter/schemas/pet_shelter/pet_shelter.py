from typing import Optional

from pydantic import EmailStr

from app.core.models import BaseModel
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

    owner_id: int
    address: Address
