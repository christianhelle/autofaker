import decimal
import pathlib
import unittest
import uuid
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


class AnonymousTupleTestCase(CreateTestCase):
    def getType(self) -> Type[tuple]:
        return tuple

    def test_create_tuple_returns_tuple(self):
        self.assertIsInstance(Autodata.create(tuple), tuple)

    def test_create_tuple_returns_non_empty(self):
        result = Autodata.create(tuple)
        self.assertGreater(len(result), 0)


class AnonymousSetTestCase(CreateTestCase):
    def getType(self) -> Type[set]:
        return set

    def test_create_set_returns_set(self):
        self.assertIsInstance(Autodata.create(set), set)

    def test_create_set_returns_non_empty(self):
        result = Autodata.create(set)
        self.assertGreater(len(result), 0)


class AnonymousFrozenSetTestCase(CreateTestCase):
    def getType(self) -> Type[frozenset]:
        return frozenset

    def test_create_frozenset_returns_frozenset(self):
        self.assertIsInstance(Autodata.create(frozenset), frozenset)

    def test_create_frozenset_returns_non_empty(self):
        result = Autodata.create(frozenset)
        self.assertGreater(len(result), 0)


class AnonymousDictTestCase(CreateTestCase):
    def getType(self) -> Type[dict]:
        return dict

    def test_create_dict_returns_dict(self):
        self.assertIsInstance(Autodata.create(dict), dict)

    def test_create_dict_returns_non_empty(self):
        result = Autodata.create(dict)
        self.assertGreater(len(result), 0)


class AnonymousDecimalTestCase(CreateTestCase):
    def getType(self) -> Type[decimal.Decimal]:
        return decimal.Decimal

    def test_create_decimal_returns_decimal(self):
        self.assertIsInstance(Autodata.create(decimal.Decimal), decimal.Decimal)

    def test_create_decimal_returns_positive_value(self):
        result = Autodata.create(decimal.Decimal)
        self.assertGreaterEqual(result, 0)


class AnonymousUUIDTestCase(CreateTestCase):
    def getType(self) -> Type[uuid.UUID]:
        return uuid.UUID

    def test_create_uuid_returns_uuid(self):
        self.assertIsInstance(Autodata.create(uuid.UUID), uuid.UUID)

    def test_create_uuid_returns_unique_values(self):
        result1 = Autodata.create(uuid.UUID)
        result2 = Autodata.create(uuid.UUID)
        self.assertNotEqual(result1, result2)


class AnonymousPathTestCase(CreateTestCase):
    def getType(self) -> Type[pathlib.Path]:
        return pathlib.Path

    def test_create_path_returns_path(self):
        self.assertIsInstance(Autodata.create(pathlib.Path), pathlib.Path)

    def test_create_path_returns_non_empty_parts(self):
        result = Autodata.create(pathlib.Path)
        self.assertGreater(len(result.parts), 0)
