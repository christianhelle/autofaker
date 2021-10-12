import unittest
from abc import abstractmethod

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
        self.assertNotEqual(Autodata.create(self.getType()), self.getType()())


class AnonymousIntegerTestCase(CreateTestCase):
    def getType(self):
        return int


class AnonymousStringTestCase(CreateTestCase):
    def getType(self):
        return str


class AnonymousFloatTestCase(CreateTestCase):
    def getType(self):
        return float


class AnonymousBooleanTestCase(CreateTestCase):
    def getType(self):
        return bool


