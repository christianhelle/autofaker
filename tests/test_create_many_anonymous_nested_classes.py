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

    def test_create_many_nested_class_returns_not_none(self):
        self.assertIsNotNone(Autodata.create_many(NestedClass))

    def test_create_many_nested_class_returns_list(self):
        self.assertIsInstance(Autodata.create_many(NestedClass), list)

    def test_create_many_nested_class_returns_list_with_not_none(self):
        result = Autodata.create_many(NestedClass)
        for item in result:
            self.assertIsNotNone(item.inner)

    def test_create_many_nested_class_returns_instance_with_new_nested_instance(self):
        result = Autodata.create_many(NestedClass)
        for item in result:
            self.assertNotEqual(item.id, NestedClass().id)
            self.assertNotEqual(item.inner.id, SimpleClass().id)
            self.assertNotEqual(item.inner.text, SimpleClass().text)


class AnonymousDoubleNestedClassTestCase(unittest.TestCase):

    def test_create_many_nested_class_returns_not_none(self):
        self.assertIsNotNone(Autodata.create_many(DoubleNestedClass))

    def test_create_many_nested_class_returns_instance(self):
        self.assertIsInstance(Autodata.create_many(DoubleNestedClass), list)

    def test_create_many_nested_class_returns_instance_with_nested_not_none(self):
        result = Autodata.create_many(DoubleNestedClass)
        for item in result:
            self.assertIsNotNone(item)
            self.assertIsNotNone(item.inner)

    def test_create_many_nested_class_returns_instance_with_new_nested_instance(self):
        result = Autodata.create_many(DoubleNestedClass)
        for item in result:
            self.assertNotEqual(item.id, DoubleNestedClass().id)
            self.assertNotEqual(item.inner, NestedClass())

    def test_create_many_nested_class_returns_instance_with_new_double_nested_instance(self):
        result = Autodata.create_many(DoubleNestedClass)
        for item in result:
            self.assertNotEqual(item.id, DoubleNestedClass().id)
            self.assertNotEqual(item.inner.inner.id, SimpleClass().id)
            self.assertNotEqual(item.inner.inner.text, SimpleClass().text)
