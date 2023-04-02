from typing import Optional

from pydantic import BaseModel


class AddressIn(BaseModel):
    city: str
    country: str
    state: str
    street_address: Optional[str]
    zip_code: Optional[str]
