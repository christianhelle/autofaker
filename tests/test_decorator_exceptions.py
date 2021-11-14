import sys
import unittest

from autofaker import autodata, fakedata, autopandas, autospark, fakepandas, fakespark


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

    @unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
    def test_autospark_throws_error_when_decorating_non_testmethod(self):
        class SimpleClass:
            id = -1
            name = 'name'
            text = 'test'
        with self.assertRaises(NotImplementedError):
            class X:
                @autospark(SimpleClass)
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

    @unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
    def test_fakespark_throws_error_when_decorating_non_testmethod(self):
        class SimpleClass:
            id = -1
            name = 'name'
            text = 'test'
        with self.assertRaises(NotImplementedError):
            class X:
                @fakespark(SimpleClass)
                def not_test_method(self, df):
                    pass
            X().not_test_method()
