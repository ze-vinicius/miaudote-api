from sqlalchemy import delete, insert, select

from app.modules.pet_shelter.models import addresses_table, pet_shelters_table
from app.modules.pet_shelter.schemas.pet_shelter import PetShelterInDb
from app.utils.base_repository import BaseRepository
from app.utils.get_columns_with_prefix_label import get_columns_with_prefix_label


class PetShelterRepository(BaseRepository):
    def _build_query_with_relations(self):
        join = pet_shelters_table.join(
            addresses_table, pet_shelters_table.c.id == addresses_table.c.pet_shelter_id
        )

        query = select(
            [
                pet_shelters_table,
                *get_columns_with_prefix_label("address", addresses_table),
            ]
        ).select_from(join)

        return query

    async def create(self, payload: PetShelterInDb):
        query = (
            insert(pet_shelters_table)
            .values(**payload.dict())
            .returning(pet_shelters_table)
        )

        return await self.db.fetch_one(query)

    async def get_all(self):
        query = self._build_query_with_relations()

        return await self.db.fetch_all(query)

    async def get_one_by_owner_id(self, owner_id: int):
        query = self._build_query_with_relations()

        query = query.where(pet_shelters_table.c.owner_id == owner_id)

        return await self.db.fetch_one(query)

    async def get_one_by_id(self, id: int):
        query = self._build_query_with_relations()
        query = query.where(pet_shelters_table.c.id == id)

        return await self.db.fetch_one(query)

    async def delete_one_by_id(self, id: int):
        query = delete(pet_shelters_table).where(pet_shelters_table.c.id == id)

        return await self.db.fetch_one(query)
