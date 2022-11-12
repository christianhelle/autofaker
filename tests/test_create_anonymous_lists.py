import unittest
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime, date
from typing import List

from autofaker import Autodata


class CreateTestCase(unittest.TestCase):
    @abstractmethod
    def getType(self):
        pass

    def create(self):
        return Autodata.create(self.getType())

    def test_create_returns_not_none(self):
        if self.getType() is None:
            return
        self.assertIsNotNone(self.create())

    def test_create_returns_not_type(self):
        if self.getType() is None:
            return
        self.assertNotIsInstance(self.create(), type)

    def test_create_returns_not_default(self):
        if self.getType() is None or self.getType() is bool:
            return
        collection = self.create()
        self.assertNotEqual(collection, [])

    def test_create_returns_not_empty(self):
        if self.getType() is None or self.getType() is bool:
            return
        collection = self.create()
        self.assertNotEqual(len(collection), 0)


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


class AnonymousNestedListTestCase(CreateTestCase):
    def getType(self):
        return List[List[int]]


class AnonymousDoubleNestedListTestCase(CreateTestCase):
    def getType(self):
        return List[List[List[int]]]


@dataclass
class DataClass:
    name: str
    age: int


class AnonymousDataClassListTestCase(CreateTestCase):
    def getType(self):
        return List[DataClass]

    def test_name_not_none(self):
        for data in self.create():
            self.assertIsNotNone(data.name)

    def test_age_not_default(self):
        for data in self.create():
            self.assertNotEqual(data.age, int())


@dataclass
class NestedDataClass:
    a: DataClass
    b: DataClass
    c: DataClass


class AnonymousNestedDataClassListTestCase(CreateTestCase):
    def getType(self):
        return List[NestedDataClass]

    def test_name_not_none(self):
        for data in self.create():
            self.assertIsNotNone(data.a.name)
            self.assertIsNotNone(data.b.name)
            self.assertIsNotNone(data.c.name)

    def test_age_not_default(self):
        for data in self.create():
            self.assertNotEqual(data.a.age, int())
            self.assertIsNotNone(data.b.age, int())
            self.assertIsNotNone(data.c.age, int())


class ConstructorWithNestedDataClassList:
    def __init__(self, inner: List[NestedDataClass]):
        self.inner = inner


class AnonymousDoubleNestedDataClassListTestCase(CreateTestCase):
    def getType(self):
        return List[ConstructorWithNestedDataClassList]

    def test_inner_not_none(self):
        for data in self.create():
            self.assertIsNotNone(data.inner)

    def test_inner_not_empty(self):
        for data in self.create():
            self.assertNotEqual(len(data.inner), 0)
