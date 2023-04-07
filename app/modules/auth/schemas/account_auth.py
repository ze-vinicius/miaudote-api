from pydantic import BaseModel, EmailStr


class AccountAuth(BaseModel):
    username: EmailStr
    password: str
