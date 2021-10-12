import unittest

from autofaker import Autodata


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
        self.assertIsNotNone(Autodata.create(NestedClass))

    def test_create_nested_class_returns_instance(self):
        self.assertIsInstance(Autodata.create(NestedClass), NestedClass)

    def test_create_nested_class_returns_instance_with_nested_not_none(self):
        self.assertIsNotNone(Autodata.create(NestedClass).inner)

    def test_create_nested_class_returns_instance_with_new_nested_instance(self):
        result = Autodata.create(NestedClass)
        self.assertNotEqual(result.id, NestedClass().id)
        self.assertNotEqual(result.inner.id, SimpleClass().id)
        self.assertNotEqual(result.inner.text, SimpleClass().text)


class AnonymousDoubleNestedClassTestCase(unittest.TestCase):

    def test_create_nested_class_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(DoubleNestedClass))

    def test_create_nested_class_returns_instance(self):
        self.assertIsInstance(Autodata.create(DoubleNestedClass), DoubleNestedClass)

    def test_create_nested_class_returns_instance_with_nested_not_none(self):
        self.assertIsNotNone(Autodata.create(DoubleNestedClass).inner)

    def test_create_nested_class_returns_instance_with_new_nested_instance(self):
        result = Autodata.create(DoubleNestedClass)
        self.assertNotEqual(result.id, DoubleNestedClass().id)
        self.assertNotEqual(result.inner, NestedClass())

    def test_create_nested_class_returns_instance_with_new_double_nested_instance(self):
        result = Autodata.create(DoubleNestedClass)
        self.assertNotEqual(result.id, DoubleNestedClass().id)
        self.assertNotEqual(result.inner.inner.id, SimpleClass().id)
        self.assertNotEqual(result.inner.inner.text, SimpleClass().text)
