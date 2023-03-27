from enum import Enum
from pydantic import BaseModel

class AccountBase(BaseModel):
  username: str

class AccountCreate(AccountBase):
  password: str

class AccountInDbBase(AccountBase):
  id: int

  class Config:
    orm_mode = True

class Account(AccountInDbBase):
  pass