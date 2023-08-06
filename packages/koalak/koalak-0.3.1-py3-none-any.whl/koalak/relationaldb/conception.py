import re
import typing
from pathlib import Path
from typing import Dict, Iterator, List, Union

import attrs

# For debug
from devtools import debug
from koalak.core import GenericField
from koalak.decorators import optionalargs

from .bases import Entity


def camel_to_snake(name):
    # TODO: understand this code!
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


ATTR_METADATA_KEY = "relationaldb"
HANDLED_TYPES = [str, int, float, bool]


def attr_metadata(
    in_filter_query: bool = None,
    ref=None,
    description: str = None,
    examples: Union[str, List[str]] = None,
    indexed: bool = None,
    unique: bool = None,
):
    if examples is None:
        examples = []
    elif isinstance(examples, str):
        examples = [examples]

    if indexed is None:
        indexed = False
    if unique is None:
        unique = False
    return {
        ATTR_METADATA_KEY: {
            "in_filter_query": in_filter_query,
            "ref": ref,
            "description": description,
            "examples": examples,
            "unique": unique,
            "indexed": indexed,
        }
    }


def attribute(
    # attrs attribute
    *,
    type=None,
    default=attrs.NOTHING,
    validator=None,
    repr=True,
    hash=None,
    init=True,
    metadata=None,
    converter=None,
    factory=None,
    kw_only=False,
    eq=None,
    order=None,
    on_setattr=None,
    # entities attribute
    in_filter_query: bool = None,
    ref=None,
    description: str = None,
    examples: Union[str, List[str]] = None,
    indexed: bool = None,
    unique: bool = None,
):
    relationaldb_metadata = attr_metadata(
        in_filter_query=in_filter_query,
        unique=unique,
        ref=ref,
        examples=examples,
        indexed=indexed,
        description=description,
    )
    if not metadata:
        metadata = {}
    metadata.update(relationaldb_metadata)
    attrib = attrs.field(  # noqa
        default=default,
        validator=validator,
        repr=repr,
        hash=hash,
        init=init,
        metadata=metadata,
        type=type,
        converter=converter,
        factory=factory,
        kw_only=kw_only,
        eq=eq,
        order=order,
        on_setattr=on_setattr,
    )
    return attrib


field = attribute


