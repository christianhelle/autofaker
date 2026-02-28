import datetime
import decimal
import pathlib
import random
import unittest
import uuid
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


class AnonymousTupleListTestCase(CreateManyTestCase):
    def getType(self):
        return tuple


class AnonymousSetListTestCase(CreateManyTestCase):
    def getType(self):
        return set


class AnonymousFrozenSetListTestCase(CreateManyTestCase):
    def getType(self):
        return frozenset


class AnonymousDictListTestCase(CreateManyTestCase):
    def getType(self):
        return dict


class AnonymousDecimalListTestCase(CreateManyTestCase):
    def getType(self):
        return decimal.Decimal


class AnonymousUUIDListTestCase(CreateManyTestCase):
    def getType(self):
        return uuid.UUID


class AnonymousPathListTestCase(CreateManyTestCase):
    def getType(self):
        return pathlib.Path


class AnonymousTimeListTestCase(CreateManyTestCase):
    def getType(self):
        return datetime.time


class AnonymousTimedeltaListTestCase(CreateManyTestCase):
    def getType(self):
        return datetime.timedelta
