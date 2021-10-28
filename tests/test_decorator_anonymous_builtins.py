import unittest
from datetime import datetime, date

from autofaker import autodata, fakedata


class AnonymousPrimitivesViaDecoratorTests(unittest.TestCase):

    @autodata(str)
    def test_create_str_using_decorator(self, text):
        self.assertIsNotNone(text)

    @autodata(int)
    def test_create_int_using_decorator(self, number):
        self.assertIsNotNone(number)

    @autodata(float)
    def test_create_float_using_decorator(self, number):
        self.assertIsNotNone(number)

    @autodata(bool)
    def test_create_boolean_using_decorator(self, boolean):
        self.assertIsNotNone(boolean)

    @autodata(datetime)
    def test_create_datetime_using_decorator(self, dt):
        self.assertIsNotNone(dt)

    @autodata(date)
    def test_create_date_using_decorator(self, d):
        self.assertIsNotNone(d)


class AnonymousPrimitivesViaDecoratorWithFakesTests(unittest.TestCase):

    @autodata(str, use_fake_data=True)
    def test_create_str_using_decorator(self, text):
        self.assertIsNotNone(text)

    @autodata(int, use_fake_data=True)
    def test_create_int_using_decorator(self, number):
        self.assertIsNotNone(number)

    @autodata(float, use_fake_data=True)
    def test_create_float_using_decorator(self, number):
        self.assertIsNotNone(number)

    @autodata(bool, use_fake_data=True)
    def test_create_boolean_using_decorator(self, boolean):
        self.assertIsNotNone(boolean)

    @autodata(datetime, use_fake_data=True)
    def test_create_datetime_using_decorator(self, dt):
        self.assertIsNotNone(dt)

    @autodata(date, use_fake_data=True)
    def test_create_date_using_decorator(self, d):
        self.assertIsNotNone(d)


class MultipleAnonymousPrimitivesViaDecoratorTests(unittest.TestCase):

    @autodata(str, int, float)
    def test_create_primitives_using_decorator(self, text, number, decimal):
        self.assertIsNotNone(text)
        self.assertNotEqual(number, 0)
        self.assertNotEqual(decimal, float())

    @autodata(str, int, float, use_fake_data=True)
    def test_create_primitives_using_decorator_with_fakes(self, text, number, decimal):
        self.assertIsNotNone(text)
        self.assertNotEqual(number, 0)
        self.assertNotEqual(decimal, float())


class MultipleArgumentsViaDecoratorTests(unittest.TestCase):

    @fakedata
    def test_create_anonymous_arguments_using_decorator(self, text: str, number: int, decimal: float):
        print(text)
        print(number)
        print(decimal)
        self.assertIsNotNone(text)
        self.assertNotEqual(number, 0)
        self.assertNotEqual(decimal, float())

    @fakedata
    def test_create_fake_arguments_using_decorator(self, text: str, number: int, decimal: float):
        print(text)
        print(number)
        print(decimal)
        self.assertIsNotNone(text)
        self.assertNotEqual(number, 0)
        self.assertNotEqual(decimal, float())

    @autodata()
    def test_create_arguments_using_decorator(self, text: str, number: int, decimal: float):
        print(text)
        print(number)
        print(decimal)
        self.assertIsNotNone(text)
        self.assertNotEqual(number, 0)
        self.assertNotEqual(decimal, float())

    @autodata(use_fake_data=True)
    def test_create_arguments_using_decorator_with_fakes(self, text: str, number: int, decimal: float):
        print(text)
        print(number)
        print(decimal)
        self.assertIsNotNone(text)
        self.assertNotEqual(number, 0)
        self.assertNotEqual(decimal, float())
