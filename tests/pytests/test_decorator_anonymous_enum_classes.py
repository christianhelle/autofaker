from enum import Enum

from autofaker import autodata


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


@autodata(Weekday)
def test_create_enum_class_returns_not_none(sut):
    assert sut is not None


@autodata(Weekday)
def test_create_enum_class_returns_instance(sut):
    assert isinstance(sut, Weekday)
