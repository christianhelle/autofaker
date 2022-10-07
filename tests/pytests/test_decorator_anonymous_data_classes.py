import dataclasses
from dataclasses import dataclass

from autofaker import autodata, fakedata


@dataclass
class DataClass:
    id: int
    name: str
    text: str


# Anonymous DataClass Via Decorator Test Cases

@autodata(DataClass)
def test_create_data_class_using_decorator_returns_not_none(instance):
    assert instance is not None


@autodata(DataClass)
def test_create_data_class_using_decorator_returns_dataclass(instance):
    assert dataclasses.is_dataclass(instance)


@autodata(DataClass)
def test_create_data_class_returns_instance_with_new_values(instance):
    assert instance.id != int()
    assert instance.name != str()
    assert instance.text != str()


@autodata()
def test_create_data_class_argument_returns_instance_with_new_values(instance: DataClass):
    assert instance.id != int()
    assert instance.name != str()
    assert instance.text != str()


@autodata()
def test_create_anonymous_data_class_returns_instance_with_new_values(instance: DataClass):
    assert instance.id != int()
    assert instance.name != str()
    assert instance.text != str()


@fakedata()
def test_create_fake_data_class_returns_instance_with_new_values(instance: DataClass):
    assert instance.id != int()
    assert instance.name != str()
    assert instance.text != str()


# Anonymous DataClass Via Decorator With Fakes Test Cases

@autodata(DataClass, use_fake_data=True)
def test_create_data_class_using_decorator_returns_not_none_with_fake_data(instance):
    assert instance is not None


@autodata(DataClass, use_fake_data=True)
def test_create_data_class_using_decorator_returns_dataclass_with_fake_data(instance):
    assert dataclasses.is_dataclass(instance)


@autodata(DataClass, use_fake_data=True)
def test_create_data_class_returns_instance_with_new_values_with_fake_data(instance):
    assert instance.id != int()
    assert instance.text != str()


@autodata(use_fake_data=True)
def test_create_data_class_argument_returns_instance_with_new_values_with_fake_data(instance: DataClass):
    assert instance.id != int()
    assert instance.name != str()
    assert instance.text != str()


@fakedata()
def test_create_fake_data_class_returns_instance_with_new_values_with_fake_data(instance: DataClass):
    assert instance.id != int()
    assert instance.name != str()
    assert instance.text != str()
