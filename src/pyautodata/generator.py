import dataclasses

from pyautodata.builtins import *
from pyautodata.dates import *
from pyautodata.attributes import *


class TypeDataGenerator:
    @staticmethod
    def create(t) -> TypeDataGeneratorBase:
        type_name = t.__name__
        if type_name == 'int':
            return IntegerGenerator()
        elif type_name == 'str':
            return StringGenerator()
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
            return DataClassGenerator(t) if dataclasses.is_dataclass(t) else ClassGenerator(t)


class DataClassGenerator(TypeDataGeneratorBase):
    def __init__(self, cls):
        self.cls = cls

    def generate(self):
        args = []
        fields = dataclasses.fields(self.cls)
        for field in fields:
            generator = TypeDataGenerator.create(field.type)
            args.append((field.name, field.type, generator.generate()))
        name = self.cls.__module__ + '.' + self.cls.__qualname__
        instance = dataclasses.make_dataclass(name, args)
        return instance


class ClassGenerator(TypeDataGeneratorBase):
    def __init__(self, cls):
        self.instance = cls()

    def generate(self):
        attributes = Attributes(self.instance)
        members = attributes.get_members()
        for member in members:
            attr = attributes.get_attribute(member)
            if type(attr).__name__ == 'list':
                for i in range(len(attr)):
                    generator = TypeDataGenerator.create(type(attr[i]))
                    attr[i] = generator.generate()
            else:
                generator = TypeDataGenerator.create(type(attr))
                attributes.set_value(member, generator.generate())
        return self.instance


class ListGenerator(TypeDataGeneratorBase):
    def __init__(self, t):
        self.instance = t()

    def generate(self):
        items = []
        for item in self.instance:
            generator = TypeDataGenerator.create(item)
            value = generator.generate()
            items.append(value)
        return items
