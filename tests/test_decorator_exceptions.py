import unittest
from dataclasses import dataclass

import pandas

from autofaker import autodata, fakedata, autopandas, fakepandas


@dataclass
class DataClass:
    id: int
    name: str
    text: str


@autodata(str, str, str)
def autodata_test_method(a, b, c):
    pass


@fakedata(str, str, str)
def fakedata_test_method(a, b, c):
    pass


@autopandas(DataClass)
def autopandas_test_method(df: pandas.DataFrame):
    pass


class AnonymousPrimitivesViaDecoratorThrowsExceptionsTests(unittest.TestCase):

    def test_autodata_throws_error_when_decorating_non_testmethod(self):
        with self.assertRaises(NotImplementedError):
            class X:
                @autodata(str, str, str)
                def not_test_method(self):
                    pass

            X().not_test_method()

    def test_autodata_throws_error_when_used_without_arguments(self):
        with self.assertRaises(NotImplementedError):
            class X:
                @autodata()
                def not_test_method(self):
                    pass

            X().not_test_method()

    def test_autodata_throws_error_when_used_without_arguments_annotation(self):
        with self.assertRaises(ValueError):
            class X(unittest.TestCase):
                @autodata()
                def not_test_method(self, text, number, decimal):
                    pass

            X().not_test_method()

    def test_fakedata_throws_error_when_decorating_non_testmethod(self):
        with self.assertRaises(NotImplementedError):
            class X:
                @fakedata(str, str, str)
                def not_test_method(self):
                    pass

            X().not_test_method()

    def test_fakedata_throws_error_when_used_without_arguments(self):
        with self.assertRaises(NotImplementedError):
            class X:
                @fakedata()
                def not_test_method(self):
                    pass

            X().not_test_method()

    def test_fakedata_throws_error_when_used_without_arguments_annotation(self):
        with self.assertRaises(ValueError):
            class X(unittest.TestCase):
                @fakedata()
                def not_test_method(self, text, number, decimal):
                    pass

            X().not_test_method()

    def test_autopandas_throws_error_when_decorating_non_testmethod(self):
        class SimpleClass:
            id = -1
            name = 'name'
            text = 'test'

        with self.assertRaises(NotImplementedError):
            class X:
                @autopandas(SimpleClass)
                def not_test_method(self, df):
                    pass

            X().not_test_method()

    def test_fakepandas_throws_error_when_decorating_non_testmethod(self):
        class SimpleClass:
            id = -1
            name = 'name'
            text = 'test'

        with self.assertRaises(NotImplementedError):
            class X:
                @fakepandas(SimpleClass)
                def not_test_method(self, df):
                    pass

            X().not_test_method()

    def test_autodata_doesnt_throw_error_when_decorating_non_pytest(self):
        autodata_test_method()

    def test_fakedata_doesnt_throw_error_when_decorating_non_pytest(self):
        fakedata_test_method()

    def test_autopandas_doesnt_throw_error_when_decorating_non_pytest(self):
        autopandas_test_method()
