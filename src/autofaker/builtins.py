import random
import uuid

from autofaker.base import TypeDataGeneratorBase


def is_builtin_type(type_name) -> bool:
    return type_name in [
        'int',
        'str',
        'float',
        'complex',
        'bool',
    ]


class IntegerGenerator(TypeDataGeneratorBase):
    def generate(self):
        return random.randint(0, 10000)


class StringGenerator(TypeDataGeneratorBase):
    def generate(self):
        return str(uuid.uuid4())


class FloatGenerator(TypeDataGeneratorBase):
    def generate(self):
        return random.uniform(0, 10000)


class BooleanGenerator(TypeDataGeneratorBase):
    def generate(self):
        return bool(random.getrandbits(1))


class ComplexGenerator(TypeDataGeneratorBase):
    def generate(self):
        return complex(IntegerGenerator().generate())
