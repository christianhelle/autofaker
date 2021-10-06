import random
import unittest

from pyautodata import Fixture


class SimpleClass:
    id = 123
    text = 'test'


class CreateManyTestCase(unittest.TestCase):
    def test_create_many_returns_not_none(self):
        self.assertIsNotNone(Fixture.create_many(SimpleClass))

    def test_create_many_returns_list(self):
        self.assertIsInstance(Fixture.create_many(SimpleClass), list)

    def test_create_many_with_size_returns(self):
        size = random.randint(1, 10)
        self.assertEqual(len(Fixture.create_many(SimpleClass, size)), size)

    def test_create_many_returns_non_default(self):
        self.assertNotEqual(Fixture.create_many(SimpleClass), [SimpleClass()])
