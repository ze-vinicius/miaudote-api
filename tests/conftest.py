from fastapi.testclient import TestClient
from sqlalchemy import create_engine
import pytest
from sqlalchemy.orm import Session, sessionmaker
from app.main import app

from app.db.base import Base, get_db
from app.modules.auth.repositories.account import AccountRepository
from app.modules.auth.schemas.account import AccountCreate
from app.modules.pet_shelter.repositories.address import AddressRepository
from app.modules.pet_shelter.repositories.pet import PetRepository
from app.modules.pet_shelter.repositories.pet_shelter import PetShelterRepository
from app.modules.pet_shelter.router import create_pet_shelter
from app.modules.pet_shelter.schemas.address.address_in_db import AddressInDb
from app.modules.pet_shelter.schemas.pet.enums import AdoptionStatus, Age, HealthStatus, Sex, Size, Species, Temper
from app.modules.pet_shelter.schemas.pet.pet_in_db import PetInDb
from app.modules.pet_shelter.schemas.pet_shelter.pet_shelter import PetShelter
from app.modules.pet_shelter.schemas.pet_shelter.pet_shelter_in import PetShelterIn
from app.modules.pet_shelter.schemas.pet_shelter.pet_shelter_in_db import PetShelterInDb

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    Base.metadata.create_all(bind=engine)

    yield engine

    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()

    Session = sessionmaker(bind=connection)
    db = Session()

    yield db

    db.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(db):
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as c:
        yield c


@pytest.fixture
def account(db):
    account_repository = AccountRepository(db)

    created_account = account_repository.create(AccountCreate(username="pet_shelter@email.com", password="12345678"))

    return created_account


@pytest.fixture
def pet_shelter(db, account):
    pet_shelter_repository = PetShelterRepository(db)
    address_repository = AddressRepository(db)

    pet_shelter_in_dict = {
        "name": "Shelter Test",
        "phone": "+55123451234",
        "email": account.username,
        "description": "Just a shelter trying to test this app",
        "instagram_address": "http://instagram.com/shelter_test",
        "twitter_address": "http://twitter.com/shelter_test",
        "facebook_address": "http://facebook.com/shelte_test",
        "account_id": account.id,
    }

    created_pet_shelter = pet_shelter_repository.create(PetShelterInDb(**pet_shelter_in_dict))

    address_in_dict = {
        "street_address": "Some street",
        "city": "Some City",
        "state": "Some State",
        "country": "Some Country",
        "zip_code": "1234567",
        "pet_shelter_id": created_pet_shelter.id,
    }

    address_repository.create(AddressInDb(**address_in_dict))

    return PetShelter.from_orm(created_pet_shelter)


@pytest.fixture
def pet(db, pet_shelter):
    pet_repository = PetRepository(db)
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

    created_pet = pet_repository.create(pet_in)

    return created_pet
