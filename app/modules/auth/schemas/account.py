from pydantic import BaseModel


class Account(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
