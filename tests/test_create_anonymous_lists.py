import unittest
from abc import abstractmethod
from datetime import datetime, date

from typing import List

from autofaker import Autodata


class CreateTestCase(unittest.TestCase):
    @abstractmethod
    def getType(self):
        pass

    def test_create_returns_not_none(self):
        if self.getType() is None:
            return
        self.assertIsNotNone(Autodata.create(self.getType()))

    def test_create_returns_not_type(self):
        if self.getType() is None:
            return
        self.assertNotIsInstance(Autodata.create(self.getType()), type)

    def test_create_returns_not_default(self):
        if self.getType() is None or self.getType() is bool:
            return
        sut = Autodata.create(self.getType())
        self.assertNotEqual(sut, list())


class AnonymousIntegerListTestCase(CreateTestCase):
    def getType(self):
        return List[int]


class AnonymousStringListTestCase(CreateTestCase):
    def getType(self):
        return List[str]


class AnonymousFloatListTestCase(CreateTestCase):
    def getType(self):
        return List[float]


class AnonymousBooleanListTestCase(CreateTestCase):
    def getType(self):
        return List[bool]


class AnonymousComplexListTestCase(CreateTestCase):
    def getType(self):
        return List[complex]


class AnonymousDatetimeListTestCase(CreateTestCase):
    def getType(self):
        return List[datetime]


class AnonymousDateListTestCase(CreateTestCase):
    def getType(self):
        return List[date]


