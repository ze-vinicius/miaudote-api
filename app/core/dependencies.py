from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from app.core.config import settings

from app.db.base import get_db
from app.modules.auth.repositories.account import AccountRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")


def get_current_account_from_token(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="sessions.invalid_token",
    )

    account_repository = AccountRepository(db)

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = account_repository.get_one_by_username(username)

    if user is None:
        raise credentials_exception
    return user
