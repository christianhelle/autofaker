import unittest
from datetime import datetime, date

from autofaker import Autodata


class AnonymousPrimitivesViaDecoratorTests(unittest.TestCase):

    @Autodata.create_argument(str)
    def test_create_str_using_decorator(self, text):
        self.assertIsNotNone(text)

    @Autodata.create_argument(int)
    def test_create_int_using_decorator(self, number):
        self.assertIsNotNone(number)

    @Autodata.create_argument(float)
    def test_create_float_using_decorator(self, number):
        self.assertIsNotNone(number)

    @Autodata.create_argument(bool)
    def test_create_boolean_using_decorator(self, boolean):
        self.assertIsNotNone(boolean)

    @Autodata.create_argument(datetime)
    def test_create_datetime_using_decorator(self, dt):
        self.assertIsNotNone(dt)

    @Autodata.create_argument(date)
    def test_create_date_using_decorator(self, d):
        self.assertIsNotNone(d)


class AnonymousPrimitivesViaDecoratorWithFakesTests(unittest.TestCase):

    @Autodata.create_argument(str, use_fake_data=True)
    def test_create_str_using_decorator(self, text):
        self.assertIsNotNone(text)

    @Autodata.create_argument(int, use_fake_data=True)
    def test_create_int_using_decorator(self, number):
        self.assertIsNotNone(number)

    @Autodata.create_argument(float, use_fake_data=True)
    def test_create_float_using_decorator(self, number):
        self.assertIsNotNone(number)

    @Autodata.create_argument(bool, use_fake_data=True)
    def test_create_boolean_using_decorator(self, boolean):
        self.assertIsNotNone(boolean)

    @Autodata.create_argument(datetime, use_fake_data=True)
    def test_create_datetime_using_decorator(self, dt):
        self.assertIsNotNone(dt)

    @Autodata.create_argument(date, use_fake_data=True)
    def test_create_date_using_decorator(self, d):
        self.assertIsNotNone(d)


class MultipleAnonymousPrimitivesViaDecoratorTests(unittest.TestCase):

    @Autodata.create_arguments(str, int, float)
    def test_create_primitives_using_decorator(self, text, number, decimal):
        self.assertIsNotNone(text)
        self.assertNotEqual(number, 0)
        self.assertNotEqual(decimal, float())

    @Autodata.create_arguments(str, int, float, use_fake_data=True)
    def test_create_primitives_using_decorator_with_fakes(self, text, number, decimal):
        self.assertIsNotNone(text)
        self.assertNotEqual(number, 0)
        self.assertNotEqual(decimal, float())
