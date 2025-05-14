import unittest
from dataclasses import dataclass
from typing import Literal

from autofaker import Autodata

string_literal = Literal["pending", "approved", "rejected"]
number_literal = Literal[1, 2, 3]


class AnonymousStringLiteralTypeTestCase(unittest.TestCase):
    def test_create_literal_returns_not_none(self):
        data = Autodata.create(string_literal)
        self.assertIsNotNone(data)

    def test_create_literal_returns_valid_value(self):
        data = Autodata.create(string_literal)
        self.assertIn(data, ["pending", "approved", "rejected"])


class AnonymousNumberLiteralTypeTestCase(unittest.TestCase):
    def test_create_literal_returns_not_none(self):
        data = Autodata.create(number_literal)
        self.assertIsNotNone(data)

    def test_create_literal_returns_valid_value(self):
        data = Autodata.create(number_literal)
        self.assertIn(data, [1, 2, 3])


@dataclass
class DataClassWithLiteral:
    id: int
    status: string_literal
    number: number_literal


class AnonymousDataClassWithLiteralTypeTestCase(unittest.TestCase):
    def test_create_literal_returns_not_none(self):
        data = Autodata.create(DataClassWithLiteral)
        self.assertIsNotNone(data)

    def test_create_literal_returns_valid_value(self):
        data = Autodata.create(DataClassWithLiteral)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
        self.assertIn(data.number, [1, 2, 3])

    def test_create_literal_returns_fake_value(self):
        data = Autodata.create(DataClassWithLiteral, use_fake_data=True)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
        self.assertIn(data.number, [1, 2, 3])
