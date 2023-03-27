from typing import Optional
from app.modules.auth.models.account import AccountModel
from app.modules.pet_shelter.models.address import AddressModel
from app.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class PetShelterModel(Base):
    __tablename__ = "pet_shelters"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    description: Mapped[str]

    # Social Media
    instagram_address: Mapped[Optional[str]]
    facebook_address: Mapped[Optional[str]]
    twitter_address: Mapped[Optional[str]]

    # Relations
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    account: Mapped["AccountModel"] = relationship()

    address: Mapped["AddressModel"] = relationship()
