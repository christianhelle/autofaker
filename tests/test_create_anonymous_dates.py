import unittest
from datetime import datetime, date

from autofaker import Autodata


class AnonymousDatetimeTestCase(unittest.TestCase):
    def test_create_datetime_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(datetime))

    def test_create_datetime_returns_not_type(self):
        self.assertNotIsInstance(Autodata.create(datetime), type)

    def test_create_datetime_returns_datetime(self):
        self.assertIsInstance(Autodata.create(datetime), datetime)


class AnonymousDateTestCase(unittest.TestCase):
    def test_create_date_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(date))

    def test_create_date_returns_not_type(self):
        self.assertNotIsInstance(Autodata.create(date), type)

    def test_create_date_returns_date(self):
        self.assertIsInstance(Autodata.create(date), date)


