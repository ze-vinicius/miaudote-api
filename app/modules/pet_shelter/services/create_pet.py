from fastapi import HTTPException
from app.modules.pet_shelter.repositories.pet import PetRepository
from app.modules.pet_shelter.schemas.pet import PetBase, PetCreate
from sqlalchemy.orm import Session

class CreatePetService:
  def __init__(self, db: Session):
    self.db = db

  def execute(self, pet_shelter_id: str, pet: PetBase):
    pet_repository = PetRepository(self.db)

    created_pet = pet_repository.create(PetCreate(
      age = pet.age,
      description = pet.description,
      name = pet.name,
      sex = pet.sex,
      size = pet.size,
      species = pet.species,
      temper = pet.temper,
      adoption_status = pet.adoption_status,
      health_status = pet.health_status,
      pet_shelter_id = pet_shelter_id,
    ))

    return created_pet



