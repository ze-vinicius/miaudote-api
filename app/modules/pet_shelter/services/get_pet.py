from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from app.modules.pet_shelter.exceptions import PetShelterNotFound

from app.modules.pet_shelter.repositories.pet import PetRepository
from app.modules.pet_shelter.schemas.pet import Pet


class GetPetService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def execute(self, pet_id: int):
        pet_repository = PetRepository(self.db)

        found_pet = pet_repository.get_one_by_id(pet_id)

        if found_pet is None:
            raise PetShelterNotFound()

        return Pet.from_orm(found_pet)
