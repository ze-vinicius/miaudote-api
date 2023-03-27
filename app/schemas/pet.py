from enum import Enum
from pydantic import BaseModel

class PetSize(str, Enum):
    small = "small"
    mid = "mid"
    large = "large"


class PetAge(str, Enum):
    less_than_one = "less_than_one"
    between_one_and_seven = "between_one_and_seven"
    greater_than_seven = "greater_than_seven"


class PetSpecies(str, Enum):
    cat = "cat"
    dog = "dog"


class PetSex(str, Enum):
    male = "male"
    female = "female"


class PetTemper(str, Enum):
    shy = "shy" 
    docile = "docile" 
    aggressive = "aggressive"

class AdoptionStatus(str, Enum):
    available = "available"
    not_available = "not_available"
    adopted = "adopted"

class HealthStatus(str, Enum):
    healthy = "healthy"
    sick = "sick"
    injured = "injured"
    dead = "dead"

class PetBase(BaseModel):
    age: PetAge
    description: str
    name: str
    sex: PetSex
    size: PetSize
    species: PetSpecies
    temper: PetTemper

    health_status: HealthStatus
    adoption_status: AdoptionStatus

class PetCreate(PetBase):
    pet_shelter_id: int

class PetInDbBase(PetBase):
    id: int
    pet_shelter_id: int

    class Config:
        orm_mode = True

class Pet(PetInDbBase):
    pass
    