import re
from typing import List

from databases.interfaces import Record
from pydantic import BaseModel as PydanticBaseModel
from pydantic.fields import ModelField


def pascal_to_snake_case(name):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


class BaseModel(PydanticBaseModel):
    __abstract__ = True

    class Config:
        orm_mode = True

    @classmethod
    def _transform_record_to_dict(
        cls, record: Record, root_keys: list, joins: dict[str, dict[str, list]] = {}
    ):
        plain_dict = dict(**record._mapping)
        result = {}

        for k in root_keys:
            result[k] = plain_dict.get(k)

        for join_name in joins:
            join_dict = joins[join_name]

            prefixed_fields = join_dict["prefixed_fields"]
            plain_fields = join_dict["plain_fields"]

            values = [plain_dict[prefixed_field] for prefixed_field in prefixed_fields]

            join_dict = dict(zip(plain_fields, values))

            result[join_name] = join_dict

        return result

    @classmethod
    def get_fields_with_prefix(cls):
        snake_case_name = pascal_to_snake_case(cls.__name__)

        return [f"{snake_case_name}_{field}" for field in cls.__fields__.keys()]

    @classmethod
    def fields_keys(cls) -> List[str]:
        return cls.__fields__.keys()

    @classmethod
    def get_field(cls, field) -> ModelField:
        return cls.__fields__[field]

    @classmethod
    def get_root_fields_keys(cls) -> List[str]:
        return [
            field
            for field in cls.fields_keys()
            if not issubclass(cls.get_field(field).type_, PydanticBaseModel)
        ]

    @classmethod
    def get_relation_fields_keys(cls) -> List[str]:
        return [
            field
            for field in cls.fields_keys()
            if issubclass(cls.get_field(field).type_, PydanticBaseModel)
        ]

    @classmethod
    def from_record(cls, records: List[Record] | Record):
        root_keys = cls.get_root_fields_keys()
        relations = cls.get_relation_fields_keys()
        joins = {}

        for relation in relations:
            relation_cls = cls.get_field(relation).type_
            relation_name = pascal_to_snake_case(relation_cls.__name__)

            joins[relation_name] = {
                "prefixed_fields": relation_cls.get_fields_with_prefix(),
                "plain_fields": relation_cls.get_root_fields_keys(),
            }

        if records is None:
            return None

        if isinstance(records, list):
            return [
                cls(
                    **cls._transform_record_to_dict(
                        record=record, joins=joins, root_keys=root_keys
                    )
                )
                for record in records
            ]

        return cls(
            **cls._transform_record_to_dict(
                record=records, joins=joins, root_keys=root_keys
            )
        )
