from app.db.models import PetModel
from app.schemas import Pet
from sqlalchemy.orm.session import Session

class PetRepository: 
  def __init__(self, db: Session):
    self.db = db

  def create_pet(self, request: Pet):
    new_pet = PetModel(
      name = request.name,
      sex = request.sex,
      size = request.size,
      species = request.species,
      age = request.age,
      description = request.description,
      temper = request.temper,
    )

    self.db.add(new_pet)
    self.db.commit()
    self.db.refresh(new_pet)

    return new_pet

  def get_pets(self):
    return self.db.query(PetModel).all()