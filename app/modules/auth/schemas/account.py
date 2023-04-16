from app.core.models import BaseModel


class Account(BaseModel):
    id: int
    username: str
