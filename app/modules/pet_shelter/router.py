from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import get_current_account_from_token
from app.db.base import get_db
from app.modules.auth.schemas.account import Account
from app.modules.pet_shelter.schemas.pet import PetBase
from app.modules.pet_shelter.services.create_pet import CreatePetService
from app.modules.pet_shelter.services.get_all_pets_from_pet_shelter import GetAllPetsFromPetShelter
from app.modules.pet_shelter.services.get_all_pet_shelters import GetAllPetSheltersService
from app.modules.pet_shelter.services.create_pet_shelter import CreatePetShelterService, CreatePetShelterParams
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/pet_shelters",
    tags=["pet_shelters", "pets"],
    responses={404: {"description": "Not Found"}},
)

fake_pet_shelters = {
    "1": {"id": "1", "name": "Marabichos"},
}


@router.get("/")
def read_pet_shelters(db: Session = Depends(get_db)):
    pet_shelter_service = GetAllPetSheltersService(db)

    pet_shelters = pet_shelter_service.execute()

    return pet_shelters


@router.post("/")
def create_pet_shelter(pet_shelter: CreatePetShelterParams, db: Session = Depends(get_db)):
    pet_shelter_service = CreatePetShelterService(db)

    created_pet_shelter = pet_shelter_service.execute(pet_shelter)

    return created_pet_shelter


@router.get("/{pet_shelter_id}/pets")
def get_all_pets_by_pet_shelter(pet_shelter_id: str, db: Session = Depends(get_db)):
    get_all_pets_by_pet_shelter_service = GetAllPetsFromPetShelter(db)

    return get_all_pets_by_pet_shelter_service.execute(pet_shelter_id)


@router.get("/{pet_shelter_id}")
def read_pet_shelter(pet_shelter_id: str):
    if pet_shelter_id not in fake_pet_shelters:
        raise HTTPException(stauts_code=404, detail="pet.not.found")

    return fake_pet_shelters[pet_shelter_id]


@router.post("/pets")
def create_pet(
    pet: PetBase, current_account: Account = Depends(get_current_account_from_token), db: Session = Depends(get_db)
):
    create_pet_service = CreatePetService(db)

    pet = create_pet_service.execute(pet=pet, account=current_account)

    return pet
