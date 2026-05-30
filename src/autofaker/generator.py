import dataclasses
import inspect

import typing_inspect

from autofaker import registry
from autofaker.registry import get_type_name
from autofaker.attributes import Attributes
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
from autofaker.dates import (
    DateGenerator, DatetimeGenerator, TimeGenerator, TimedeltaGenerator,
    is_date_type,
)
from autofaker.enums import EnumGenerator, is_enum
from autofaker.fakes import (
    FakeIntegerGenerator, FakeStringGenerator, StringGenerator,
    TypeDataGeneratorBase,
)
from autofaker.literals import LiteralGenerator, is_literal_type


class TypeDataGenerator:
    @staticmethod
    def create(
        t, field_name: str = None, use_fake_data: bool = False
    ) -> TypeDataGeneratorBase:
        return registry.resolve(t, field_name, use_fake_data)

    @staticmethod
    def create_datetime(type_name):
        if type_name == "datetime":
            return DatetimeGenerator()
        if type_name == "date":
            return DateGenerator()
        if type_name == "time":
            return TimeGenerator()
        if type_name == "timedelta":
            return TimedeltaGenerator()

    @staticmethod
    def _is_optional(t):
        return typing_inspect.is_optional_type(t)

    @staticmethod
    def _get_type_name(t) -> str:
        return registry.get_type_name(t)


