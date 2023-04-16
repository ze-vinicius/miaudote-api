from databases import Database

from app.modules.pet_shelter.repositories.pet_shelter import PetShelterRepository
from app.modules.pet_shelter.schemas.pet_shelter import PetShelter


class GetAllPetSheltersService:
    def __init__(self, db: Database):
        self.db = db

    async def execute(self):
        pet_shelter_repository = PetShelterRepository(self.db)

        records = await pet_shelter_repository.get_all()

        pet_shelters = PetShelter.from_record(records)

        return pet_shelters
