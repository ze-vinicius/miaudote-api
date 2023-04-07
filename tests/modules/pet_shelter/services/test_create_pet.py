import pytest
from app.modules.pet_shelter.exceptions import PetShelterNotFound
from app.modules.pet_shelter.schemas.pet.enums import AdoptionStatus, Age, HealthStatus, Sex, Size, Species, Temper
from app.modules.pet_shelter.schemas.pet.pet_in import PetIn
from app.modules.pet_shelter.services.create_pet import CreatePetService


@pytest.fixture
def create_pet_service(db):
    return CreatePetService(db)


def create_pet_without_profile_picture_success(account, pet_shelter, create_pet_service):
    pet_in = PetIn(
        age=Age.BETWEEN_ONE_AND_SEVEN,
        adoption_status=AdoptionStatus.AVAILABLE,
        description="Some awesome rescued kitten",
        health_status=HealthStatus.HEALTHY,
        name="Kitten",
        sex=Sex.FEMALE,
        size=Size.SMALL,
        species=Species.CAT,
        temper=Temper.DOCILE,
    )

    created_pet = create_pet_service.execute(
        pet_in=pet_in, profile_picture=None, account=account)

    assert created_pet.name == "Kitten"


def create_pet_error_pet_shelter_not_found(account, create_pet_service):
    pet_in = PetIn(
        age=Age.BETWEEN_ONE_AND_SEVEN,
        adoption_status=AdoptionStatus.AVAILABLE,
        description="Some awesome rescued kitten",
        health_status=HealthStatus.HEALTHY,
        name="Kitten",
        sex=Sex.FEMALE,
        size=Size.SMALL,
        species=Species.CAT,
        temper=Temper.DOCILE,
    )

    with pytest.raises(PetShelterNotFound) as exception:
        create_pet_service.execute(
            pet_in=pet_in, profile_picture=None, account=account)

    assert exception.value.status_code == 404
    assert exception.value.detail == 'pet_shelter_not_found'