class DataClassGenerator(TypeDataGeneratorBase):
    def __init__(self, cls, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        self.cls = cls

    def generate(self):
        fields = dataclasses.fields(self.cls)
        params = {}
        for dataclass_field in fields:
            field_type = dataclass_field.type
            generator = TypeDataGenerator.create(
                field_type, dataclass_field.name, use_fake_data=self.use_fake_data
            )
            params[dataclass_field.name] = generator.generate()
        instance = self.cls(**params)
        return instance


class ClassGenerator(TypeDataGeneratorBase):
    def __init__(self, cls, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        self._try_create_instance(cls)

    def generate(self):
        if not self._is_supported():
            return None

        attributes = Attributes(self.instance)
        members = attributes.get_members()

        for member in members:
            attr = attributes.get_attribute(member)
            if type(attr).__name__ == "list":
                for i in range(len(attr)):
                    attr[i] = self._try_generate(attr[i])
            else:
                attributes.set_value(member, self._try_generate(attr))

        # Handle annotated attributes (especially Literal types)
        # In Python 3.14+, PEP 649 requires accessing __annotations__ from the class type
        # Falls back to instance __annotations__ for Python 3.10-3.13 compatibility
        annotations = {}
        if hasattr(type(self.instance), '__annotations__'):
            annotations = type(self.instance).__annotations__
        elif hasattr(self.instance, '__annotations__'):
            annotations = self.instance.__annotations__
        
        for key, value in (annotations or {}).items():
            if key not in members:
                if is_literal_type(value):
                    v = LiteralGenerator(value).generate()
                    self.instance.__dict__[key] = v

        return self.instance

    def _is_supported(self):
        import pandas

        unsupported_types = [pandas.core.frame.DataFrame]
        for t in unsupported_types:
            if isinstance(self.instance, t):
                return False
        return True

    def _try_generate(self, attr):
        try:
            generator = TypeDataGenerator.create(
                type(attr), use_fake_data=self.use_fake_data
            )
            return generator.generate()
        except TypeError as e:
            print(e)

    def _try_create_instance(self, cls):
        try:
            self.instance = cls()
        except TypeError:
            self._create_with_init_args(cls)

    def _create_with_init_args(self, cls):
        init_args = inspect.getfullargspec(cls.__init__)
        values = []
        for key, t in init_args.annotations.items():
            if key == 'return':
                continue
            origin = typing_inspect.get_origin(t)
            if origin == list:
                list_arg = typing_inspect.get_args(t)
                if not list_arg:
                    values.append([])
                    continue
                items = []
                for _ in range(3):
                    generator = TypeDataGenerator.create(
                        list_arg[0], use_fake_data=self.use_fake_data
                    )
                    items.append(generator.generate())
                values.append(items)
            else:
                generator = TypeDataGenerator.create(
                    t, use_fake_data=self.use_fake_data
                )
                value = generator.generate()
                values.append(value)
        self.instance = cls(*tuple(values))


class ListGenerator(TypeDataGeneratorBase):
    def __init__(self, t, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        self.list_arg = typing_inspect.get_args(t)

    def generate(self):
        if not self.list_arg:
            return []
        items = []
        for _ in range(3):
            generator = TypeDataGenerator.create(
                self.list_arg[0], use_fake_data=self.use_fake_data
            )
            items.append(generator.generate())
        return items


class TypedTupleGenerator(TypeDataGeneratorBase):
    def __init__(self, t, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        self.args = typing_inspect.get_args(t)

    def generate(self):
        items = []
        # Handle variable-length tuples of the form Tuple[T, ...]
        if len(self.args) == 2 and self.args[1] is Ellipsis:
            elem_type = self.args[0]
            for _ in range(3):
                generator = TypeDataGenerator.create(
                    elem_type, use_fake_data=self.use_fake_data
                )
                items.append(generator.generate())
        else:
            # Handle fixed-length typed tuples, e.g., Tuple[int, str]
            for arg in self.args:
                generator = TypeDataGenerator.create(
                    arg, use_fake_data=self.use_fake_data
                )
                items.append(generator.generate())
        return tuple(items)


class TypedSetGenerator(TypeDataGeneratorBase):
    def __init__(self, t, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        self.set_arg = typing_inspect.get_args(t)

    def generate(self):
        items = set()
        target_size = 3
        max_attempts = 10 * target_size
        attempts = 0
        while len(items) < target_size and attempts < max_attempts:
            generator = TypeDataGenerator.create(
                self.set_arg[0], use_fake_data=self.use_fake_data
            )
            items.add(generator.generate())
            attempts += 1
        return items


class TypedFrozenSetGenerator(TypeDataGeneratorBase):
    def __init__(self, t, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        self.set_arg = typing_inspect.get_args(t)

    def generate(self):
        items = set()
        target_size = 3
        max_attempts = 10 * target_size
        attempts = 0
        while len(items) < target_size and attempts < max_attempts:
            generator = TypeDataGenerator.create(
                self.set_arg[0], use_fake_data=self.use_fake_data
            )
            items.add(generator.generate())
            attempts += 1
        return frozenset(items)


class TypedDictGenerator(TypeDataGeneratorBase):
    def __init__(self, t, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        args = typing_inspect.get_args(t)
        self.key_type = args[0]
        self.value_type = args[1]

    def generate(self):
        result = {}
        target_size = 3
        max_attempts = 10 * target_size
        attempts = 0
        while len(result) < target_size and attempts < max_attempts:
            key_gen = TypeDataGenerator.create(
                self.key_type, use_fake_data=self.use_fake_data
            )
            val_gen = TypeDataGenerator.create(
                self.value_type, use_fake_data=self.use_fake_data
            )
            result[key_gen.generate()] = val_gen.generate()
            attempts += 1
        return result


class OptionalGenerator(TypeDataGeneratorBase):
    def __init__(self, t, use_fake_data: bool = False):
        self.use_fake_data = use_fake_data
        args = typing_inspect.get_args(t)
        # Optional[X] is Union[X, None], get the non-None type
        self.inner_type = next(a for a in args if a is not type(None))

    def generate(self):
        generator = TypeDataGenerator.create(
            self.inner_type, use_fake_data=self.use_fake_data
        )
        return generator.generate()


# --- built-in scalar dispatch (absorbs the former factory.py) --------------

_BUILTIN_GENERATORS = {
    "int": lambda f, u: FakeIntegerGenerator() if u else IntegerGenerator(),
    "str": lambda f, u: (
        FakeStringGenerator(f) if (f is not None and u) else StringGenerator()
    ),
    "float": lambda f, u: FloatGenerator(),
    "complex": lambda f, u: ComplexGenerator(),
    "bool": lambda f, u: BooleanGenerator(),
    "range": lambda f, u: RangeGenerator(),
    "bytes": lambda f, u: BytesGenerator(),
    "bytearray": lambda f, u: ByteArrayGenerator(),
    "memoryview": lambda f, u: MemoryViewGenerator(),
    "tuple": lambda f, u: TupleGenerator(),
    "set": lambda f, u: SetGenerator(),
    "frozenset": lambda f, u: FrozenSetGenerator(),
    "dict": lambda f, u: DictGenerator(),
    "decimal": lambda f, u: DecimalGenerator(),
    "uuid": lambda f, u: UUIDGenerator(),
    "posixpath": lambda f, u: PathGenerator(),
    "windowspath": lambda f, u: PathGenerator(),
    "path": lambda f, u: PathGenerator(),
}


def _register_builtin_rules():
    """Register the built-in resolution rules in precedence order.

    Order is significant and mirrors the original dispatch: typed generics
    first, then Optional, then scalars/builtins, dates, the bare ``list``,
    enum, and finally Literal. The dataclass/class fallback is set separately
    and always runs last.
    """
    _b = registry._register_builtin

    _b(
        lambda t, n: typing_inspect.get_origin(t) is list
        or (n == "list" and typing_inspect.get_args(t)),
        lambda t, f, u: ListGenerator(t, use_fake_data=u),
    )
    _b(
        lambda t, n: typing_inspect.get_origin(t) is tuple
        and typing_inspect.get_args(t),
        lambda t, f, u: TypedTupleGenerator(t, use_fake_data=u),
    )
    _b(
        lambda t, n: typing_inspect.get_origin(t) is set
        and typing_inspect.get_args(t),
        lambda t, f, u: TypedSetGenerator(t, use_fake_data=u),
    )
    _b(
        lambda t, n: typing_inspect.get_origin(t) is frozenset
        and typing_inspect.get_args(t),
        lambda t, f, u: TypedFrozenSetGenerator(t, use_fake_data=u),
    )
    _b(
        lambda t, n: typing_inspect.get_origin(t) is dict
        and typing_inspect.get_args(t),
        lambda t, f, u: TypedDictGenerator(t, use_fake_data=u),
    )
    _b(
        lambda t, n: typing_inspect.is_optional_type(t),
        lambda t, f, u: OptionalGenerator(t, use_fake_data=u),
    )
    _b(
        lambda t, n: n in _BUILTIN_GENERATORS,
        lambda t, f, u: _BUILTIN_GENERATORS[get_type_name(t).lower()](f, u),
    )
    _b(
        lambda t, n: is_date_type(n),
        lambda t, f, u: TypeDataGenerator.create_datetime(get_type_name(t).lower()),
    )
    _b(
        lambda t, n: n == "list",
        lambda t, f, u: ListGenerator(t, use_fake_data=u),
    )
    _b(
        lambda t, n: is_enum(t),
        lambda t, f, u: EnumGenerator(t),
    )
    _b(
        lambda t, n: is_literal_type(t),
        lambda t, f, u: LiteralGenerator(t),
    )

    registry._set_fallback(
        lambda t, f, u: (
            DataClassGenerator(t, use_fake_data=u)
            if dataclasses.is_dataclass(t)
            else ClassGenerator(t, use_fake_data=u)
        )
    )


_register_builtin_rules()
