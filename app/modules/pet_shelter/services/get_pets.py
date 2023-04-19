from databases import Database
from app.core.pagination import Pagination

from app.modules.pet_shelter.repositories.pet import PetRepository
from app.modules.pet_shelter.schemas.pet import Pet


class GetPetsService:
    def __init__(self, db: Database):
        self.db = db

    async def execute(self, skip: int = 0, limit: int = 20):
        pet_repository = PetRepository(self.db)

        records = await pet_repository.get_all(skip=skip, limit=limit)
        total = await pet_repository.count_pets()

        pets = Pet.from_record(records)
        
        result = Pagination(skip=skip, limit=limit, total=total, items=pets)

        return result
