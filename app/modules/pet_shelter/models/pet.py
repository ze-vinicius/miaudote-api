from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Identity,
    Integer,
    String,
    Table,
    func,
)

from app.core.database import metadata

pets_table = Table(
    "pets",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("age", String, nullable=False),
    Column("name", String, nullable=False),
    Column("description", String, nullable=True),
    Column("sex", String, nullable=False),
    Column("size", String, nullable=False),
    Column("profile_picture", String, nullable=True),
    Column("species", String, nullable=False),
    Column("temper", String, nullable=False),
    Column("adoption_status", String, nullable=False),
    Column("health_status", String, nullable=False),
    Column("pet_shelter_id", Integer, ForeignKey("pet_shelters.id"), nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=True),
)
