import unittest

from autofaker import Autodata


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

    def test_create_many_nested_class_returns_not_none(self):
        self.assertIsNotNone(Autodata.create_many(NestedWithCollectionClass))

    def test_create_many_nested_class_returns_list(self):
        self.assertIsInstance(Autodata.create_many(NestedWithCollectionClass), list)

    def test_create_many_nested_class_returns_instances_with_nested_not_none(self):
        result = Autodata.create_many(NestedWithCollectionClass)
        for item in result:
            self.assertIsNotNone(item.inner)

    def test_create_many_nested_class_returns_instances_with_nested_not_empty(self):
        result = Autodata.create_many(NestedWithCollectionClass)
        for item in result:
            self.assertNotEqual(0, len(item.inner))

    def test_create_many_nested_class_returns_instances_with_new_nested_instance(self):
        result = Autodata.create_many(NestedWithCollectionClass)
        for item in result:
            self.assertNotEqual(item.id, NestedWithCollectionClass().id)
            for cls in item.inner:
                self.assertIsNotNone(cls)
                self.assertNotEqual(cls.id, SimpleClass().id)
                self.assertNotEqual(cls.text, SimpleClass().text)


class AnonymousNestedClassWithNestedCollectionTestCase(unittest.TestCase):

    def test_create_many_nested_class_returns_not_none(self):
        self.assertIsNotNone(Autodata.create_many(NestedWithCollectionClass))

    def test_create_many_nested_class_returns_list(self):
        self.assertIsInstance(Autodata.create_many(NestedWithCollectionClass), list)

    def test_create_many_nested_class_returns_instances_with_inner_not_none(self):
        result = Autodata.create_many(NestedWithNestedCollectionClass)
        for item in result:
            self.assertIsNotNone(item.inner)

    def test_create_many_nested_class_returns_instances_with_inner_not_empty(self):
        result = Autodata.create_many(NestedWithNestedCollectionClass)
        for item in result:
            self.assertNotEqual(0, len(item.inner))

    def test_create_many_nested_class_returns_instances_with_nested_inner_not_empty(self):
        result = Autodata.create_many(NestedWithNestedCollectionClass)
        for item in result:
            for cls in item.inner:
                self.assertNotEqual(0, len(cls.inner))

    def test_create_many_nested_class_returns_instances_with_new_nested_instances(self):
        result = Autodata.create_many(NestedWithNestedCollectionClass)
        for root in result:
            self.assertNotEqual(root.id, NestedWithNestedCollectionClass().id)
            self.assertNotEqual(root.text, NestedWithNestedCollectionClass().text)
            for inner in root.inner:
                self.assertNotEqual(inner.id, NestedWithCollectionClass().id)
                self.assertNotEqual(inner.text, NestedWithCollectionClass().text)
                for nested_inner in inner.inner:
                    self.assertNotEqual(nested_inner.id, SimpleClass().id)
                    self.assertNotEqual(nested_inner.text, SimpleClass().text)
