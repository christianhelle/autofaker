import unittest

from pyautodata import Fixture


class SimpleClass:
    id = 123
    text = 'test'


class NestedClass:
    id = 123
    text = 'test'
    inner = SimpleClass()


class DoubleNestedClass:
    id = 123
    text = 'test'
    inner = NestedClass()


class AnonymousNestedClassTestCase(unittest.TestCase):

    def test_create_nested_class_returns_not_none(self):
        self.assertIsNotNone(Fixture.create(NestedClass))

    def test_create_nested_class_returns_instance(self):
        self.assertIsInstance(Fixture.create(NestedClass), NestedClass)

    def test_create_nested_class_returns_instance_with_nested_not_none(self):
        self.assertIsNotNone(Fixture.create(NestedClass).inner)

    def test_create_nested_class_returns_instance_with_new_nested_instance(self):
        result = Fixture.create(NestedClass)
        self.assertNotEqual(result.id, NestedClass().id)
        self.assertNotEqual(result.inner.id, SimpleClass().id)
        self.assertNotEqual(result.inner.text, SimpleClass().text)


class AnonymousDoubleNestedClassTestCase(unittest.TestCase):

    def test_create_nested_class_returns_not_none(self):
        self.assertIsNotNone(Fixture.create(DoubleNestedClass))

    def test_create_nested_class_returns_instance(self):
        self.assertIsInstance(Fixture.create(DoubleNestedClass), DoubleNestedClass)

    def test_create_nested_class_returns_instance_with_nested_not_none(self):
        self.assertIsNotNone(Fixture.create(DoubleNestedClass).inner)

    def test_create_nested_class_returns_instance_with_new_nested_instance(self):
        result = Fixture.create(DoubleNestedClass)
        self.assertNotEqual(result.id, DoubleNestedClass().id)
        self.assertNotEqual(result.inner, NestedClass())

    def test_create_nested_class_returns_instance_with_new_double_nested_instance(self):
        result = Fixture.create(DoubleNestedClass)
        self.assertNotEqual(result.id, DoubleNestedClass().id)
        self.assertNotEqual(result.inner.inner.id, SimpleClass().id)
        self.assertNotEqual(result.inner.inner.text, SimpleClass().text)
