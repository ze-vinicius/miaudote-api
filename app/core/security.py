from datetime import datetime, timedelta
from typing import Optional

from jose import jwt

from app.core.config import settings


def create_access_token(data: dict, expires_in: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_in:
        expire = datetime.utcnow() + expires_in
    else:
        expire = datetime.utcnow() + timedelta(weeks=99)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )

    return encoded_jwt
