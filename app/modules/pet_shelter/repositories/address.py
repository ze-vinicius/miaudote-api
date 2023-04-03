from app.modules.pet_shelter.models.address import AddressModel
from app.utils.base_repository import BaseRepository

from app.modules.pet_shelter.schemas.address import AddressInDb
from sqlalchemy import delete


class AddressRepository(BaseRepository):
    def create(self, payload: AddressInDb):
        new_address = AddressModel(
            **payload.dict()
        )

        self.db.add(new_address)
        self.db.commit()
        self.db.refresh(new_address)

        return new_address
    
    def delete_one_by_id(self, address_id: int):
        stmt = (
            delete(AddressModel).where(AddressModel.id == address_id)
        )
        self.db.execute(stmt).all()