from pydantic import BaseModel


class AccountIn(BaseModel):
    username: str
    password: str
