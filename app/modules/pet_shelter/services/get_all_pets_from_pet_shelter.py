from databases import Database

from app.modules.pet_shelter.repositories.pet import PetRepository
from app.modules.pet_shelter.schemas.pet import Pet


class GetAllPetsFromPetShelter:
    def __init__(self, db: Database):
        self.db = db

    async def execute(self, pet_shelter_id: int):
        pet_repository = PetRepository(self.db)

        records = await pet_repository.get_all_by_pet_shelter_id(pet_shelter_id)

        pets = Pet.from_record(records)

        return pets
