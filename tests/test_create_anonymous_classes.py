import unittest

from pyautodata import Fixture


class AnonymousSimpleClassTestCase(unittest.TestCase):

    def test_create_local_class_returns_not_none(self):
        class X:
            pass

        self.assertIsNotNone(Fixture.create(X))

    def test_create_local_class_returns_instance(self):
        class X:
            pass

        self.assertIsInstance(Fixture.create(X), X)

    def test_create_simple_class_returns_not_none(self):
        self.assertIsNotNone(Fixture.create(SimpleClass))

    def test_create_simple_class_returns_instance(self):
        self.assertIsInstance(Fixture.create(SimpleClass), SimpleClass)

    def test_create_simple_class_returns_instance_with_new_values(self):
        result = Fixture.create(SimpleClass)
        self.assertNotEqual(result.id, SimpleClass().id)
        self.assertNotEqual(result.text, SimpleClass().text)


class SimpleClass:
    id = 123
    text = 'test'


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


class NestedClass:
    id = 123
    text = 'test'
    inner = SimpleClass()


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


class NestedWithCollectionClass:
    id = 123
    text = 'test'
    inner = [SimpleClass(), SimpleClass()]


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
        print(result)


class NestedWithNestedCollectionClass:
    id = 123
    text = 'test'
    inner = [NestedWithCollectionClass(), NestedWithCollectionClass()]
