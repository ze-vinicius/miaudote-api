from typing import Dict, Optional

from pydantic import root_validator

from app.core.config import settings
from app.core.models import BaseModel

from .enums import AdoptionStatus, Age, HealthStatus, Sex, Size, Species, Temper


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

    profile_picture_url: Optional[str]

    @root_validator
    def compute_profile_picture_url(cls: BaseModel, values: Dict) -> Dict:
        profile_picture = values["profile_picture"]

        values["profile_picture_url"] = (
            f"{settings.BUCKET_ENDPOINT}/{profile_picture}" if profile_picture else None
        )

        return values
