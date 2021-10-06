import unittest

from pyautodata import Fixture


class SimpleClass:
    id = 123
    text = 'test'


class NestedWithCollectionClass:
    id = 123
    text = 'test'
    inner = [SimpleClass(), SimpleClass()]


class NestedWithNestedCollectionClass:
    id = 123
    text = 'test'
    inner = [NestedWithCollectionClass(), NestedWithCollectionClass()]


class AnonymousNestedClassWithCollectionTestCase(unittest.TestCase):

    def test_create_nested_class_returns_not_none(self):
        self.assertIsNotNone(Fixture.create(NestedWithCollectionClass))

    def test_create_nested_class_returns_instance(self):
        self.assertIsInstance(Fixture.create(NestedWithCollectionClass), NestedWithCollectionClass)

    def test_create_nested_class_returns_instance_with_nested_not_none(self):
        self.assertIsNotNone(Fixture.create(NestedWithCollectionClass).inner)

    def test_create_nested_class_returns_instance_with_nested_not_empty(self):
        self.assertNotEqual(0, len(Fixture.create(NestedWithCollectionClass).inner))

    def test_create_nested_class_returns_instance_with_new_nested_instance(self):
        result = Fixture.create(NestedWithCollectionClass)
        self.assertNotEqual(result.id, NestedWithCollectionClass().id)
        for cls in result.inner:
            self.assertIsNotNone(cls)
            self.assertNotEqual(cls.id, SimpleClass().id)
            self.assertNotEqual(cls.text, SimpleClass().text)


class AnonymousNestedClassWithNestedCollectionTestCase(unittest.TestCase):

    def test_create_nested_class_returns_not_none(self):
        self.assertIsNotNone(Fixture.create(NestedWithCollectionClass))

    def test_create_nested_class_returns_instance(self):
        self.assertIsInstance(Fixture.create(NestedWithCollectionClass), NestedWithCollectionClass)

    def test_create_nested_class_returns_instance_with_inner_not_none(self):
        self.assertIsNotNone(Fixture.create(NestedWithNestedCollectionClass).inner)

    def test_create_nested_class_returns_instance_with_inner_not_empty(self):
        self.assertNotEqual(0, len(Fixture.create(NestedWithNestedCollectionClass).inner))

    def test_create_nested_class_returns_instance_with_nested_inner_not_empty(self):
        self.assertNotEqual(0, len(Fixture.create(NestedWithNestedCollectionClass).inner[0].inner))

    def test_create_nested_class_returns_instance_with_new_nested_instance(self):
        result = Fixture.create(NestedWithNestedCollectionClass)
        self.assertNotEqual(result.id, NestedWithNestedCollectionClass().id)
        self.assertNotEqual(result.text, NestedWithNestedCollectionClass().text)
        for cls in result.inner:
            self.assertIsNotNone(cls)
            self.assertNotEqual(cls.id, NestedWithCollectionClass().id)
            self.assertNotEqual(cls.text, NestedWithCollectionClass().text)
            for inner in cls.inner:
                self.assertNotEqual(inner.id, SimpleClass().id)
                self.assertNotEqual(inner.text, SimpleClass().text)