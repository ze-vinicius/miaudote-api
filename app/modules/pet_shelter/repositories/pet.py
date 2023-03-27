from app.modules.pet_shelter.models.pet import PetModel
from app.modules.pet_shelter.schemas.pet import PetCreate
from app.utils.base_repository import BaseRepository

class PetRepository(BaseRepository): 
  def create(self, request: PetCreate):
    new_pet = PetModel(
      age = request.age,
      description = request.description,
      name = request.name,
      sex = request.sex,
      size = request.size,
      species = request.species,
      temper = request.temper,
      adoption_status = request.adoption_status,
      health_status = request.health_status,
      pet_shelter_id = request.pet_shelter_id,
    )

    self.db.add(new_pet)
    self.db.commit()
    self.db.refresh(new_pet)

    return new_pet

  def get_all(self):
    return self.db.query(PetModel).all()