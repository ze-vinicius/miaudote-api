import pytest
from app.core.dependencies import get_current_account_from_token
from app.main import app
from app.modules.auth.schemas.account import Account
from app.modules.pet_shelter.repositories.pet_shelter import PetShelterRepository
from app.modules.pet_shelter.schemas.pet.enums import AdoptionStatus, Age, HealthStatus, Sex, Size, Species, Temper
from app.modules.pet_shelter.schemas.pet.pet_in import PetIn
from app.modules.pet_shelter.schemas.pet_shelter import PetShelterIn, PetShelter
from app.modules.pet_shelter.services.create_pet import CreatePetService
from app.modules.pet_shelter.services.create_pet_shelter import CreatePetShelterService

pet_shelter_in_complete = {
    "name": "Shelter Test",
    "phone": "+55123451234",
    "email": "shelter_test@email.com",
    "password": "12345678",
    "description": "Just a shelter trying to test this app",
    "instagram_address": "http://instagram.com/shelter_test",
    "twitter_address": "http://twitter.com/shelter_test",
    "facebook_address": "http://facebook.com/shelte_test",
    "address": {
        "street_address": "Some street",
        "city": "Some City",
        "state": "Some State",
        "country": "Some Country",
        "zip_code": "1234567",
    },
}


def test_create_pet_shelter_success(client):
    response = client.post("/pet_shelters/", json=pet_shelter_in_complete)

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == "shelter_test@email.com"
    assert data["name"] == "Shelter Test"


def test_create_pet_shelter_duplicate_username(client):
    response = client.post("/pet_shelters/", json=pet_shelter_in_complete)

    response = client.post("/pet_shelters", json=pet_shelter_in_complete)

    assert response.status_code == 400
    data = response.json()

    assert data["detail"] == "a_pet_shelter_with_this_email_already_exists"


def test_get_pet_shelters(client, pet_shelter):
    response = client.get("/pet_shelters/")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1


def test_get_pet_shelter_success(client, pet_shelter):
    response = client.get("/pet_shelters/1")

    data = response.json()

    assert data["email"] == pet_shelter.email


def test_get_pet_shelter_not_found(client):
    response = client.get("/pet_shelters/1")

    data = response.json()

    assert response.status_code == 404
    assert data["detail"] == "pet_shelter_not_found"


def test_create_pet_success(client, pet_shelter: PetShelter):
    def override_get_current_account_from_token():
        return Account(id=1, username="test_shelter@email.com")

    app.dependency_overrides[get_current_account_from_token] = override_get_current_account_from_token

    pet_in_complete = {
        "name": "Cute Pet Name",
        "description": "It's a cute female and healthy cat",
        "age": "LESS_THAN_ONE",
        "species": "CAT",
        "sex": "FEMALE",
        "size": "SMALL",
        "temper": "SHY",
        "health_status": "HEALTHY",
        "adoption_status": "AVAILABLE",
    }

    response = client.post("/pets/", data=pet_in_complete)

    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Cute Pet Name"


def test_get_pets_from_pet_shelter_success(client, pet_shelter, pet):
    response = client.get(f"/pet_shelters/{pet_shelter.id}/pets")

    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1


def test_get_pet_success(client, pet):
    response = client.get("/pets/1")

    data = response.json()

    assert response.status_code == 200
    assert data["name"] == pet.name


def test_get_pet_not_found(client):
    response = client.get("/pets/1")

    data = response.json()

    assert response.status_code == 404
    assert data["detail"] == "pet_not_found"
