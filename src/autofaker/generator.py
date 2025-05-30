import dataclasses
import inspect

import typing_inspect

from autofaker.attributes import Attributes
from autofaker.dates import DateGenerator, DatetimeGenerator, is_date_type
from autofaker.enums import EnumGenerator, is_enum
from autofaker.factory import BuiltinTypeDataGeneratorFactory
from autofaker.fakes import TypeDataGeneratorBase
from autofaker.literals import LiteralGenerator, is_literal_type


class TypeDataGenerator:
    @staticmethod
    def create(
        t, field_name: str = None, use_fake_data: bool = False
    ) -> TypeDataGeneratorBase:
        type_name = TypeDataGenerator._get_type_name(t).lower()
        if BuiltinTypeDataGeneratorFactory.is_supported(type_name):
            return BuiltinTypeDataGeneratorFactory.create(
                type_name, field_name, use_fake_data
            )
        if is_date_type(type_name):
            return TypeDataGenerator.create_datetime(
                type_name
            )
        if type_name == "list":
            return ListGenerator(t)
        if is_enum(t):
            return EnumGenerator(t)
        if is_literal_type(t):
            return LiteralGenerator(t)
        return (
            DataClassGenerator(t, use_fake_data=use_fake_data)
            if dataclasses.is_dataclass(t)
            else ClassGenerator(t, use_fake_data=use_fake_data)
        )

    @staticmethod
    def create_datetime(type_name):
        if type_name == "datetime":
            return DatetimeGenerator()
        if type_name == "date":
            return DateGenerator()

    @staticmethod
    def _get_type_name(t) -> str:
        PRIMITIVE_TYPES = {
            "int", "float", "str", "complex", "range", "bytes", "bytearray"
        }

        try:
            return t.__name__
        except Exception:
            attributes = dir(t)
            if "_name" in attributes:
                if t._name is not None:
                    return t._name
            # If __future__.annotations was imported by the user, then the type
            # will be a str. Thus, asserting the type with type() will fail,
            # because it will always be a string. This is because, annotations
            # transforms any type into a string object. Therefore, if the type
            # is a string, assess if it is the name of a known primitive type.
            elif t.isinstance(str) and t in PRIMITIVE_TYPES:
                return t
            return type(t).__name__


class DataClassGenerator(TypeDataGeneratorBase):
    def __init__(self, cls, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        self.cls = cls

    def generate(self):
        fields = dataclasses.fields(self.cls)
        params = {}
        for dataclass_field in fields:
            field_type = dataclass_field.type
            generator = TypeDataGenerator.create(
                field_type, dataclass_field.name, use_fake_data=self.use_fake_data
            )
            params[dataclass_field.name] = generator.generate()
        instance = self.cls(**params)
        return instance


class ClassGenerator(TypeDataGeneratorBase):
    def __init__(self, cls, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        self._try_create_instance(cls)

    def generate(self):
        if not self._is_supported():
            return None

        attributes = Attributes(self.instance)
        members = attributes.get_members()

        for member in members:
            attr = attributes.get_attribute(member)
            if type(attr).__name__ == "list":
                for i in range(len(attr)):
                    attr[i] = self._try_generate(attr[i])
            else:
                attributes.set_value(member, self._try_generate(attr))

        if hasattr(self.instance, '__annotations__'):
            for key, value in self.instance.__annotations__.items():
                if key not in members:
                    if is_literal_type(value):
                        v = LiteralGenerator(value).generate()
                        self.instance.__dict__[key] = v

        return self.instance

    def _is_supported(self):
        import pandas

        unsupported_types = [pandas.core.frame.DataFrame]
        for t in unsupported_types:
            if isinstance(self.instance, t):
                return False
        return True

    def _try_generate(self, attr):
        try:
            generator = TypeDataGenerator.create(
                type(attr), use_fake_data=self.use_fake_data
            )
            return generator.generate()
        except TypeError as e:
            print(e)

    def _try_create_instance(self, cls):
        try:
            self.instance = cls()
        except TypeError:
            self._create_with_init_args(cls)

    def _create_with_init_args(self, cls):
        init_args = inspect.getfullargspec(cls.__init__)
        values = []
        for t in init_args.annotations.values():
            origin = typing_inspect.get_origin(t)
            if origin == list:
                list_arg = typing_inspect.get_args(t)
                items = []
                for _ in range(3):
                    generator = TypeDataGenerator.create(
                        list_arg[0], use_fake_data=self.use_fake_data
                    )
                    items.append(generator.generate())
                values.append(items)
            else:
                generator = TypeDataGenerator.create(
                    t, use_fake_data=self.use_fake_data
                )
                value = generator.generate()
                values.append(value)
        self.instance = cls(*tuple(values))


class ListGenerator(TypeDataGeneratorBase):
    def __init__(self, t, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        self.list_arg = typing_inspect.get_args(t)

    def generate(self):
        items = []
        for _ in range(3):
            generator = TypeDataGenerator.create(
                self.list_arg[0], use_fake_data=self.use_fake_data
            )
            items.append(generator.generate())
        return items
