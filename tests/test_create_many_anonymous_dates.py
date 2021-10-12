import unittest
from abc import abstractmethod
from datetime import date, datetime
import random

from autofaker import Autodata


class CreateManyTestCase(unittest.TestCase):
    @abstractmethod
    def getType(self):
        pass

    def test_create_many_returns_not_none(self):
        if self.getType() is None:
            return
        self.assertIsNotNone(Autodata.create_many(self.getType()))

    def test_create_many_returns_returns_list(self):
        if self.getType() is None:
            return
        self.assertIsInstance(Autodata.create_many(self.getType()), list)

    def test_create_many_with_size_returns(self):
        if self.getType() is None:
            return
        size = random.randint(1, 10)
        self.assertEqual(len(Autodata.create_many(self.getType(), size)), size)

    def test_create_many_returns_list_with_non_defaults(self):
        if self.getType() is None:
            return
        self.assertNotEqual(Autodata.create_many(self.getType()), [self.getType()(1970, 1, 1)])


class AnonymousDatetimeListTestCase(CreateManyTestCase):
    def getType(self):
        return datetime


class AnonymousDateListTestCase(CreateManyTestCase):
    def getType(self):
        return date
