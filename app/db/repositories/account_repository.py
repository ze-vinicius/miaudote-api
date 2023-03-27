from sqlalchemy.orm.session import Session
from app.db.models.account import AccountModel
from app.db.repositories.base import BaseRepository

from app.schemas.account import AccountCreate

class AccountRepository(BaseRepository):
  def create(self, payload: AccountCreate):
    new_account = AccountModel(
      username = payload.username,
      password = payload.password
    )

    self.db.add(new_account)
    self.db.commit()
    self.db.refresh(new_account)

    return new_account

  def get_one_by_username(self, username: str):
    account = self.db.query(AccountModel).where(AccountModel.username == username).first()

    return account