import unittest
from datetime import datetime, date

from pyautodata import Fixture


class AnonymousDatetimeTestCase(unittest.TestCase):
    def test_create_datetime_returns_not_none(self):
        self.assertIsNotNone(Fixture.create(datetime))

    def test_create_datetime_returns_not_type(self):
        self.assertNotIsInstance(Fixture.create(datetime), type)

    def test_create_datetime_returns_datetime(self):
        self.assertIsInstance(Fixture.create(datetime), datetime)


class AnonymousDateTestCase(unittest.TestCase):
    def test_create_date_returns_not_none(self):
        self.assertIsNotNone(Fixture.create(date))

    def test_create_date_returns_not_type(self):
        self.assertNotIsInstance(Fixture.create(date), type)

    def test_create_date_returns_date(self):
        self.assertIsInstance(Fixture.create(date), date)


