from typing import Optional

from pydantic import BaseModel


class AddressBase(BaseModel):
  city: str
  country: str
  state: str
  street_address: Optional[str]
  zip_code: Optional[str]

class AddressCreate(AddressBase):
  pet_shelter_id: str

class AddressInDbBase(AddressCreate):
  id: int

  class Config:
    orm_mode = True
  
class Address(AddressInDbBase):
  pass



  