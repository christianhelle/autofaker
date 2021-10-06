from pyautodata.builtins import *
from pyautodata.dates import *


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
            return ClassGenerator(t)


class ClassGenerator(TypeDataGeneratorBase):
    def __init__(self, cls):
        self.instance = cls()

    def generate(self):
        members = [
            attr for attr in dir(self.instance)
            if not callable(getattr(self.instance, attr)) and not attr.startswith("__")
        ]
        for member in members:
            attr = getattr(self.instance, member)
            if type(attr).__name__ == 'list':
                for i in range(len(attr)):
                    item = attr[i]
                    generator = TypeDataGenerator.create(type(item))
                    value = generator.generate()
                    attr[i] = value
            else:
                generator = TypeDataGenerator.create(type(attr))
                value = generator.generate()
                setattr(self.instance, member, value)
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

