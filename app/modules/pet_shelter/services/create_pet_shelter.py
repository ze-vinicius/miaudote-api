from typing import Optional

from databases import Database

from app.modules.auth.repositories.account import AccountRepository
from app.modules.auth.schemas import AccountIn
from app.modules.pet_shelter.exceptions import (
    AccountNotCreated,
    PetShelterAlreadyExists,
)
from app.modules.pet_shelter.repositories.address import AddressRepository
from app.modules.pet_shelter.repositories.pet_shelter import PetShelterRepository
from app.modules.pet_shelter.schemas.address import AddressInDb
from app.modules.pet_shelter.schemas.address.address import Address
from app.modules.pet_shelter.schemas.pet_shelter import (
    PetShelter,
    PetShelterIn,
    PetShelterInDb,
)
from app.utils.hash import Hash


class CreatePetShelterService:
    def __init__(self, db: Database):
        self.db = db
        self.pet_shelter_repository = PetShelterRepository(db)
        self.address_repository = AddressRepository(db)
        self.account_respository = AccountRepository(db)

    async def delete_created_pet_shelter(
        self,
        pet_shelter_id: Optional[int] = None,
        account_id: Optional[int] = None,
        address_id: Optional[int] = None,
    ):
        if address_id:
            await self.address_repository.delete_one_by_id(address_id)
        if pet_shelter_id:
            await self.pet_shelter_repository.delete_one_by_id(pet_shelter_id)
        if account_id:
            await self.account_respository.delete_one_by_id(account_id)

    async def execute(self, pet_shelter: PetShelterIn):
        alreadyExists = await self.account_respository.get_one_by_username(
            pet_shelter.email
        )

        if alreadyExists:
            raise PetShelterAlreadyExists()

        account_payload = AccountIn(
            username=pet_shelter.email,
            password=Hash.encrypt(pet_shelter.password),
        )

        created_account = await self.account_respository.create(account_payload)

        if not created_account:
            raise AccountNotCreated()

        create_pet_shelter_payload = PetShelterInDb(
            owner_id=created_account["id"],
            description=pet_shelter.description,
            email=pet_shelter.email,
            name=pet_shelter.name,
            phone=pet_shelter.phone,
            instagram_address=pet_shelter.instagram_address,
            facebook_address=pet_shelter.instagram_address,
            twitter_address=pet_shelter.twitter_address,
        )

        created_pet_shelter = await self.pet_shelter_repository.create(
            create_pet_shelter_payload
        )

        if not created_pet_shelter:
            await self.delete_created_pet_shelter(account_id=created_account["id"])
            raise AccountNotCreated()

        create_address_payload = AddressInDb(
            city=pet_shelter.address.city,
            state=pet_shelter.address.state,
            country=pet_shelter.address.country,
            street_address=pet_shelter.address.street_address,
            zip_code=pet_shelter.address.zip_code,
            pet_shelter_id=created_pet_shelter["id"],
        )

        created_address = await self.address_repository.create(create_address_payload)

        if not created_address:
            await self.delete_created_pet_shelter(
                pet_shelter_id=created_pet_shelter["id"],
                account_id=created_account["id"],
            )
            raise AccountNotCreated()

        return PetShelter(
            id=created_pet_shelter._mapping["id"],
            name=created_pet_shelter._mapping["name"],
            description=created_pet_shelter._mapping["description"],
            email=created_pet_shelter._mapping["email"],
            phone=created_pet_shelter._mapping["phone"],
            facebook_address=created_pet_shelter._mapping["facebook_address"],
            instagram_address=created_pet_shelter._mapping["instagram_address"],
            twitter_address=created_pet_shelter._mapping["twitter_address"],
            owner_id=created_pet_shelter._mapping["owner_id"],
            address=Address(
                id=created_address._mapping["id"],
                city=created_address._mapping["city"],
                country=created_address._mapping["country"],
                state=created_address._mapping["state"],
                street_address=created_address._mapping["street_address"],
                zip_code=created_address._mapping["zip_code"],
                pet_shelter_id=created_address._mapping["pet_shelter_id"],
            ),
        )
