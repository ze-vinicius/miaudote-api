from enum import Enum
from pydantic import BaseModel

class PetSize(str, Enum):
    SMALL = "SMALL"
    MID = "MID"
    LARGE = "LARGE"


class PetAge(str, Enum):
    LESS_THAN_ONE = "LESS_THAN_ONE"
    BETWEEN_ONE_AND_SEVEN = "BETWEEN_ONE_AND_SEVEN"
    GREATHER_THAN_SEVEN = "GREATHER_THAN_SEVEN"


class PetSpecies(str, Enum):
    CAT = "CAT"
    DOG = "DOG"


class PetSex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class PetTemper(str, Enum):
    SHY = "SHY" 
    DOCILE = "DOCILE" 
    AGGRESSIVE = "AGGRESSIVE"

class AdoptionStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    ADOPTED = "ADOPTED"

class HealthStatus(str, Enum):
    HEALTHY = "HEALTHY"
    SICK = "SICK"
    INJURIED = "INJURIED"
    DEAD = "DEAD"

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
    