from fastapi import HTTPException
from app.modules.auth.repositories.account import AccountRepository
from app.modules.pet_shelter.exceptions import AccountNotCreated, AlreadyExists
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
        self.pet_shelter_repository = PetShelterRepository(db)
        self.address_repository = AddressRepository(db)
        self.account_respository = AccountRepository(db)

    def delete_created_pet_shelter(self, pet_shelter_id: int = None, account_id: int = None, address_id: int = None):
        self.address_repository.delete_by_id(address_id)
        self.pet_shelter_repository.delete_by_id(pet_shelter_id)
        self.account_respository.delete_by_id(account_id)

    def execute(self, pet_shelter: PetShelterIn):
        alreadyExists = self.account_respository.get_one_by_username(
            pet_shelter.email)

        if alreadyExists:
            raise AlreadyExists()

        account_payload = AccountCreate(
            username=pet_shelter.email, password=Hash().encrypt(pet_shelter.password))

        created_account = self.account_respository.create(account_payload)

        if not created_account.id:
            raise AccountNotCreated()

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

        created_pet_shelter = self.pet_shelter_repository.create(
            create_pet_shelter_payload)
        
        if created_pet_shelter == None or not created_pet_shelter.id:
            self.delete_created_pet_shelter(
                account_id=created_account.id
            )
            raise AccountNotCreated()

        create_address_payload = AddressInDb(
            city=pet_shelter.address.city,
            state=pet_shelter.address.state,
            country=pet_shelter.address.country,
            street_address=pet_shelter.address.street_address,
            zip_code=pet_shelter.address.zip_code,
            pet_shelter_id=created_pet_shelter.id,
        )

        address_created = self.address_repository.create(
            create_address_payload)

        if not address_created.id:
            self.delete_created_pet_shelter(
                pet_shelter_id=created_pet_shelter.id,
                account_id=created_account.id
            )
            raise AccountNotCreated()

        return PetShelter.from_orm(created_pet_shelter)
