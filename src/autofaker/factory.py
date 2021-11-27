from autofaker.builtins import (
    IntegerGenerator,
    FloatGenerator,
    BooleanGenerator,
    ComplexGenerator,
    RangeGenerator,
    BytesGenerator,
    ByteArrayGenerator,
    MemoryViewGenerator
)
from autofaker.fakes import FakeStringGenerator, StringGenerator, FakeIntegerGenerator


class BuiltinTypeDataGeneratorFactory:
    @staticmethod
    def is_supported(type_name) -> bool:
        return type_name in [
            'int',
            'str',
            'float',
            'complex',
            'bool',
            'range',
            'bytes',
            'bytearray',
            'memoryview'
        ]

    @staticmethod
    def create(type_name, field_name: str = None, use_fake_data: bool = False):
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
        elif type_name == 'range':
            return RangeGenerator()
        elif type_name == 'bytes':
            return BytesGenerator()
        elif type_name == 'bytearray':
            return ByteArrayGenerator()
        elif type_name == 'memoryview':
            return MemoryViewGenerator()
