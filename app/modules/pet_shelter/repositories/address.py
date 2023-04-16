from app.modules.pet_shelter.models import addresses_table
from app.modules.pet_shelter.schemas.address import AddressInDb
from app.utils.base_repository import BaseRepository


class AddressRepository(BaseRepository):
    async def create(self, address_in: AddressInDb):
        query = (
            addresses_table.insert()
            .values(**address_in.dict())
            .returning(addresses_table)
        )

        return await self.db.fetch_one(query)

    async def delete_one_by_id(self, id: int):
        query = addresses_table.delete().where(addresses_table.c.id == id)

        return await self.db.fetch_one(query)
