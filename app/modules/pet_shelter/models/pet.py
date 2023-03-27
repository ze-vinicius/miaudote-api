from app.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class PetModel(Base):
  __tablename__ = 'pets'

  id: Mapped[int] = mapped_column(primary_key=True, index=True)

  age: Mapped[str] 
  description: Mapped[str] 
  name: Mapped[str]  
  sex: Mapped[str] 
  size: Mapped[str] 
  species: Mapped[str] 
  temper: Mapped[str] 

  adoption_status: Mapped[str] 
  health_status: Mapped[str] 

  # Relatios
  pet_shelter_id: Mapped[int] = mapped_column(ForeignKey("pet_shelters.id"), nullable=False) 
