import random
import uuid

from pyautodata.base import TypeDataGeneratorBase


class IntegerGenerator(TypeDataGeneratorBase):
    def generate(self):
        return random.randint(0, 2147483647)


class StringGenerator(TypeDataGeneratorBase):
    def generate(self):
        return str(uuid.uuid4())


class FloatGenerator(TypeDataGeneratorBase):
    def generate(self):
        return random.uniform(0, 2147483647)


class BooleanGenerator(TypeDataGeneratorBase):
    def generate(self):
        return bool(random.getrandbits(1))
