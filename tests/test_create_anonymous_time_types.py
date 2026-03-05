import unittest
from datetime import time, timedelta

from autofaker import Autodata


class AnonymousTimeTestCase(unittest.TestCase):
    def test_create_time_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(time))

    def test_create_time_returns_not_type(self):
        self.assertNotIsInstance(Autodata.create(time), type)

    def test_create_time_returns_time(self):
        self.assertIsInstance(Autodata.create(time), time)

    def test_create_time_returns_unique_values(self):
        result1 = Autodata.create(time)
        result2 = Autodata.create(time)
        self.assertNotEqual(result1, result2)


class AnonymousTimedeltaTestCase(unittest.TestCase):
    def test_create_timedelta_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(timedelta))

    def test_create_timedelta_returns_not_type(self):
        self.assertNotIsInstance(Autodata.create(timedelta), type)

    def test_create_timedelta_returns_timedelta(self):
        self.assertIsInstance(Autodata.create(timedelta), timedelta)

    def test_create_timedelta_returns_non_negative(self):
        result = Autodata.create(timedelta)
        self.assertGreaterEqual(result.total_seconds(), 0)
