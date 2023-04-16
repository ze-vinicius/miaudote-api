from typing import Optional

from pydantic import BaseModel, EmailStr


class PetShelterInDb(BaseModel):
    name: str
    phone: str
    email: EmailStr
    description: str

    instagram_address: Optional[str]
    facebook_address: Optional[str]
    twitter_address: Optional[str]

    owner_id: int
