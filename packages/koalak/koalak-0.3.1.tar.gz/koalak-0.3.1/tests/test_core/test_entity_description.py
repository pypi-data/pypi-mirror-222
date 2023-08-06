import pytest
from koalak.relationaldb import Entity, GenericField


def test_generic_field_equality():
    entity = Entity()
    test_field = entity.add_field("test")
    assert test_field == GenericField("test")

    assert entity.add_field("attr2", kw_only=True) == GenericField(
        "attr2", kw_only=True
    )


def test_dunder_methods():
    entity = Entity()
    assert len(entity) == 0

    filed1 = entity.add_field("firstname")
    assert len(entity) == 1
    assert list(entity) == [filed1]

    field2 = entity.add_field("lastname")
    assert len(entity) == 2
    assert list(entity) == [filed1, field2]


def test_add_existing_field():
    entity = Entity()
    assert len(entity) == 0

    filed1 = entity.add_field("firstname")
    assert len(entity) == 1
    assert list(entity) == [filed1]

    field2 = GenericField("lastname")
    entity.add_existing_field(field2)
    assert len(entity) == 2
    assert list(entity) == [filed1, field2]

    with pytest.raises(ValueError):
        # Field without name not allowed
        entity.add_existing_field(GenericField())

    with pytest.raises(ValueError):
        # Already existing
        entity.add_existing_field(GenericField("firstname"))


def test_builting_attrs_class():
    entity = Entity("persons", cls_name="Person")
    entity.add_field("firstname")
    entity.add_field("lastname")

    Person = entity.build_attrs_dataclass()

    person = Person("John", "Smith")
    assert person.firstname == "John"
    assert person.lastname == "Smith"


def test_equality():
    assert Entity() == Entity()
    assert Entity("name") == Entity("name")

    assert Entity(description="abc") != Entity()
    assert Entity("a") != Entity("b")
