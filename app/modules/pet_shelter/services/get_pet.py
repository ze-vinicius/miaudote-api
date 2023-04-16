from databases import Database

from app.modules.pet_shelter.exceptions import PetNotFound
from app.modules.pet_shelter.repositories.pet import PetRepository
from app.modules.pet_shelter.schemas.pet import Pet


class GetPetService:
    def __init__(self, db: Database) -> None:
        self.db = db

    async def execute(self, pet_id: int):
        pet_repository = PetRepository(self.db)

        record = await pet_repository.get_one_by_id(pet_id)

        if record is None:
            raise PetNotFound()

        return Pet.from_record(record)
