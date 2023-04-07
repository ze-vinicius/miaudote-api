from app.modules.pet_shelter.repositories.pet_shelter import (
    PetShelterRepository,
)
from sqlalchemy.orm import Session


class GetAllPetSheltersService:
    def __init__(self, db: Session):
        self.db = db

    def execute(self):
        pet_shelter_repository = PetShelterRepository(self.db)

        return pet_shelter_repository.get_all()
