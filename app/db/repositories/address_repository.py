from sqlalchemy.orm.session import Session
from app.db.models.address import AddressModel
from app.db.models.pet_shelter import PetShelterModel
from app.db.repositories.base import BaseRepository

from app.schemas import AddressCreate

class AddressRepository(BaseRepository):
  def create(self, payload: AddressCreate):
    new_address = AddressModel(
      city = payload.city,
      country = payload.country,
      state = payload.state,
      street_address = payload.street_address,
      zip_code = payload.zip_code,
      pet_shelter_id = payload.pet_shelter_id
    )

    self.db.add(new_address)
    self.db.commit()
    self.db.refresh(new_address)

    return new_address
