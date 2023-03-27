from pydantic import BaseModel


class AccountBase(BaseModel):
    username: str


class AccountCreate(AccountBase):
    password: str


class AccountAuth(AccountCreate):
    pass


class AccountInDbBase(AccountBase):
    id: int

    class Config:
        orm_mode = True


class Account(AccountInDbBase):
    pass
