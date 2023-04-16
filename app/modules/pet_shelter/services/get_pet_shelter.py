from databases import Database

from app.modules.pet_shelter.exceptions import PetShelterNotFound
from app.modules.pet_shelter.repositories.pet_shelter import PetShelterRepository
from app.modules.pet_shelter.schemas import PetShelter


class GetPetShelterService:
    def __init__(self, db: Database) -> None:
        self.db = db

    async def execute(self, pet_shelter_id: int):
        pet_shelter_repository = PetShelterRepository(self.db)

        record = await pet_shelter_repository.get_one_by_id(pet_shelter_id)

        if record is None:
            raise PetShelterNotFound()

        pet_shelter = PetShelter.from_record(record)

        return pet_shelter
