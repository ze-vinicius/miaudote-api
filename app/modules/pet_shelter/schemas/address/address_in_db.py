from typing import Optional

from pydantic import BaseModel


class AddressInDb(BaseModel):
    city: str
    country: str
    state: str
    street_address: Optional[str]
    zip_code: Optional[str]
    pet_shelter_id: str
