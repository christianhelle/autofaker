import unittest
from datetime import datetime, date

from autofaker import Autodata


class AnonymousPrimitivesViaDecoratorTests(unittest.TestCase):

    @Autodata.create_arguments(str)
    def test_create_str_using_decorator(self, text):
        self.assertIsNotNone(text)

    @Autodata.create_arguments(int)
    def test_create_int_using_decorator(self, number):
        self.assertIsNotNone(number)

    @Autodata.create_arguments(float)
    def test_create_float_using_decorator(self, number):
        self.assertIsNotNone(number)

    @Autodata.create_arguments(bool)
    def test_create_boolean_using_decorator(self, boolean):
        self.assertIsNotNone(boolean)

    @Autodata.create_arguments(datetime)
    def test_create_datetime_using_decorator(self, dt):
        self.assertIsNotNone(dt)

    @Autodata.create_arguments(date)
    def test_create_date_using_decorator(self, d):
        self.assertIsNotNone(d)


class AnonymousPrimitivesViaDecoratorWithFakesTests(unittest.TestCase):

    @Autodata.create_arguments(str, use_fake_data=True)
    def test_create_str_using_decorator(self, text):
        self.assertIsNotNone(text)

    @Autodata.create_arguments(int, use_fake_data=True)
    def test_create_int_using_decorator(self, number):
        self.assertIsNotNone(number)

    @Autodata.create_arguments(float, use_fake_data=True)
    def test_create_float_using_decorator(self, number):
        self.assertIsNotNone(number)

    @Autodata.create_arguments(bool, use_fake_data=True)
    def test_create_boolean_using_decorator(self, boolean):
        self.assertIsNotNone(boolean)

    @Autodata.create_arguments(datetime, use_fake_data=True)
    def test_create_datetime_using_decorator(self, dt):
        self.assertIsNotNone(dt)

    @Autodata.create_arguments(date, use_fake_data=True)
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


class MultipleArgumentsViaDecoratorTests(unittest.TestCase):

    @Autodata.create_anonymous_arguments
    def test_create_anonymous_arguments_using_decorator(self, text: str, number: int, decimal: float):
        print(text)
        print(number)
        print(decimal)
        self.assertIsNotNone(text)
        self.assertNotEqual(number, 0)
        self.assertNotEqual(decimal, float())

    @Autodata.create_fake_arguments
    def test_create_fake_arguments_using_decorator(self, text: str, number: int, decimal: float):
        print(text)
        print(number)
        print(decimal)
        self.assertIsNotNone(text)
        self.assertNotEqual(number, 0)
        self.assertNotEqual(decimal, float())

    @Autodata.create_arguments()
    def test_create_arguments_using_decorator(self, text: str, number: int, decimal: float):
        print(text)
        print(number)
        print(decimal)
        self.assertIsNotNone(text)
        self.assertNotEqual(number, 0)
        self.assertNotEqual(decimal, float())

    @Autodata.create_arguments(use_fake_data=True)
    def test_create_arguments_using_decorator_with_fakes(self, text: str, number: int, decimal: float):
        print(text)
        print(number)
        print(decimal)
        self.assertIsNotNone(text)
        self.assertNotEqual(number, 0)
        self.assertNotEqual(decimal, float())
