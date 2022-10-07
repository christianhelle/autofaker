import dataclasses
from dataclasses import dataclass

from autofaker import autodata, fakedata


@dataclass
class SimpleClass:
    id: int
    name: str
    text: str


@dataclass
class NestedClass:
    id: int
    name: str
    text: str
    inner: SimpleClass


@dataclass
class DoubleNestedClass:
    id: int
    name: str
    text: str
    inner: NestedClass


# Anonymous Nested Class Via Decorator Test Cases

@autodata(NestedClass)
def test_create_nested_class_using_decorator_returns_not_none(instance):
    assert instance is not None


@autodata(NestedClass)
def test_create_nested_class_using_decorator_returns_dataclass(instance):
    assert dataclasses.is_dataclass(instance)


@autodata(NestedClass)
def test_create_nested_class_returns_instance_with_new_values(instance):
    assert instance.id != 0
    assert instance.inner.id != 0
    assert instance.inner.text != str()


@autodata()
def test_create_nested_class_argument_returns_instance_with_new_values(instance: NestedClass):
    assert instance.id != 0
    assert instance.name != str()
    assert instance.text != str()


@autodata()
def test_create_anonymous_nested_class_returns_instance_with_new_values(instance: NestedClass):
    assert instance.id != 0
    assert instance.name != str()
    assert instance.text != str()


@fakedata()
def test_create_fake_nested_class_returns_instance_with_new_values(instance: NestedClass):
    assert instance.id != 0
    assert instance.name != str()
    assert instance.text != str()


# Anonymous Double Nested Class Via Decorator With Fakes Test Cases

@autodata(DoubleNestedClass, use_fake_data=True)
def test_create_double_nested_class_using_decorator_returns_not_none(instance):
    assert instance is not None


@autodata(DoubleNestedClass, use_fake_data=True)
def test_create_nested_class_using_decorator_returns_dataclass(instance):
    assert dataclasses.is_dataclass(instance)


@autodata(DoubleNestedClass, use_fake_data=True)
def test_create_double_nested_class_returns_instance_with_new_values(instance):
    assert instance.id != 0
    assert instance.inner.inner.id != 0
    assert instance.inner.inner.text != str()


@autodata(use_fake_data=True)
def test_create_double_nested_class_argument_using_decorator_returns_not_none(instance: DoubleNestedClass):
    assert instance is not None


@fakedata()
def test_create_double_nested_class_argument_returns_instance_with_new_values(instance: DoubleNestedClass):
    assert instance.id != 0
    assert instance.inner.inner.id != 0
    assert instance.inner.inner.text != str()
