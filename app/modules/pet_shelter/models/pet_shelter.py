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

pet_shelters_table = Table(
    "pet_shelters",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, nullable=False),
    Column("phone", String, nullable=False),
    Column("description", String, nullable=False),
    Column("profile_picture", String, nullable=True),
    Column("instagram_address", String, nullable=True),
    Column("facebook_address", String, nullable=True),
    Column("twitter_address", String, nullable=True),
    Column("owner_id", Integer, ForeignKey("accounts.id"), nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=True),
)
