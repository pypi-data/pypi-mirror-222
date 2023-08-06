from typing import Set

import attr
import pytest
from koalak.core import GenericField
from koalak.relationaldb import conception

# ======================================= #
# TESTING CONCEPTION with descriptive API #
# ======================================= #


def test_conception_add_entity():
    c = conception()

    assert len(c) == 0

    entity_persons = c.add_entity("persons")

    assert len(c) == 1
    assert c["persons"] is entity_persons

    entity_animals = c.add_entity("animals")
    assert len(c) == 2
    assert c["animals"] is entity_animals

    assert list(c) == [entity_persons, entity_animals]

    with pytest.raises(ValueError):
        c.add_entity("persons")  # name already exists


def test_conception_add_entity_from_cls_empty_cls_with_name():
    pass
    c = conception()

    assert len(c) == 0

    class Person:
        pass

    entity_persons = c.add_entity_from_cls(Person, name="persons")
    assert entity_persons.cls is Person
    assert entity_persons.cls_name == "Person"
    assert entity_persons.name == "persons"

    assert len(c) == 1
    assert c["persons"] is entity_persons


def test_conception_add_entity_from_cls_empty_cls_without_name():
    c = conception()

    assert len(c) == 0

    class Person:
        pass

    entity_persons = c.add_entity_from_cls(Person)
    assert entity_persons.cls is Person
    assert entity_persons.cls_name == "Person"
    assert entity_persons.name == "Person"

    assert len(c) == 1
    assert c["Person"] is entity_persons


def test_conception_add_entity_from_cls_with_fields():
    pass
    c = conception()

    assert len(c) == 0

    class Person:
        firstname = GenericField()
        lastname: str = GenericField()

    entity_persons = c.add_entity_from_cls(Person, name="persons")
    assert entity_persons.cls is Person
    assert entity_persons.cls_name == "Person"
    assert entity_persons.name == "persons"

    assert len(c) == 1
    assert c["persons"] is entity_persons

    assert len(entity_persons) == 2
    firstname_field = entity_persons["firstname"]
    assert firstname_field.annotation is None

    lastname_field = entity_persons["lastname"]
    assert lastname_field.annotation is str


def test_conception_with_2_class_with_generic_fields():
    c = conception()
    assert len(c) == 0

    class Person:
        firstname = GenericField()
        lastname: str = GenericField()

    class Animal:
        name: str = GenericField()
        owner: Person = GenericField()

    entity_persons = c.add_entity_from_cls(Person, name="persons")
    entity_animals = c.add_entity_from_cls(Animal, name="animals")

    assert entity_persons.cls is Person
    assert entity_persons.cls_name == "Person"
    assert entity_persons.name == "persons"
    assert len(entity_persons) == 2

    assert entity_animals.cls is Animal
    assert entity_animals.cls_name == "Animal"
    assert entity_animals.name == "animals"
    assert len(entity_animals) == 2
    assert entity_animals["owner"].annotation is Person


def test_simple_metadata_one_entity_without_entity_name():
    c = conception()

    @c.entity
    class Animal:
        name = c.field()

    c.init()

    assert len(c) == 1

    animals_entity = c["Animal"]
    assert animals_entity.cls is Animal
    assert animals_entity.cls_name == "Animal"
    assert animals_entity.name == "Animal"


def test_simple_metadata_one_entity_with_entity_name():
    c = conception()

    @c.define("animals")
    class Animal:
        name = c.field()

    c.init()

    assert len(c) == 1

    animals_entity = c["animals"]
    assert animals_entity.cls is Animal
    assert animals_entity.cls_name == "Animal"
    assert animals_entity.name == "animals"


def test_simple_metadata_one_entity_02():
    c = conception()

    @c.define
    class Animal:
        name = c.field()

    @c.define
    class Person:
        firstname = c.field()

    c.init()

    assert len(c) == 2

    animals_entity = c["Animal"]
    assert animals_entity.cls is Animal
    assert animals_entity.cls_name == "Animal"
    assert animals_entity.name == "Animal"

    entity = c["Person"]
    assert entity.cls is Person
    assert entity.cls_name == "Person"
    assert entity.name == "Person"


def test_simple_metadata_one_entity_02_with_entity_name():
    c = conception()

    @c.define("animals")
    class Animal:
        name = c.field()

    @c.define("persons")
    class Person:
        firstname = c.field()

    c.init()

    assert len(c) == 2

    animals_entity = c["animals"]
    assert animals_entity.cls is Animal
    assert animals_entity.cls_name == "Animal"
    assert animals_entity.name == "animals"

    entity = c["persons"]
    assert entity.cls is Person
    assert entity.cls_name == "Person"
    assert entity.name == "persons"


def test_metadata_attributes_one_entity_without_entity_name():
    c = conception()

    @c.define
    class Animal:
        name: str = c.field()
        age: int = c.field(default=10)

    assert len(c) == 1

    animals_entity = c["Animal"]
    assert len(animals_entity) == 2

    attribute = animals_entity["name"]
    assert attribute.name == "name"
    assert attribute.annotation is str
    assert attribute.required is True
    assert attribute.default is attr.NOTHING

    attribute = animals_entity["age"]
    assert attribute.name == "age"
    assert attribute.annotation is int
    assert attribute.required is False
    assert attribute.default == 10


