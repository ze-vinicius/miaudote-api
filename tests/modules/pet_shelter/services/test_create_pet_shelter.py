from fastapi import HTTPException
from pydantic import EmailStr
import pytest
from app.modules.pet_shelter.exceptions import PetShelterAlreadyExists
from app.modules.pet_shelter.schemas.address.address_in import AddressIn
from app.modules.pet_shelter.schemas.pet_shelter.pet_shelter import PetShelter
from app.modules.pet_shelter.schemas.pet_shelter.pet_shelter_in import PetShelterIn
from app.modules.pet_shelter.services.create_pet_shelter import CreatePetShelterService


@pytest.fixture
def create_pet_shelter_service(db):
    return CreatePetShelterService(db)


def test_create_pet_shelter_success(create_pet_shelter_service):
    pet_shelter_in = PetShelterIn(
        name="Awesome Pet Shelter",
        email=EmailStr("awesome-pet-shelter@email.com"),
        password="12345678",
        phone="+55123451234",
        description="An Awesome description for my pet shelter",
        address=AddressIn(
            street_address="Street Address",
            zip_code="12345678910",
            city="Hidden City",
            state="Hidden State",
            country="Hidden Country",
        ),
    )

    pet_shelter = create_pet_shelter_service.execute(pet_shelter_in)

    assert pet_shelter.email == "awesome-pet-shelter@email.com"


def test_create_pet_shelter_already_exists(create_pet_shelter_service, pet_shelter: PetShelter):
    pet_shelter_in = PetShelterIn(
        name="Awesome Pet Shelter",
        email=EmailStr(pet_shelter.email),
        password="12345678",
        phone="+55123451234",
        description="An Awesome description for my pet shelter",
        address=AddressIn(
            street_address="Street Address",
            zip_code="12345678910",
            city="Hidden City",
            state="Hidden State",
            country="Hidden Country",
        ),
    )

    with pytest.raises(PetShelterAlreadyExists) as exception:
        pet_shelter = create_pet_shelter_service.execute(pet_shelter_in)

    assert exception.value.status_code == 400
