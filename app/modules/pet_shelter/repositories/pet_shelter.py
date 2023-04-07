from sqlalchemy import delete
from app.modules.pet_shelter.models.pet_shelter import PetShelterModel
from app.utils.base_repository import BaseRepository

from app.modules.pet_shelter.schemas.pet_shelter import PetShelterInDb


class PetShelterRepository(BaseRepository):
    def create(self, payload: PetShelterInDb):
        new_pet_shelter = PetShelterModel(**payload.dict())

        self.db.add(new_pet_shelter)
        self.db.commit()
        self.db.refresh(new_pet_shelter)

        return new_pet_shelter

    def get_all(self):
        return self.db.query(PetShelterModel).all()

    def get_one_by_account_id(self, account_id: int):
        return (
            self.db.query(PetShelterModel)
            .where(PetShelterModel.account_id == account_id)
            .first()
        )

    def get_one_by_id(self, id: int):
        return (
            self.db.query(PetShelterModel)
            .where(PetShelterModel.id == id)
            .first()
        )

    def delete_one_by_id(self, address_id: int):
        stmt = delete(PetShelterModel).where(PetShelterModel.id == address_id)
        self.db.execute(stmt).all()
