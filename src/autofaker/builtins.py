import random
import uuid

from autofaker.base import TypeDataGeneratorBase


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


class RangeGenerator(TypeDataGeneratorBase):
    def generate(self):
        return range(IntegerGenerator().generate())


class BytesGenerator(TypeDataGeneratorBase):
    def generate(self):
        return bytes(range(random.randint(1, 256)))


class ByteArrayGenerator(TypeDataGeneratorBase):
    def generate(self):
        return bytearray(range(random.randint(1, 256)))


class MemoryViewGenerator(TypeDataGeneratorBase):
    def generate(self):
        return memoryview(BytesGenerator().generate())
