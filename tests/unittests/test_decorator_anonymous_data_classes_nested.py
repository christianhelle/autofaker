import dataclasses
import unittest
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


class AnonymousNestedClassViaDecoratorTestCase(unittest.TestCase):

    @autodata(NestedClass)
    def test_create_nested_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @autodata(NestedClass)
    def test_create_nested_class_using_decorator_returns_dataclass(self, instance):
        self.assertTrue(dataclasses.is_dataclass(instance))

    @autodata(NestedClass)
    def test_create_nested_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, 0)
        self.assertNotEqual(instance.inner.id, 0)
        self.assertNotEqual(instance.inner.text, str())

    @autodata()
    def test_create_nested_class_argument_returns_instance_with_new_values(self, instance: NestedClass):
        self.assertNotEqual(instance.id, 0)
        self.assertNotEqual(instance.name, str())
        self.assertNotEqual(instance.text, str())

    @autodata()
    def test_create_anonymous_nested_class_returns_instance_with_new_values(self, instance: NestedClass):
        self.assertNotEqual(instance.id, 0)
        self.assertNotEqual(instance.name, str())
        self.assertNotEqual(instance.text, str())

    @fakedata()
    def test_create_fake_nested_class_returns_instance_with_new_values(self, instance: NestedClass):
        self.assertNotEqual(instance.id, 0)
        self.assertNotEqual(instance.name, str())
        self.assertNotEqual(instance.text, str())


class AnonymousDoubleNestedClassViaDecoratorWithFakesTestCase(unittest.TestCase):

    @autodata(DoubleNestedClass, use_fake_data=True)
    def test_create_double_nested_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @autodata(DoubleNestedClass, use_fake_data=True)
    def test_create_nested_class_using_decorator_returns_dataclass(self, instance):
        self.assertTrue(dataclasses.is_dataclass(instance))

    @autodata(DoubleNestedClass, use_fake_data=True)
    def test_create_double_nested_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, 0)
        self.assertNotEqual(instance.inner.inner.id, 0)
        self.assertNotEqual(instance.inner.inner.text, str())

    @autodata(use_fake_data=True)
    def test_create_double_nested_class_argument_using_decorator_returns_not_none(self, instance: DoubleNestedClass):
        self.assertIsNotNone(instance)

    @fakedata()
    def test_create_double_nested_class_argument_returns_instance_with_new_values(self, instance: DoubleNestedClass):
        self.assertNotEqual(instance.id, 0)
        self.assertNotEqual(instance.inner.inner.id, 0)
        self.assertNotEqual(instance.inner.inner.text, str())
