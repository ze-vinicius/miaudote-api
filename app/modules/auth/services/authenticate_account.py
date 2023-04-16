from databases import Database

from app.core.security import create_access_token
from app.modules.auth.exceptions import InvalidCredentials
from app.modules.auth.repositories.account import AccountRepository
from app.modules.auth.schemas import Token
from app.modules.auth.schemas.account_auth import AccountAuth
from app.utils.hash import Hash


class AuthenticateAccount:
    def __init__(self, db: Database):
        self.db = db
        self.account_repository = AccountRepository(self.db)

    async def execute(self, account_form: AccountAuth):
        existent_account = await self.account_repository.get_one_by_username(
            account_form.username
        )

        if not existent_account:
            raise InvalidCredentials()

        password_is_valid = Hash.verify(
            hashed_password=existent_account.password,
            plain_password=account_form.password,
        )

        if not password_is_valid:
            raise InvalidCredentials()

        access_token = create_access_token(
            data={
                "sub": existent_account.username,
            }
        )

        return Token(
            access_token=access_token,
            token_type="bearer",
        )
