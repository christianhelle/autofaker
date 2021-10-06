import random
import uuid

from pyautodata.base import TypeDataGeneratorBase


class IntegerGeneratorBase(TypeDataGeneratorBase):

    def generate(self):
        return random.randint(0, 2147483647)


class StringGeneratorBase(TypeDataGeneratorBase):
    def generate(self):
        return str(uuid.uuid4())


class FloatGeneratorBase(TypeDataGeneratorBase):
    def generate(self):
        return random.uniform(0, 2147483647)

