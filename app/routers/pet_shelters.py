from fastapi import APIRouter, Depends, HTTPException, Request
from app.db.base import get_db
from app.db.repositories.pet_shelter_repository import PetShelterRepository
# from app.services.pet_shelter_service import CreatePetShelterParams, PetShelterService
from app.services.pet_shelter.get_all_pet_shelters import GetAllPetSheltersService
from app.services.pet_shelter.create_pet_shelter import CreatePetShelterService, CreatePetShelterParams
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/pet_shelters",
    tags=["pet_shelters"],
    responses={404: {"description": "Not Found"}},
)

fake_pet_shelters = {
    "1": {
        "id": "1",
        "name": "Marabichos"
    },
}


@router.get('/')
async def read_pet_shelters(db: Session = Depends(get_db)):
    pet_shelter_service = GetAllPetSheltersService(db)

    pet_shelters = pet_shelter_service.execute()

    return pet_shelters


@router.get('/{pet_shelter_id}')
async def read_pet_shelter(pet_shelter_id: str):
    if pet_shelter_id not in fake_pet_shelters:
        raise HTTPException(stauts_code=404, detail="pet.not.found")

    return fake_pet_shelters[pet_shelter_id]

@router.post('/')
async def create_pet_shelter(pet_shelter: CreatePetShelterParams, db: Session = Depends(get_db)):
    pet_shelter_service = CreatePetShelterService(db)

    created_pet_shelter = pet_shelter_service.execute(pet_shelter)

    return created_pet_shelter
    

