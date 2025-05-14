import unittest
from dataclasses import dataclass
from typing import Literal

from autofaker import Autodata


@dataclass
class DataClassWithLiteral:
    id: int
    status: Literal["pending", "approved", "rejected"]


class AnonymousLiteralTypeTestCase(unittest.TestCase):
    def test_create_literal_returns_not_none(self):
        data = Autodata.create(DataClassWithLiteral)
        self.assertIsNotNone(data)

    def test_create_literal_returns_valid_value(self):
        data = Autodata.create(DataClassWithLiteral)
        self.assertIn(data.status, ["pending", "approved", "rejected"])

    def test_create_literal_returns_fake_value(self):
        data = Autodata.create(DataClassWithLiteral, use_fake_data=True)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
