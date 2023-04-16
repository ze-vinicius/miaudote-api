from databases import Database
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.core.config import settings
from app.core.database import get_db
from app.modules.auth.repositories.account import AccountRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")

from app.modules.auth.schemas import Account


async def get_current_account_from_token(
    token: str = Depends(oauth2_scheme), db: Database = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="sessions.invalid_token",
    )

    account_repository = AccountRepository(db)

    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    record = await account_repository.get_one_by_username(username)

    if record is None:
        raise credentials_exception

    return Account.from_record(record)
