from typing import List, Optional
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from app.core.dependencies import get_current_account_from_token
from app.db.base import get_db
from app.modules.auth.schemas.account import Account
from app.modules.pet_shelter.schemas.pet import PetIn
from app.modules.pet_shelter.schemas.pet_shelter import PetShelterIn
from app.modules.pet_shelter.services.create_pet import CreatePetService
from app.modules.pet_shelter.services.get_all_pets_from_pet_shelter import GetAllPetsFromPetShelter
from app.modules.pet_shelter.services.get_all_pet_shelters import GetAllPetSheltersService
from app.modules.pet_shelter.services.create_pet_shelter import CreatePetShelterService
from sqlalchemy.orm import Session

from app.modules.pet_shelter.services.get_pet_shelter import GetPetShelterService

router = APIRouter(
    tags=["pet_shelters", "pets"],
    responses={404: {"description": "Not Found"}},
)


@router.get("/pet_shelters")
def read_pet_shelters(db: Session = Depends(get_db)):
    pet_shelter_service = GetAllPetSheltersService(db)

    pet_shelters = pet_shelter_service.execute()

    return pet_shelters


@router.post("/pet_shelters")
def create_pet_shelter(pet_shelter_form: PetShelterIn, db: Session = Depends(get_db)):
    pet_shelter_service = CreatePetShelterService(db)

    created_pet_shelter = pet_shelter_service.execute(pet_shelter_form)

    return created_pet_shelter


@router.get("/pet_shelters/{pet_shelter_id}/pets")
def get_all_pets_by_pet_shelter(pet_shelter_id: str, db: Session = Depends(get_db)):
    get_all_pets_by_pet_shelter_service = GetAllPetsFromPetShelter(db)

    return get_all_pets_by_pet_shelter_service.execute(pet_shelter_id)


@router.get("/pet_shelters/{pet_shelter_id}")
def read_pet_shelter(pet_shelter_id: str, db: Session = Depends(get_db)):
    get_pet_shelter_service = GetPetShelterService(db)

    return get_pet_shelter_service.execute(pet_shelter_id)


@router.post("/pets")
def create_pet(
    pet_form: PetIn = Depends(PetIn.as_form),
    profile_picture: UploadFile = File(None),
    current_account: Account = Depends(get_current_account_from_token),
    db: Session = Depends(get_db),
):
    create_pet_service = CreatePetService(db)

    pet = create_pet_service.execute(
        pet_form=pet_form, profile_picture=profile_picture, account=current_account)

    return pet
