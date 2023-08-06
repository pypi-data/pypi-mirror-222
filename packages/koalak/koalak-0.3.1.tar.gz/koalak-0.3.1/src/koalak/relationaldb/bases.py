from typing import Dict, Iterator, List

import attrs
from koalak.core import GenericField

from .utils import _attr_nothing_factory, camel_to_snake


class Entity:
    def __init__(
        self,
        name: str = None,
        *,
        cls_name: str = None,
        cls=None,
        description: str = None,
    ):
        self.name: str = name
        self.cls_name: str = cls_name
        self.cls = cls
        self.description: str = description
        self._fields = {}

    def __iter__(self) -> Iterator[GenericField]:
        yield from self._fields.values()

    def __len__(self):
        return self._fields.__len__()

    def __getitem__(self, item):
        return self._fields.__getitem__(item)

    def __repr__(self):
        name = self.name
        if name is None:
            name = ""
        return f"Entity({name})"

    def __eq__(self, other):
        if not isinstance(other, Entity):
            raise ValueError(
                f"Cannot compare {self.__class__.__name__!r} with a different type."
            )

        if (
            self.name == other.name
            and self.cls_name == other.cls_name
            and self.cls == other.cls
            and self.description == other.description
            and self._fields == other._fields
        ):
            return True

        return False

    def add_field(self, name: str, *args, **kwargs):
        if name in self._fields:
            raise ValueError(f"Field {name!r} already exists")

        field = GenericField(name=name, *args, **kwargs)
        self._fields[name] = field
        return field

    def add_existing_field(self, field: GenericField):
        if field.name is None:
            raise ValueError(f"field.name must not be None")

        if field.name in self._fields:
            raise ValueError(f"Field {field.name!r} already exists")

        # TODO: what if the generic_field is changed afterward?
        self._fields[field.name] = field
        return field

    @property
    def fields(self):
        return list(self)

    def get_fields(self, kw_only=None):
        raise NotImplemented

    def get_kw_only_attributes(self):
        return [e for e in self if e.kw_only]

    def get_not_kw_only_attributes(self):
        return [e for e in self if not e.kw_only]

    def get_in_filter_query_attributes(self):
        return [e for e in self if e.in_filter_query]

    def get_not_in_filter_query_attributes(self):
        return [e for e in self if not e.in_filter_query]

    # TODO: remove following functions!
    @property
    def snakecase_name(self):
        return camel_to_snake(self.cls_name)

    @property
    def camlecase_name(self):
        return self.cls_name

    @property
    def container_name(self):
        return f"{self.cls_name}Container"

    @property
    def normalize_func_name(self):
        return f"_normalize_{self.snakecase_name}"

    @property
    def fromdict_name(self):
        return f"fromdict_{self.snakecase_name}"

    def build_attrs_dataclass(self, name=None):
        if name is None:
            name = self.name
        attributes = {}
        for field in self:
            attributes[field.name] = field.build_attrs_field()

        AttrClass = type(name, (object,), attributes)
        return attrs.define(AttrClass)
