from typing import Optional
from pydantic import BaseModel, root_validator, validator
from pydantic_computed import Computed, computed

from app.modules.pet_shelter.schemas.pet_shelter import PetShelter
from app.core.config import settings
from .enums import (
    AdoptionStatus,
    Age,
    HealthStatus,
    Sex,
    Size,
    Temper,
    Species,
)


class Pet(BaseModel):
    id: int
    age: Age
    description: Optional[str]
    name: str
    sex: Sex
    size: Size
    species: Species
    temper: Temper
    profile_picture: Optional[str]
    pet_shelter_id: int

    health_status: HealthStatus
    adoption_status: AdoptionStatus

    profile_picture_url: Computed[str]

    @computed("profile_picture_url")
    def compute_profile_picture_url(profile_picture: Optional[str], **kwargs):
        return f"{settings.BUCKET_ENDPOINT}/{profile_picture}" if profile_picture else None

    # @root_validator
    # def compute_profile_picture_url(cls, values):
    #     if values['profile_picture_url'] is None:
    #         profile_picture = values['profile_picture']
    #
    #         profile_picture_url = f"{settings.BUCKET_ENDPOINT}/{profile_picture}"
    #
    #         print({profile_picture_url, values})
    #
    #         values['profile_picture_url'] = profile_picture_url
    #
    #     return values

    class Config:
        orm_mode = True
