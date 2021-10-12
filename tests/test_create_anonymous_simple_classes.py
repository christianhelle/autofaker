import unittest

from autofaker import Autodata


class AnonymousSimpleClassTestCase(unittest.TestCase):

    def test_create_local_class_returns_not_none(self):
        class X:
            pass

        self.assertIsNotNone(Autodata.create(X))

    def test_create_local_class_returns_instance(self):
        class X:
            pass

        self.assertIsInstance(Autodata.create(X), X)

    def test_create_simple_class_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(SimpleClass))

    def test_create_simple_class_returns_instance(self):
        self.assertIsInstance(Autodata.create(SimpleClass), SimpleClass)

    def test_create_simple_class_returns_instance_with_new_values(self):
        result = Autodata.create(SimpleClass)
        self.assertNotEqual(result.id, SimpleClass().id)
        self.assertNotEqual(result.text, SimpleClass().text)


class SimpleClass:
    id = 123
    text = 'test'
