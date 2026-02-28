import decimal
import pathlib
import random
import uuid

from autofaker.base import TypeDataGeneratorBase


class IntegerGenerator(TypeDataGeneratorBase):
    def generate(self):
        return random.randint(1, 10000)


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


class TupleGenerator(TypeDataGeneratorBase):
    def generate(self):
        return (
            IntegerGenerator().generate(),
            StringGenerator().generate(),
            FloatGenerator().generate(),
        )


class SetGenerator(TypeDataGeneratorBase):
    def generate(self):
        return {
            StringGenerator().generate(),
            StringGenerator().generate(),
            StringGenerator().generate(),
        }


class FrozenSetGenerator(TypeDataGeneratorBase):
    def generate(self):
        return frozenset({
            StringGenerator().generate(),
            StringGenerator().generate(),
            StringGenerator().generate(),
        })


class DictGenerator(TypeDataGeneratorBase):
    def generate(self):
        return {
            StringGenerator().generate(): IntegerGenerator().generate(),
            StringGenerator().generate(): IntegerGenerator().generate(),
            StringGenerator().generate(): IntegerGenerator().generate(),
        }


class DecimalGenerator(TypeDataGeneratorBase):
    def generate(self):
        return decimal.Decimal(str(random.uniform(0, 10000)))


class UUIDGenerator(TypeDataGeneratorBase):
    def generate(self):
        return uuid.uuid4()


class PathGenerator(TypeDataGeneratorBase):
    def generate(self):
        return pathlib.Path(
            StringGenerator().generate(),
            StringGenerator().generate(),
        )
