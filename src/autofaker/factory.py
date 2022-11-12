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
        if type_name == 'str':
            return FakeStringGenerator(field_name) \
                if field_name is not None and use_fake_data is True \
                else StringGenerator()
        if type_name == 'float':
            return FloatGenerator()
        if type_name == 'complex':
            return ComplexGenerator()
        if type_name == 'bool':
            return BooleanGenerator()
        if type_name == 'range':
            return RangeGenerator()
        if type_name == 'bytes':
            return BytesGenerator()
        if type_name == 'bytearray':
            return ByteArrayGenerator()
        if type_name == 'memoryview':
            return MemoryViewGenerator()
