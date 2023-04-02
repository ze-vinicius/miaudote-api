from fastapi import HTTPException
from sqlalchemy.orm.session import Session

from app.modules.pet_shelter.repositories.pet_shelter import PetShelterRepository
from app.modules.pet_shelter.schemas.pet_shelter.pet_shelter import PetShelter


class GetPetShelterService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def execute(self, pet_shelter_id: int):
        pet_shelter_repository = PetShelterRepository(self.db)

        pet_shelter = pet_shelter_repository.get_one_by_id(pet_shelter_id)

        if pet_shelter is None:
            raise HTTPException(
                status_code=404, detail='pet_shelters.error.pet_shelter_not_found')

        return PetShelter.from_orm(pet_shelter)
