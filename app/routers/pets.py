from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.repositories.pet import PetRepository
from app.db.base import get_db
from ..schemas import Pet

router = APIRouter(
    prefix="/pets",
    tags=["pets"],
    responses={404: {"description": "Not Found"}},
)

fake_pets = {
    "1": {
        "id": "1",
        "name": "Zaya"
    },
    "2": {
        "id": "2",
        "name": "Raikou"
    },
    "3": {
        "id": "3",
        "name": "Tai Lung"
    }
}


@router.get('/')
async def read_pets(db: Session = Depends(get_db)):
    pet_repository = PetRepository(db)

    return pet_repository.get_pets()


@router.get('/{pet_id}', response_model=Pet, summary="See the pet profile")
async def read_pet(pet_id: str):
    if pet_id not in fake_pets:
        raise HTTPException(stauts_code=404, detail="pet.not.found")

    return fake_pets[pet_id]
