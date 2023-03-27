from fastapi import HTTPException
from app.db.repositories.account_repository import AccountRepository
from app.db.repositories.address_repository import AddressRepository
from app.db.repositories.pet_shelter_repository import PetShelterRepository
from app.schemas.account import AccountCreate
from app.schemas.address import AddressBase, AddressCreate
from app.schemas.pet_shelter import PetShelter, PetShelterBase, PetShelterCreate
from sqlalchemy.orm import Session

from app.utils.hash import Hash

class CreatePetShelterParams(PetShelterBase):
  password: str
  address: AddressBase


class CreatePetShelterService:
  def __init__(self, db: Session):
    self.db = db

  def execute(self, pet_shelter: CreatePetShelterParams):
    pet_shelter_repository = PetShelterRepository(self.db)
    address_repository = AddressRepository(self.db)
    account_respository = AccountRepository(self.db)

    alreadyExists = account_respository.get_one_by_username(pet_shelter.email)

    if (alreadyExists):
      raise HTTPException(status_code=400, detail='pet_shelters.create.error.user_already_exists')
    
    account_payload = AccountCreate(username=pet_shelter.email, password=Hash().encrypt(pet_shelter.password))
    
    created_account = account_respository.create(account_payload)

    
    if not created_account.id:
      raise HTTPException(status_code=400, detail="pet_shelters.create.error.unknown_error")

    create_pet_shelter_payload = PetShelterCreate(
      account_id=created_account.id,
      description=pet_shelter.description,
      email=pet_shelter.email,
      name=pet_shelter.name,
      phone=pet_shelter.phone,
      instagram_address=pet_shelter.instagram_address,
      facebook_address=pet_shelter.instagram_address,
      twitter_address=pet_shelter.twitter_address,
    )

    created_pet_shelter = pet_shelter_repository.create(create_pet_shelter_payload)

    create_address_payload = AddressCreate(
        city=pet_shelter.address.city,
        state=pet_shelter.address.state,
        country=pet_shelter.address.country,
        street_address=pet_shelter.address.street_address,
        zip_code=pet_shelter.address.zip_code,
        pet_shelter_id=created_pet_shelter.id
       )
    
    created_address = address_repository.create(create_address_payload)

    print(created_pet_shelter)

    response = {
      "id":created_pet_shelter.id,
      "description":created_pet_shelter.description,
      "email":created_pet_shelter.email,
      "name":created_pet_shelter.name,
      "phone":created_pet_shelter.phone,
      "instagram_address":created_pet_shelter.instagram_address,
      "facebook_address":created_pet_shelter.instagram_address,
      "twitter_address":created_pet_shelter.twitter_address,
      "address": created_address
    }

    return response



