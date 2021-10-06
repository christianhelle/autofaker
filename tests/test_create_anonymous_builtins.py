import unittest
import uuid

from pyautodata import Fixture


class AnonymousIntegerTestCase(unittest.TestCase):
    def test_create_int_returns_not_none(self):
        self.assertIsNotNone(Fixture.create(int))

    def test_create_int_returns_not_type(self):
        self.assertNotIsInstance(Fixture.create(int), type)

    def test_create_int_returns_not_default(self):
        self.assertNotEqual(Fixture.create(int), 0)


class AnonymousStringTestCase(unittest.TestCase):
    def test_create_str_returns_not_none(self):
        self.assertIsNotNone(Fixture.create(str))

    def test_create_str_returns_not_type(self):
        self.assertNotIsInstance(Fixture.create(str), type)

    def test_create_str_returns_uuid_str(self):
        self.assertIsNotNone(uuid.UUID(Fixture.create(str)))


class AnonymousFloatTestCase(unittest.TestCase):
    def test_create_float_returns_not_none(self):
        self.assertIsNotNone(Fixture.create(float))

    def test_create_float_returns_not_type(self):
        self.assertNotIsInstance(Fixture.create(float), type)

    def test_create_float_returns_not_default(self):
        self.assertNotEqual(Fixture.create(float), float())


