from app.modules.pet_shelter.repositories.pet import PetRepository
from sqlalchemy.orm import Session


class GetAllPetsFromPetShelter:
    def __init__(self, db: Session):
        self.db = db

    def execute(self, pet_shelter_id: str):
        pet_shelter_repository = PetRepository(self.db)

        return pet_shelter_repository.get_all_by_pet_shelter_id(pet_shelter_id)
