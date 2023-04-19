from typing import List

from databases import Database
from fastapi import APIRouter, Depends, File, UploadFile

from app.core.database import get_db
from app.core.dependencies import get_current_account_from_token
from app.modules.auth.schemas.account import Account
from app.modules.pet_shelter.schemas.pet import PetIn
from app.modules.pet_shelter.schemas.pet.pet import Pet
from app.modules.pet_shelter.schemas.pet_shelter import PetShelterIn
from app.modules.pet_shelter.schemas.pet_shelter.pet_shelter import PetShelter
from app.modules.pet_shelter.services.create_pet import CreatePetService
from app.modules.pet_shelter.services.create_pet_shelter import CreatePetShelterService
from app.modules.pet_shelter.services.get_all_pet_shelters import (
    GetAllPetSheltersService,
)
from app.modules.pet_shelter.services.get_all_pets_from_pet_shelter import (
    GetAllPetsFromPetShelter,
)
from app.modules.pet_shelter.services.get_pet import GetPetService
from app.modules.pet_shelter.services.get_pet_shelter import GetPetShelterService
from app.modules.pet_shelter.services.get_pets import GetPetsService

router = APIRouter(
    tags=["pet_shelters", "pets"],
    responses={404: {"description": "Not Found"}},
)


@router.get("/pet_shelters", response_model=List[PetShelter])
async def get_pet_shelters(db: Database = Depends(get_db)):
    pet_shelter_service = GetAllPetSheltersService(db)

    pet_shelters = await pet_shelter_service.execute()

    return pet_shelters


@router.post("/pet_shelters", response_model=PetShelter)
async def create_pet_shelter(
    pet_shelter_form: PetShelterIn, db: Database = Depends(get_db)
):
    pet_shelter_service = CreatePetShelterService(db)

    created_pet_shelter = await pet_shelter_service.execute(pet_shelter_form)

    return created_pet_shelter


@router.get("/pet_shelters/{pet_shelter_id}/pets", response_model=List[Pet])
async def get_pets_from_pet_shelter(
    pet_shelter_id: int, db: Database = Depends(get_db)
):
    get_all_pets_by_pet_shelter_service = GetAllPetsFromPetShelter(db)

    pets_from_pet_shelter = await get_all_pets_by_pet_shelter_service.execute(
        pet_shelter_id
    )

    return pets_from_pet_shelter


@router.get("/pet_shelters/{pet_shelter_id}", response_model=PetShelter)
async def get_pet_shelter(pet_shelter_id: int, db: Database = Depends(get_db)):
    get_pet_shelter_service = GetPetShelterService(db)

    pet_shelter = await get_pet_shelter_service.execute(pet_shelter_id)

    return pet_shelter

@router.get("/pets")
async def get_pets(skip: int = 0, limit: int = 20, db: Database = Depends(get_db)):
    service = GetPetsService(db)
    
    pets = await service.execute(skip=skip, limit=limit)

    return pets

@router.post("/pets", response_model=Pet)
async def create_pet(
    pet_in: PetIn = Depends(PetIn.as_form),
    profile_picture: UploadFile = File(None),
    current_account: Account = Depends(get_current_account_from_token),
    db: Database = Depends(get_db),
):
    create_pet_service = CreatePetService(db)

    pet = await create_pet_service.execute(
        pet_in=pet_in, profile_picture=profile_picture, account=current_account
    )

    return pet

@router.get("/pets/{pet_id}", response_model=Pet)
async def get_pet(pet_id: int, db: Database = Depends(get_db)):
    get_pet_service = GetPetService(db)

    pet = await get_pet_service.execute(pet_id)

    return pet


