from autofaker.builtins import (
    BooleanGenerator,
    ByteArrayGenerator,
    BytesGenerator,
    ComplexGenerator,
    DecimalGenerator,
    DictGenerator,
    FloatGenerator,
    FrozenSetGenerator,
    IntegerGenerator,
    MemoryViewGenerator,
    PathGenerator,
    RangeGenerator,
    SetGenerator,
    TupleGenerator,
    UUIDGenerator,
)
from autofaker.fakes import FakeIntegerGenerator, FakeStringGenerator, StringGenerator


class BuiltinTypeDataGeneratorFactory:
    @staticmethod
    def is_supported(type_name) -> bool:
        return type_name in [
            "int",
            "str",
            "float",
            "complex",
            "bool",
            "range",
            "bytes",
            "bytearray",
            "memoryview",
            "tuple",
            "set",
            "frozenset",
            "dict",
            "decimal",
            "uuid",
            "posixpath",
            "windowspath",
            "path",
        ]

    @staticmethod
    def create(type_name, field_name: str = None, use_fake_data: bool = False):
        if type_name == "int":
            return (
                FakeIntegerGenerator()
                if use_fake_data is True
                else IntegerGenerator()
            )
        if type_name == "str":
            return (
                FakeStringGenerator(field_name)
                if field_name is not None and use_fake_data is True
                else StringGenerator()
            )
        if type_name == "float":
            return FloatGenerator()
        if type_name == "complex":
            return ComplexGenerator()
        if type_name == "bool":
            return BooleanGenerator()
        if type_name == "range":
            return RangeGenerator()
        if type_name == "bytes":
            return BytesGenerator()
        if type_name == "bytearray":
            return ByteArrayGenerator()
        if type_name == "memoryview":
            return MemoryViewGenerator()
        if type_name == "tuple":
            return TupleGenerator()
        if type_name == "set":
            return SetGenerator()
        if type_name == "frozenset":
            return FrozenSetGenerator()
        if type_name == "dict":
            return DictGenerator()
        if type_name == "decimal":
            return DecimalGenerator()
        if type_name == "uuid":
            return UUIDGenerator()
        if type_name in ("posixpath", "windowspath", "path"):
            return PathGenerator()
