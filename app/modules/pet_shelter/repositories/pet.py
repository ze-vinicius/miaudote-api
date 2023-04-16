from sqlalchemy import insert, select

from app.modules.pet_shelter.models import pets_table
from app.modules.pet_shelter.schemas.pet import PetInDb
from app.utils.base_repository import BaseRepository


class PetRepository(BaseRepository):
    async def create(self, pet_in: PetInDb):
        query = insert(pets_table).values(**pet_in.dict()).returning(pets_table)

        return await self.db.fetch_one(query)

    async def get_all(self):
        query = select(pets_table)

        result = await self.db.fetch_all(query)

        return result

    async def get_all_by_pet_shelter_id(self, pet_shelter_id: int):
        query = select(pets_table).where(pets_table.c.pet_shelter_id == pet_shelter_id)

        return await self.db.fetch_all(query)

    async def get_one_by_id(self, id: int):
        query = select(pets_table).where(pets_table.c.id == id)

        return await self.db.fetch_one(query)