def test_metadata_attributes_one_entity_with_entity_name():
    c = conception()

    @c.define("animals")
    class Animal:
        name: str = c.field()
        age: int = c.field(default=10)

    assert len(c) == 1

    animals_entity = c["animals"]
    assert len(animals_entity) == 2

    attribute = animals_entity["name"]
    assert attribute.name == "name"
    assert attribute.annotation is str
    assert attribute.required is True
    assert attribute.default is attr.NOTHING

    attribute = animals_entity["age"]
    assert attribute.name == "age"
    assert attribute.annotation is int
    assert attribute.required is False
    assert attribute.default == 10


# ============== #
# TEST RELATIONS #
# ============== #


def test_conception_relation_one_to_many_basic_descriptive_api():
    c = conception()

    # Adding persons entity
    entity_persons = c.add_entity("persons")
    persons_firstname_field = entity_persons.add_field("firstname", type=str)
    persons_lastname_field = entity_persons.add_field(
        "lastname", type=str, default=None
    )

    # Adding animals entity
    entity_animals = c.add_entity("animals")
    animals_name_field = entity_animals.add_field("name", type=str)
    animals_owner_field = entity_animals.add_field(
        "owner", type="persons", default=None
    )

    c.init()

    # Checking conception
    assert len(c) == 2
    assert c["persons"] is entity_persons
    assert c["animals"] is entity_animals

    # Checking entity persons
    assert c["persons"] is entity_persons
    assert len(entity_persons) == 2
    assert entity_persons["firstname"] is persons_firstname_field
    assert persons_firstname_field.name == "firstname"
    assert persons_firstname_field.annotation is str
    assert persons_firstname_field.referenced_entity is None

    assert entity_persons["lastname"] is persons_lastname_field
    assert persons_lastname_field.name == "lastname"
    assert persons_lastname_field.annotation is str
    assert persons_lastname_field.referenced_entity is None

    # Checking entity animals
    assert c["animals"] is entity_animals
    assert len(entity_animals) == 2
    assert entity_animals["name"] is animals_name_field
    assert animals_name_field.name == "name"
    assert animals_name_field.annotation is str
    assert animals_name_field.referenced_entity is None

    assert entity_animals["owner"] is animals_owner_field
    assert animals_owner_field.name == "owner"
    assert animals_owner_field.annotation is entity_persons.cls
    assert animals_owner_field.referenced_entity is entity_persons


def test_conception_relation_one_to_many_basic_cls_api():
    c = conception()

    # Adding persons entity
    @c.entity("persons")
    class Person:
        firstname: str = c.field()
        lastname: str = c.field()

    @c.entity("animals")
    class Animal:
        name: str = c.field()
        owner: Person = c.field()

    c.init()

    # Checking conception
    assert len(c) == 2
    entity_persons = c["persons"]
    entity_animals = c["animals"]

    # Checking entity persons
    assert entity_persons.cls is Person
    assert len(entity_persons) == 2
    persons_firstname_field = entity_persons["firstname"]
    assert persons_firstname_field.name == "firstname"
    assert persons_firstname_field.annotation is str
    assert persons_firstname_field.referenced_entity is None

    persons_lastname_field = entity_persons["lastname"]
    assert persons_lastname_field.name == "lastname"
    assert persons_lastname_field.annotation is str
    assert persons_lastname_field.referenced_entity is None

    # Checking entity animals
    assert entity_animals.cls is Animal
    assert len(entity_animals) == 2
    animals_name_field = entity_animals["name"]
    assert animals_name_field.name == "name"
    assert animals_name_field.annotation is str
    assert animals_name_field.referenced_entity is None

    animals_owner_field = entity_animals["owner"]
    assert animals_owner_field.name == "owner"
    assert animals_owner_field.annotation is entity_persons.cls
    assert animals_owner_field.referenced_entity is entity_persons


# Test List, Set
def test_conception_type_is_a_set_of_elements():
    c = conception()

    # Adding persons entity
    @c.entity("persons")
    class Person:
        firstname: str = c.field()
        lastname: str = c.field()
        pet_names: Set[str] = c.field()

    c.init()

    # Checking conception
    assert len(c) == 1
    entity_persons = c["persons"]

    # Checking entity persons
    assert entity_persons.cls is Person
    assert len(entity_persons) == 3
    persons_firstname_field = entity_persons["firstname"]
    assert persons_firstname_field.name == "firstname"
    assert persons_firstname_field.annotation is str
    assert persons_firstname_field.referenced_entity is None

    persons_lastname_field = entity_persons["lastname"]
    assert persons_lastname_field.name == "lastname"
    assert persons_lastname_field.annotation is str
    assert persons_lastname_field.referenced_entity is None

    persons_pet_names_field = entity_persons["pet_names"]
    assert persons_pet_names_field.name == "pet_names"
    assert persons_pet_names_field.annotation is Set[str]
    assert persons_pet_names_field.referenced_entity is None
    assert persons_pet_names_field.is_set
    assert not persons_pet_names_field.is_list
    assert not persons_pet_names_field.is_atomic


# =========== #
# TEST ERRORS #
# =========== #
def test_error_double_init():
    c = conception()

    @c.define("animals")
    class Animal:
        name = c.field()

    c.init()
    with pytest.raises(ValueError):
        c.init()


def test_error_adding_cls_after_init():
    c = conception()

    @c.define("animals")
    class Animal:
        name = c.field()

    c.init()
    with pytest.raises(ValueError):

        @c.define("persons")
        class Person:
            name = c.field()


def test_error_referencing_none_registred_cls():
    class Person:
        pass

    c = conception()

    @c.define("animals")
    class Animal:
        name: Person = c.field()

    with pytest.raises(ValueError):
        c.init()


# TODO think about how it should work with ATTRS?
