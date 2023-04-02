from typing import Optional, Type
from fastapi import Form
from pydantic import BaseModel
from app.modules.pet_shelter.schemas.pet.enums import (
    Age,
    Sex,
    Size,
    Species,
    Temper,
    HealthStatus,
    AdoptionStatus,
)


class PetIn(BaseModel):
    age: Age
    description: Optional[str]
    name: str
    sex: Sex
    size: Size
    species: Species
    temper: Temper
    health_status: HealthStatus
    adoption_status: AdoptionStatus

    @classmethod
    def as_form(
        cls: Type[BaseModel],
        age: Age = Form(),
        description: Optional[str] = Form(None),
        name: str = Form(),
        sex: Sex = Form(),
        size: Size = Form(),
        species: Species = Form(),
        temper: Temper = Form(),
        health_status: HealthStatus = Form(),
        adoption_status: AdoptionStatus = Form(),
    ):
        return cls(
            age=age,
            description=description,
            name=name,
            sex=sex,
            size=size,
            species=species,
            temper=temper,
            health_status=health_status,
            adoption_status=adoption_status,
        )
