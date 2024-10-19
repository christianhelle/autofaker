import unittest
from abc import abstractmethod
from typing import Type

from autofaker import Autodata


class CreateTestCase(unittest.TestCase):
    @abstractmethod
    def getType(self) -> Type:
        pass

    def test_create_returns_not_none(self):
        if self.getType() is not None:
            self.assertIsNotNone(Autodata.create(self.getType()))

    def test_create_returns_not_type(self):
        if self.getType() is not None:
            self.assertNotIsInstance(Autodata.create(self.getType()), type)

    def test_create_returns_not_default(self):
        if (self.getType() is not None
            and not bool
            and not range):
            self.assertNotEqual(Autodata.create(self.getType()), self.getType()())


class AnonymousIntegerTestCase(CreateTestCase):
    def getType(self) -> Type[int]:
        return int


class AnonymousStringTestCase(CreateTestCase):
    def getType(self) -> Type[str]:
        return str


class AnonymousFloatTestCase(CreateTestCase):
    def getType(self) -> Type[float]:
        return float


class AnonymousBooleanTestCase(CreateTestCase):
    def getType(self) -> Type[bool]:
        return bool


class AnonymousComplexTestCase(CreateTestCase):
    def getType(self) -> Type[complex]:
        return complex


class AnonymousRangeTestCase(CreateTestCase):
    def getType(self) -> Type[range]:
        return range


class AnonymousBytesTestCase(CreateTestCase):
    def getType(self) -> Type[bytes]:
        return bytes


class AnonymousByteArrayTestCase(CreateTestCase):
    def getType(self) -> Type[bytearray]:
        return bytearray


class AnonymousMemoryViewTestCase(CreateTestCase):
    def getType(self) -> Type[memoryview]:
        return memoryview


class AnonymousSetTestCase(CreateTestCase):
    def getType(self) -> Type[set]:
        return set


class AnonymousFrozensetTestCase(CreateTestCase):
    def getType(self) -> Type[frozenset]:
        return frozenset
