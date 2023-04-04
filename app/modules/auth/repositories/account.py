from sqlalchemy import delete
from sqlalchemy.orm.session import Session
from app.modules.auth.models.account import AccountModel
from app.utils.base_repository import BaseRepository

from app.modules.auth.schemas.account import AccountCreate


class AccountRepository(BaseRepository):
    def create(self, payload: AccountCreate):
        new_account = AccountModel(username=payload.username, password=payload.password)

        self.db.add(new_account)
        self.db.commit()
        self.db.refresh(new_account)

        return new_account

    def get_one_by_username(self, username: str):
        account = self.db.query(AccountModel).where(AccountModel.username == username).first()

        return account

    def delete_one_by_id(self, address_id: int):
        stmt = delete(AccountModel).where(AccountModel.id == address_id)
        self.db.execute(stmt).all()
