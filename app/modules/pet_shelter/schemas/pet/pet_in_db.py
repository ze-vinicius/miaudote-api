
from typing import Optional
from pydantic import BaseModel

from app.modules.pet_shelter.schemas.pet.enums import AdoptionStatus, Age, HealthStatus, Sex, Size, Species, Temper


class PetInDb(BaseModel):
    pet_shelter_id: int
    age: Age
    description: Optional[str]
    name: str
    sex: Sex
    size: Size
    species: Species
    temper: Temper
    profile_picture: Optional[str]

    health_status: HealthStatus
    adoption_status: AdoptionStatus

