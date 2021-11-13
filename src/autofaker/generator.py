import dataclasses
import inspect
import typing_inspect

from autofaker.attributes import Attributes
from autofaker.builtins import IntegerGenerator, FloatGenerator, BooleanGenerator, ComplexGenerator, is_builtin_type
from autofaker.dates import DatetimeGenerator, DateGenerator, is_date_type
from autofaker.fakes import FakeStringGenerator, StringGenerator, FakeIntegerGenerator, TypeDataGeneratorBase


class TypeDataGenerator:
    @staticmethod
    def create(t, field_name: str = None, use_fake_data: bool = False) -> TypeDataGeneratorBase:
        type_name = TypeDataGenerator._get_type_name(t).lower()
        if is_builtin_type(type_name):
            return TypeDataGenerator.create_builtin(type_name, field_name, use_fake_data)
        elif is_date_type(type_name):
            return TypeDataGenerator.create_datetime(type_name, field_name, use_fake_data)
        elif type_name == 'list':
            return ListGenerator(t)
        else:
            return DataClassGenerator(t, use_fake_data=use_fake_data) \
                if dataclasses.is_dataclass(t) \
                else ClassGenerator(t, use_fake_data=use_fake_data)

    @staticmethod
    def create_builtin(type_name, field_name: str = None, use_fake_data: bool = False):
        if type_name == 'int':
            return FakeIntegerGenerator() \
                if field_name is not None and use_fake_data is True \
                else IntegerGenerator()
        elif type_name == 'str':
            return FakeStringGenerator(field_name) \
                if field_name is not None and use_fake_data is True \
                else StringGenerator()
        elif type_name == 'float':
            return FloatGenerator()
        elif type_name == 'complex':
            return ComplexGenerator()
        elif type_name == 'bool':
            return BooleanGenerator()


    @staticmethod
    def create_datetime(type_name, field_name: str = None, use_fake_data: bool = False):
        if type_name == 'datetime':
            return DatetimeGenerator()
        elif type_name == 'date':
            return DateGenerator()

    @staticmethod
    def _get_type_name(t) -> str:
        try:
            return t.__name__
        except Exception:
            attributes = dir(t)
            if '_name' in attributes:
                return t._name
            else:
                return type(t).__name__


class DataClassGenerator(TypeDataGeneratorBase):
    def __init__(self, cls, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        self.cls = cls

    def generate(self):
        args = []
        fields = dataclasses.fields(self.cls)
        for field in fields:
            generator = TypeDataGenerator.create(field.type, field.name, use_fake_data=self.use_fake_data)
            args.append((field.name, field.type, generator.generate()))
        name = self.cls.__module__ + '.' + self.cls.__qualname__
        instance = dataclasses.make_dataclass(name, args)
        return instance


class ClassGenerator(TypeDataGeneratorBase):
    def __init__(self, cls, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        self._try_create_instance(cls)

    def generate(self):
        attributes = Attributes(self.instance)
        members = attributes.get_members()
        for member in members:
            attr = attributes.get_attribute(member)
            if type(attr).__name__ == 'list':
                for i in range(len(attr)):
                    attr[i] = self._try_generate(attr[i])
            else:
                attributes.set_value(member, self._try_generate(attr))
        return self.instance

    def _try_generate(self, attr):
        try:
            generator = TypeDataGenerator.create(type(attr), use_fake_data=self.use_fake_data)
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
                    generator = TypeDataGenerator.create(list_arg[0], use_fake_data=self.use_fake_data)
                    items.append(generator.generate())
                values.append(items)
            else:
                generator = TypeDataGenerator.create(t, use_fake_data=self.use_fake_data)
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
            generator = TypeDataGenerator.create(self.list_arg[0], use_fake_data=self.use_fake_data)
            items.append(generator.generate())
        return items
