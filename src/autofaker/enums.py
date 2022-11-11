import random

from autofaker.base import TypeDataGeneratorBase


def is_enum(t) -> bool:
    return t.__base__.__name__ == 'Enum'


class EnumGenerator(TypeDataGeneratorBase):
    def __init__(self, enum):
        self.enum = enum

    def generate(self):
        names = [member.name for member in self.enum]
        value = names[random.randint(0, len(self.enum) - 1)]
        return self.enum[value]
