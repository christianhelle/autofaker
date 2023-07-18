import unittest
from enum import Enum

from autofaker import Autodata


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class AnonymousWeekdayTestCase(unittest.TestCase):
    def test_create_enum_class_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(Weekday))

    def test_create_enum_class_returns_instance(self):
        self.assertIsInstance(Autodata.create(Weekday), Weekday)


class BasicEnum(Enum):
    """empty"""


class InheritedEnum(BasicEnum):
    VALUE_1 = 1
    VALUE_2 = 2


class AnonymousEnumInheritanceTestCase(unittest.TestCase):
    def test_create_enum_class_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(InheritedEnum))

    def test_create_enum_class_returns_instance(self):
        self.assertIsInstance(Autodata.create(InheritedEnum), BasicEnum)