class Conceptor:
    """Base class to design the database. Responsible to register the entities"""

    def __init__(self):
        self.builder = None
        self._built = False
        self._initialized = False
        self._built_cls = None
        self._cg = None
        self._map_clsname_to_entity = {}

        # 2nd try
        self._entities: Dict[str:Entity] = {}

    def _check_initialized(self):
        if self._initialized:
            raise ValueError(f"Can not add new entities to already initialize class")

    def add_entity(self, name: str, description: str = None):
        self._check_initialized()
        if name in self._entities:
            raise ValueError(f"Entity {name!r} already exists")

        entity = Entity(name=name, description=description)
        self._entities[name] = entity
        return entity

    def add_entity_from_cls(self, cls, name=None, description=None):
        # FIXME: add description and other attributes?
        self._check_initialized()
        if name is None:
            name = cls.__name__

        if name in self._entities:
            raise ValueError(f"Entity {name!r} already exists")

        entity = Entity(
            name=name, cls=cls, description=description, cls_name=cls.__name__
        )
        # Adding fields
        generic_fields = {
            attr_name: getattr(cls, attr_name)
            for attr_name in cls.__dict__
            if isinstance(getattr(cls, attr_name), GenericField)
        }
        for field_name, field in generic_fields.items():
            field = field.copy()
            field.name = field_name
            if hasattr(cls, "__annotations__") and field_name in cls.__annotations__:
                field.annotation = cls.__annotations__[field_name]
            entity.add_existing_field(field)

        self._entities[name] = entity

        return entity

    def __iter__(self) -> Iterator[Entity]:
        yield from self._entities.values()

    def __len__(self):
        return self._entities.__len__()

    def __getitem__(self, item):
        return self._entities.__getitem__(item)

    attr_metadata = staticmethod(attr_metadata)
    attribute = staticmethod(GenericField)
    field = attribute

    @optionalargs(firstarg=str)
    def entity(self, cls, entity_name: str = None, *, description: str = None):
        if entity_name is None:
            entity_name = cls.__name__

        entity = self.add_entity_from_cls(
            cls, name=entity_name, description=description
        )
        attrs_cls = entity.build_attrs_dataclass(name=cls.__name__)
        entity.cls = attrs_cls
        return attrs_cls

    @optionalargs(firstarg=str)
    def entity2(self, cls, entity_name: str = None, *, description: str = None):
        """Register new entity"""
        # FIXME: if entity name match keyword! keep keyword and entity will be accesible trhoug [] syntax
        # FIXME: study the case if the entity is already built

        self._check_initialized()
        # ======================================= #
        # decorate cls with attr (if not already) #
        # ======================================= #
        if entity_name is None:
            entity_name = cls.__name__
        if not hasattr(cls, "__attrs_attrs__"):
            # TODO: adding slots is False, so that we can dynamically add attributes to our class!
            #       we can simply ad the attribute `id` so that we don't need slots?
            cls = attrs.define(cls, slots=False)

            current_entity = Entity(
                name=entity_name,
                cls=cls,
                cls_name=cls.__name__,
                attribute_name=camel_to_snake(cls.__name__),
                description=description,
            )
            self.entities[entity_name] = current_entity

            # add attributes
            current_attributes = current_entity.attributes
            for attr_attribute in cls.__attrs_attrs__:
                # Add annotation for autocomplete
                attr_attribute: attrs.Attribute

                required = attr_attribute.default is attrs.NOTHING
                relationaldb_attr_metadata = attr_attribute.metadata.get(
                    ATTR_METADATA_KEY, {}
                )

                current_attributes[attr_attribute.name] = GenericField(
                    attr_attribute.name,
                    annotation=attr_attribute.type,
                    kw_only=attr_attribute.kw_only,
                    required=required,
                    default=attr_attribute.default,
                    **relationaldb_attr_metadata,
                )

        else:
            raise ValueError(
                f"Class {cls.__name__} must not be decorated with attrs.define use db.define instead!"
            )

        return cls

    define = entity

    def init(self):
        """

        List of checks
        - Conception not initilaised twice
        - Check all type are handled
            - primitives types
            - list/set ...
            - known entity
        - All entities must have an attrs class
        """

        # Check that class is not already initialised
        if self._initialized:
            raise ValueError(f"Already initialized")
        self._initialized = True

        # Adding classes for each entity (if it doesn't have)
        for entity in self:
            if entity.cls is None:
                entity.cls = entity.build_attrs_dataclass()
                entity.cls_name = entity.cls.__name__

        # Add cls mapping
        for entity in self:
            self._map_clsname_to_entity[entity.cls_name] = entity

        # Get classes
        classes = [e.cls for e in self]

        # Compute referenced_entity
        for entity in self:
            for field in entity:
                if typing.get_origin(field.annotation) not in [dict, list, None]:
                    pass

                if field.annotation is None:
                    continue
                elif field.annotation in HANDLED_TYPES:
                    continue
                elif isinstance(field.annotation, str):
                    if field.annotation in self._entities:
                        field.referenced_entity = self._entities[field.annotation]
                        field.annotation = field.referenced_entity.cls
                    else:
                        pass  # FIXME: raise value error

                # TODO: here, we have to handle List[] Set[] ...
                else:  # field.annotation is a cls
                    cls_name = field.annotation.__name__
                    if cls_name not in self._map_clsname_to_entity:
                        raise ValueError(
                            f"Unregistred/Unhandled annotation for field {entity.name}.{field.name}: {field.annotation}"
                        )
                    referenced_entity = self._map_clsname_to_entity[cls_name]
                    field.referenced_entity = referenced_entity

        """
        for entity in self:
            for attribute in entity:
                attribute.atomic_type = attribute.annotation  # fixme

                # Check if the atomic_type is already registred (random cls) or handled (primitive types)
                if (
                    attribute.atomic_type is not None
                    and attribute.atomic_type not in PRIMITIVE_TYPES
                    and attribute.atomic_type not in classes
                ):
                    raise ValueError(
                        f"Type of attribute {entity.name}.{attribute.name} is a cls which is "
                        f"nor registered nor handled"
                    )

                if attribute.atomic_type in classes:

                    if (
                        not attribute.ref
                    ):  # since type is an annotation make attribute true
                        cls_name = attribute.atomic_type.__name__
                        attribute.ref = self._map_clsname_to_entity[cls_name]

                    if isinstance(attribute.ref, str):
                        pass
                        # ref_entity = self._map_clsname_to_entity[attribute.annotation.__name__]
                        # ref_entity.attributes[attribute.ref] = Attribute(attribute.ref, many=True,
                        # ref=attribute.name, annotation=ref_entity.cls)
                        # FIXME: if we add an attribute, it will be added, so we must have 2 attribues
                        #  attributes that will be built, and references attributes?
    """

    def build(self, name="BaseDatabase"):
        self.init()

        from .mongodb_builder import MongodbBuilder

        mongodb_builder = MongodbBuilder(self, name)
        self._code = mongodb_builder.generate_code()
        self._stubcode = mongodb_builder.generate_stub_code()

        self._built = True
        self._built_cls = mongodb_builder.build()
        return self._built_cls

    def mongodb(
        self,
        dbname: str,
        host: str = "127.0.0.1",
        port: int = 27017,
        timeout: int = 3000,
        username: str = None,
        password: str = None,
    ):
        # TODO: refactor and add None to every thing
        if not self._built:
            self.build()

        return self._built_cls(
            dbname=dbname,
            host=host,
            port=port,
            timeout=timeout,
            username=username,
            password=password,
        )

    def create_stubfile(self, *, __file__: str):
        path = Path(__file__)
        if not path.exists():
            raise FileNotFoundError(
                f"File {__file__} not found to create it's stub file"
            )

        if not __file__.endswith(".py"):
            raise ValueError(f".py file must be provided")

        pyi_file = __file__.replace(".py", ".pyi")

        pyi_code = self._stubcode
        if not Path(pyi_file).exists() or open(pyi_file).read() != pyi_code:
            print("Adding stub file")
            with open(pyi_file, "w") as f:
                f.write(pyi_code)

    def create_codefile(self, *, __file__: str):
        path = Path(__file__)
        if not path.exists():
            raise FileNotFoundError(
                f"File {__file__} not found to create it's stub file"
            )

        if not __file__.endswith(".py"):
            raise ValueError(f".py file must be provided")

        pyi_file = __file__.replace(".py", "_codegen.py")
        pyi_code = self._code
        if not Path(pyi_file).exists() or open(pyi_file).read() != pyi_code:
            print("Adding code file")
            with open(pyi_file, "w") as f:
                f.write(pyi_code)

    @classmethod
    def _str_annotation_to_annotation(cls, str_annotation):
        mapping = {
            "str": str,
            "int": int,
            "bool": bool,
            "float": float,
        }
        return mapping.get(str_annotation, str_annotation)

    @classmethod
    def from_dict(
        cls,
        entities_dict: Dict,
        init=None,
        ignore_entity_keys=None,
        replace_entity_keys=None,
        replace_field_keys=None,
    ):
        if ignore_entity_keys is None:
            ignore_entity_keys = []

        if replace_entity_keys is None:
            replace_entity_keys = {}

        if replace_field_keys is None:
            replace_field_keys = {}

        if init is None:
            init = True

        conception = Conceptor()
        debug(replace_entity_keys)
        for entity_name, entity_dict in entities_dict.items():
            # Remove ignored keys
            for key in ignore_entity_keys:
                entity_dict.pop(key, None)

            # Rename keys
            for old_name, new_name in replace_entity_keys.items():
                if old_name in entity_dict:
                    entity_dict[new_name] = entity_dict.pop(old_name)

            fields_dict = entity_dict.pop("fields")
            current_entity = conception.add_entity(entity_name, **entity_dict)

            for field_name, field_dict in fields_dict.items():
                # Rename keys
                for old_name, new_name in replace_field_keys.items():
                    if old_name in field_dict:
                        field_dict[new_name] = field_dict.pop(old_name)

                if "type" in field_dict:
                    field_dict["type"] = cls._str_annotation_to_annotation(
                        field_dict["type"]
                    )

                if field_dict.get("is_set"):
                    field_dict.pop("is_set")
                    if field_dict.get("type"):
                        field_dict["type"] = typing.Set[field_dict["type"]]
                    else:
                        field_dict["type"] = typing.Set

                # FIXME: same with list

                current_entity.add_field(field_name, **field_dict)

        if init:
            conception.init()
        return conception

    def print(self):
        import rich

        for entity in self:
            rich.print(f"Entity: {entity.name}")
            for field in entity:
                print(f"  {field.name}")
