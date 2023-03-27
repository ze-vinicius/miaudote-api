from app.db.repositories.pet_shelter_repository import PetShelterRepository
from sqlalchemy.orm import Session


class GetAllPetSheltersService:
  def __init__(self, db: Session):
    self.db = db

  def execute(self):
    pet_shelter_repository = PetShelterRepository(self.db)

    return pet_shelter_repository.get_all()


