import random
import unittest
from abc import abstractmethod

from autofaker import Autodata


class CreateManyTestCase(unittest.TestCase):
    @abstractmethod
    def getType(self):
        pass

    def test_create_many_returns_not_none(self):
        if self.getType() is None:
            return
        self.assertIsNotNone(Autodata.create_many(self.getType()))

    def test_create_many_returns_list(self):
        if self.getType() is None:
            return
        self.assertIsInstance(Autodata.create_many(self.getType()), list)

    def test_create_many_with_size_returns(self):
        if self.getType() is None:
            return
        size = random.randint(1, 10)
        self.assertEqual(len(Autodata.create_many(self.getType(), size)), size)

    def test_create_many_returns_non_default(self):
        if self.getType() is None:
            return
        self.assertNotEqual(Autodata.create_many(self.getType()), [self.getType()()])


class AnonymousStringListTestCase(CreateManyTestCase):
    def getType(self):
        return str


class AnonymousIntegerListTestCase(CreateManyTestCase):
    def getType(self):
        return int


class AnonymousFloatListTestCase(CreateManyTestCase):
    def getType(self):
        return float


class AnonymousBooleanListTestCase(CreateManyTestCase):
    def getType(self):
        return bool
