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

addresses_table = Table(
    "addresses",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("city", String, nullable=False),
    Column("country", String, nullable=False),
    Column("state", String, nullable=False),
    Column("street_address", String, nullable=True),
    Column("zip_code", String, nullable=True),
    Column("pet_shelter_id", Integer, ForeignKey("pet_shelters.id"), nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=True),
)
