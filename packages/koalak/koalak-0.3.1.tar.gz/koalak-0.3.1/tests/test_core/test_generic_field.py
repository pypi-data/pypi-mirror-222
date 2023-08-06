from typing import List, Set

import attrs
import pytest
from koalak.core import GenericField, field


def test_default_values():
    field = GenericField()

    assert field.name is None

    # attributes related to arguments/parameters
    assert field.kw_only is False
    assert field.default is attrs.NOTHING
    assert field.required is True
    assert field.annotation is None

    # attributes related to type checking
    assert field.type is None
    assert field.choices is None  # FIXME: None or list?

    # attributes related to documentation
    assert field.description is None
    assert field.examples is None

    # attributes related to database
    assert field.unique is False
    assert field.indexed is False


def test_generic_field_if_default_required_is_false():
    field = GenericField(default=10)
    assert field.default == 10
    assert field.required is False


def test_generic_field_error_when_default_and_factory_are_set():
    with pytest.raises(ValueError):
        field(default=10, factory=list)


def test_method_get_default():
    field = GenericField()
    assert field.get_default() is attrs.NOTHING

    field = GenericField(default=10)
    assert field.default == 10

    field = GenericField(factory=list)
    l1 = field.get_default()
    assert l1 == []

    l2 = field.get_default()
    assert l2 == []

    assert l1 is not l2


def test_required_property():
    field = GenericField()
    assert field.required is True

    field = GenericField(default=10)
    assert field.required is False

    field = GenericField(factory=list)
    assert field.required is False


def test_equality():
    assert GenericField() == GenericField()
    assert GenericField("name") == GenericField("name")

    assert GenericField(kw_only=True) != GenericField(kw_only=False)
    assert GenericField("a") != GenericField("b")


def test_atomic_type_and_origin_annotation():
    field = GenericField(annotation=str)
    assert not field.is_list()
    assert not field.is_set()
    assert field.is_atomic()
    assert field.atomic_type is str

    field = GenericField(annotation=List[str])
    assert field.is_list()
    assert not field.is_set()
    assert not field.is_atomic()
    assert field.atomic_type is str

    field = GenericField(annotation=Set[int])
    assert not field.is_list()
    assert field.is_set()
    assert not field.is_atomic()
    assert field.atomic_type is int


@pytest.mark.skip
def test_converters():
    field = GenericField(converters=[int])
    assert field.init("12") == 12
