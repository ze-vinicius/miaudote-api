from typing import Optional
from fastapi import HTTPException, UploadFile
from app.core.upload_file import upload_file
from app.modules.auth.schemas.account import Account
from app.modules.pet_shelter.repositories.pet import PetRepository
from app.modules.pet_shelter.repositories.pet_shelter import PetShelterRepository
from app.modules.pet_shelter.schemas.pet import PetIn, PetInDb
from sqlalchemy.orm import Session


class CreatePetService:
    def __init__(self, db: Session):
        self.db = db

    def execute(self, pet_form: PetIn, profile_picture: Optional[UploadFile], account: Account):
        profile_picture_name = None

        if profile_picture:
            profile_picture_name = upload_file(file=profile_picture)

        print({profile_picture_name})

        pet_repository = PetRepository(self.db)
        pet_shelter_repository = PetShelterRepository(self.db)

        pet_shelter = pet_shelter_repository.get_one_by_account_id(account.id)

        if not pet_shelter:
            raise HTTPException(status_code=403, detail="pet_shelters.pet_shelter_does_not_exist")

        created_pet = pet_repository.create(
            PetInDb(
                **pet_form.dict(),
                profile_picture=profile_picture_name if profile_picture_name else None,
                pet_shelter_id=pet_shelter.id,
            )
        )

        return created_pet
