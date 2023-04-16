import asyncio
import pytest
from app.main import app

from app.core.database import get_db, database
from app.modules.auth.repositories.account import AccountRepository
from app.modules.auth.schemas import AccountIn
from app.modules.auth.schemas.account import Account
from app.modules.pet_shelter.repositories.address import AddressRepository
from app.modules.pet_shelter.repositories.pet import PetRepository
from app.modules.pet_shelter.repositories.pet_shelter import PetShelterRepository
from app.modules.pet_shelter.router import create_pet_shelter
from app.modules.pet_shelter.schemas.address.address_in_db import AddressInDb
from app.modules.pet_shelter.schemas.pet.enums import AdoptionStatus, Age, HealthStatus, Sex, Size, Species, Temper
from app.modules.pet_shelter.schemas.pet.pet import Pet
from app.modules.pet_shelter.schemas.pet.pet_in_db import PetInDb
from app.modules.pet_shelter.schemas.pet_shelter.pet_shelter import PetShelter
from app.modules.pet_shelter.schemas.pet_shelter.pet_shelter_in import PetShelterIn
from app.modules.pet_shelter.schemas.pet_shelter.pet_shelter_in_db import PetShelterInDb
from app.utils.hash import Hash
from async_asgi_testclient import TestClient
import pytest_asyncio


@pytest.fixture(autouse=True, scope="session")
def run_migrations():
    import os

    print("running migrations")
    os.system("alembic upgrade head")

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    
    yield loop

    loop.close()

@pytest_asyncio.fixture
async def client():
    async with TestClient(app) as c:
        yield c


@pytest_asyncio.fixture
async def account():
    account_repository = AccountRepository(database)

    hashed_password = Hash.encrypt("12345678")

    created_account = await account_repository.create(
        AccountIn(username="pet_shelter@email.com", password=hashed_password))

    return Account.from_orm(created_account)


@pytest_asyncio.fixture
async def pet_shelter(account: Account):
    pet_shelter_repository = PetShelterRepository(database)
    address_repository = AddressRepository(database)

    pet_shelter_in_dict = {
        "name": "Shelter Test",
        "phone": "+55123451234",
        "email": account.username,
        "description": "Just a shelter trying to test this app",
        "instagram_address": "http://instagram.com/shelter_test",
        "twitter_address": "http://twitter.com/shelter_test",
        "facebook_address": "http://facebook.com/shelte_test",
        "owner_id": account.id,
    }

    created_pet_shelter = await pet_shelter_repository.create(
        PetShelterInDb(**pet_shelter_in_dict))

    if not created_pet_shelter:
        raise Exception()

    address_in_dict = {
        "street_address": "Some street",
        "city": "Some City",
        "state": "Some State",
        "country": "Some Country",
        "zip_code": "1234567",
        "pet_shelter_id": created_pet_shelter['id'],
    }

    await address_repository.create(AddressInDb(**address_in_dict))

    return PetShelter.from_record(created_pet_shelter)


@pytest_asyncio.fixture
async def pet(pet_shelter: PetShelter):
    pet_repository = PetRepository(database)
    pet_in = PetInDb(
        name="Cute Pet Name",
        description="It's a cute female and healthy cat",
        profile_picture="cute_pet_profile.png",
        age=Age.BETWEEN_ONE_AND_SEVEN,
        species=Species.CAT,
        sex=Sex.FEMALE,
        size=Size.SMALL,
        temper=Temper.SHY,
        health_status=HealthStatus.HEALTHY,
        adoption_status=AdoptionStatus.ADOPTED,
        pet_shelter_id=pet_shelter.id,
    )

    created_pet = await pet_repository.create(pet_in)

    return Pet.from_orm(created_pet)
