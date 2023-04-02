from app.modules.pet_shelter.models.pet import PetModel
from app.modules.pet_shelter.schemas.pet import PetInDb
from app.utils.base_repository import BaseRepository


class PetRepository(BaseRepository):
    def create(self, request: PetInDb):
        new_pet = PetModel(**request.dict())

        self.db.add(new_pet)
        self.db.commit()
        self.db.refresh(new_pet)

        return new_pet

    def get_all(self):
        return self.db.query(PetModel).all()

    def get_all_by_pet_shelter_id(self, pet_shelter_id: str):
        return self.db.query(PetModel).where(PetModel.pet_shelter_id == pet_shelter_id).all()
