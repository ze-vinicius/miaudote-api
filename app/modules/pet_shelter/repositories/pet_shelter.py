from app.modules.pet_shelter.models.pet_shelter import PetShelterModel
from app.utils.base_repository import BaseRepository

from app.modules.pet_shelter.schemas.pet_shelter import PetShelterCreate


class PetShelterRepository(BaseRepository):
    def create(self, payload: PetShelterCreate):
        new_pet_shelter = PetShelterModel(
            name=payload.name,
            email=payload.email,
            phone=payload.phone,
            description=payload.description,
            instagram_address=payload.instagram_address,
            facebook_address=payload.facebook_address,
            twitter_address=payload.twitter_address,
            account_id=payload.account_id,
        )

        self.db.add(new_pet_shelter)
        self.db.commit()
        self.db.refresh(new_pet_shelter)

        return new_pet_shelter

    def get_all(self):
        return self.db.query(PetShelterModel).all()
