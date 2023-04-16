from sqlalchemy.orm import Mapped, mapped_column

from ....db.base import Base


class AccountModel(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    username: Mapped[str]
    password: Mapped[str]
