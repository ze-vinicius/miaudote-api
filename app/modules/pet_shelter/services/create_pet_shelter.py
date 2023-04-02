from fastapi import HTTPException
from app.modules.auth.repositories.account import AccountRepository
from app.modules.pet_shelter.repositories.address import AddressRepository
from app.modules.pet_shelter.repositories.pet_shelter import PetShelterRepository
from app.modules.auth.schemas.account import AccountCreate
from app.modules.pet_shelter.schemas.address import AddressInDb
from app.modules.pet_shelter.schemas.pet_shelter import (
    PetShelterIn,
    PetShelter,
    PetShelterInDb
)
from sqlalchemy.orm import Session

from app.utils.hash import Hash


class CreatePetShelterService:
    def __init__(self, db: Session):
        self.db = db

    def execute(self, pet_shelter: PetShelterIn):
        pet_shelter_repository = PetShelterRepository(self.db)
        address_repository = AddressRepository(self.db)

        account_respository = AccountRepository(self.db)

        alreadyExists = account_respository.get_one_by_username(
            pet_shelter.email)

        if alreadyExists:
            raise HTTPException(
                status_code=400, detail="pet_shelters.create.error.user_already_exists")

        account_payload = AccountCreate(
            username=pet_shelter.email, password=Hash().encrypt(pet_shelter.password))

        created_account = account_respository.create(account_payload)

        if not created_account.id:
            raise HTTPException(
                status_code=400, detail="pet_shelters.create.error.unknown_error")

        create_pet_shelter_payload = PetShelterInDb(
            account_id=created_account.id,
            description=pet_shelter.description,
            email=pet_shelter.email,
            name=pet_shelter.name,
            phone=pet_shelter.phone,
            instagram_address=pet_shelter.instagram_address,
            facebook_address=pet_shelter.instagram_address,
            twitter_address=pet_shelter.twitter_address,
        )

        created_pet_shelter = pet_shelter_repository.create(
            create_pet_shelter_payload)

        create_address_payload = AddressInDb(
            city=pet_shelter.address.city,
            state=pet_shelter.address.state,
            country=pet_shelter.address.country,
            street_address=pet_shelter.address.street_address,
            zip_code=pet_shelter.address.zip_code,
            pet_shelter_id=created_pet_shelter.id,
        )

        address_repository.create(create_address_payload)

        print(created_pet_shelter)

        return PetShelter.from_orm(created_pet_shelter)
