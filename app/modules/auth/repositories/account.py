from sqlalchemy import Column, DateTime, Identity, Integer, String, Table, func

from app.core.database import metadata
from app.modules.auth.schemas import AccountIn
from app.utils.base_repository import BaseRepository

accounts_table = Table(
    "accounts",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=True),
)


class AccountRepository(BaseRepository):
    async def create(self, account_in: AccountIn):
        query = (
            accounts_table.insert()
            .values(**account_in.dict())
            .returning(accounts_table)
        )

        return await self.db.fetch_one(query)

    async def get_one_by_username(self, username: str):
        query = accounts_table.select().where(accounts_table.c.username == username)

        return await self.db.fetch_one(query)

    async def delete_one_by_id(self, id: int):
        query = accounts_table.delete().where(accounts_table.c.id == id)

        return await self.db.fetch_one(query)
