from typing import Optional

from app.core.models import BaseModel


class Address(BaseModel):
    id: int
    city: str
    country: str
    state: str
    street_address: Optional[str]
    zip_code: Optional[str]

    pet_shelter_id: int
