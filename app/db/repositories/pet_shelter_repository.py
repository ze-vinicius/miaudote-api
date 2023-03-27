from sqlalchemy.orm.session import Session
from app.db.models.address import AddressModel
from app.db.models.pet_shelter import PetShelterModel
from app.db.repositories.base import BaseRepository

from app.schemas import PetShelterCreate

class PetShelterRepository(BaseRepository):
  def create(self, payload: PetShelterCreate):
    new_pet_shelter = PetShelterModel(
      name = payload.name,
      email = payload.email,
      phone = payload.phone,
      description = payload.description,
      
      instagram_address = payload.instagram_address,
      facebook_address = payload.facebook_address,
      twitter_address = payload.twitter_address,
      
      account_id = payload.account_id
    )

    self.db.add(new_pet_shelter)
    self.db.commit()
    self.db.refresh(new_pet_shelter)

    return new_pet_shelter

  def get_all(self):
    return self.db.query(PetShelterModel).all()
