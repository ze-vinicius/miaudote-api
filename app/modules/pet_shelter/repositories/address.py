from app.modules.pet_shelter.models.address import AddressModel
from app.utils.base_repository import BaseRepository

from app.modules.pet_shelter.schemas.address import AddressInDb


class AddressRepository(BaseRepository):
    def create(self, payload: AddressInDb):
        new_address = AddressModel(
            **payload.dict()
        )

        self.db.add(new_address)
        self.db.commit()
        self.db.refresh(new_address)

        return new_address
