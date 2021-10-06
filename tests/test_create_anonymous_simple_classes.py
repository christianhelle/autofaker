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
