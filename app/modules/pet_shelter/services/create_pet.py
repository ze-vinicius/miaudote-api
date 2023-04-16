from typing import Optional

from databases import Database
from fastapi import UploadFile

from app.core.upload_file import upload_file
from app.modules.auth.schemas.account import Account
from app.modules.pet_shelter.exceptions import PetShelterNotFound
from app.modules.pet_shelter.repositories.pet import PetRepository
from app.modules.pet_shelter.repositories.pet_shelter import PetShelterRepository
from app.modules.pet_shelter.schemas import Pet, PetIn, PetInDb


class CreatePetService:
    def __init__(self, db: Database):
        self.db = db
        self.pet_repository = PetRepository(self.db)
        self.pet_shelter_repository = PetShelterRepository(self.db)

    async def execute(
        self,
        pet_in: PetIn,
        profile_picture: Optional[UploadFile],
        account: Account,
    ):
        profile_picture_name = None

        if profile_picture:
            profile_picture_name = upload_file(file=profile_picture)

        pet_shelter = await self.pet_shelter_repository.get_one_by_owner_id(account.id)

        if not pet_shelter:
            raise PetShelterNotFound()

        created_pet = await self.pet_repository.create(
            PetInDb(
                **pet_in.dict(),
                profile_picture=profile_picture_name if profile_picture_name else None,
                pet_shelter_id=pet_shelter["id"],
            )
        )

        pet = Pet.from_record(created_pet)
        return pet
