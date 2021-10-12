import random
import unittest

from autofaker import Autodata


class SimpleClass:
    id = 123
    text = 'test'


class AnonymousSimpleClassTestCase(unittest.TestCase):
    def test_create_many_returns_not_none(self):
        self.assertIsNotNone(Autodata.create_many(SimpleClass))

    def test_create_many_returns_list(self):
        self.assertIsInstance(Autodata.create_many(SimpleClass), list)

    def test_create_many_with_size_returns(self):
        size = random.randint(1, 10)
        self.assertEqual(len(Autodata.create_many(SimpleClass, size)), size)

    def test_create_many_returns_non_default(self):
        self.assertNotEqual(Autodata.create_many(SimpleClass), [SimpleClass()])

    def test_create_many_local_class_returns_not_none(self):
        class X:
            pass
        self.assertIsNotNone(Autodata.create_many(X))

    def test_create_many_local_class_returns_instance(self):
        class X:
            pass
        self.assertIsInstance(Autodata.create_many(X), list)

    def test_create_many_local_returns_non_default(self):
        class X:
            pass
        self.assertNotEqual(Autodata.create_many(X), [X()])
