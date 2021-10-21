import dataclasses

from autofaker.attributes import Attributes
from autofaker.builtins import IntegerGenerator, FloatGenerator, BooleanGenerator
from autofaker.dates import DatetimeGenerator, DateGenerator
from autofaker.fakes import FakeStringGenerator, StringGenerator, FakeIntegerGenerator, TypeDataGeneratorBase


class TypeDataGenerator:
    @staticmethod
    def create(t, field_name: str = None, use_fake_data: bool = False) -> TypeDataGeneratorBase:
        type_name = t.__name__
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
        elif type_name == 'bool':
            return BooleanGenerator()
        elif type_name == 'datetime':
            return DatetimeGenerator()
        elif type_name == 'date':
            return DateGenerator()
        elif type_name == 'list':
            return ListGenerator(t)
        else:
            return DataClassGenerator(t, use_fake_data=use_fake_data) \
                if dataclasses.is_dataclass(t) \
                else ClassGenerator(t, use_fake_data=use_fake_data)


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
        self.instance = cls()

    def generate(self):
        attributes = Attributes(self.instance)
        members = attributes.get_members()
        for member in members:
            attr = attributes.get_attribute(member)
            if type(attr).__name__ == 'list':
                for i in range(len(attr)):
                    generator = TypeDataGenerator.create(type(attr[i]), use_fake_data=self.use_fake_data)
                    attr[i] = generator.generate()
            else:
                generator = TypeDataGenerator.create(type(attr), member, use_fake_data=self.use_fake_data)
                attributes.set_value(member, generator.generate())
        return self.instance


class ListGenerator(TypeDataGeneratorBase):
    def __init__(self, t, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        self.instance = t()

    def generate(self):
        items = []
        for item in self.instance:
            generator = TypeDataGenerator.create(item, use_fake_data=self.use_fake_data)
            value = generator.generate()
            items.append(value)
        return items
