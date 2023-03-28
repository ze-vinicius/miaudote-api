from fastapi import HTTPException
from app.modules.auth.schemas.account import Account
from app.modules.pet_shelter.repositories.pet import PetRepository
from app.modules.pet_shelter.repositories.pet_shelter import PetShelterRepository
from app.modules.pet_shelter.schemas.pet import PetBase, PetCreate
from sqlalchemy.orm import Session


class CreatePetService:
    def __init__(self, db: Session):
        self.db = db

    def execute(self, pet: PetBase, account: Account):
        pet_repository = PetRepository(self.db)
        pet_shelter_repository = PetShelterRepository(self.db)

        pet_shelter = pet_shelter_repository.get_one_by_account_id(account.id)

        if not pet_shelter:
            raise HTTPException(status_code=403, detail="pet_shelters.pet_shelter_does_not_exist")

        created_pet = pet_repository.create(
            PetCreate(
                age=pet.age,
                description=pet.description,
                name=pet.name,
                sex=pet.sex,
                size=pet.size,
                species=pet.species,
                temper=pet.temper,
                adoption_status=pet.adoption_status,
                health_status=pet.health_status,
                pet_shelter_id=pet_shelter.id,
            )
        )

        return created_pet
