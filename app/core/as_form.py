from typing import Type
from fastapi import Form

from pydantic import BaseModel


def as_form(cls: Type[BaseModel]):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls
