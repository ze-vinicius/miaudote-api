from ....db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class AccountModel(Base):
  __tablename__ = 'accounts'

  id: Mapped[int] = mapped_column(primary_key=True, index=True)
  
  username: Mapped[str]
  password: Mapped[str]