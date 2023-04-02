from typing import List
from app.modules.pet_shelter.schemas.pet import Pet
from app.modules.pet_shelter.repositories.pet import PetRepository
from sqlalchemy.orm import Session


class GetAllPetsFromPetShelter:
    def __init__(self, db: Session):
        self.db = db

    def execute(self, pet_shelter_id: str):
        pet_repository = PetRepository(self.db)

        pet_models = pet_repository.get_all_by_pet_shelter_id(pet_shelter_id)

        pets = [Pet.from_orm(pet) for pet in pet_models]

        return pets
