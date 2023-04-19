from typing import List, TypeVar, Generic

from pydantic import BaseModel

T = TypeVar("T")

class Pagination(Generic[T], BaseModel):
    skip: int
    limit: int
    total: int
    items: List[T]


