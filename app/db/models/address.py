from typing import Optional
from ..base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class AddressModel(Base):
  __tablename__ = 'addresses'

  id: Mapped[int] = mapped_column(primary_key=True, index=True)

  city: Mapped[str]
  country: Mapped[str]
  state: Mapped[str]
  street_address: Mapped[Optional[str]]
  zip_code: Mapped[Optional[str]]

  pet_shelter_id: Mapped[int] = mapped_column(ForeignKey("pet_shelters.id"), nullable=False)