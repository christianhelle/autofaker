import unittest

from autofaker import Autodata


class AnonymousPrimitivesViaDecoratorThrowsExceptionsTests(unittest.TestCase):

    def test_create_arguments_throws_error_when_decorating_non_testmethod(self):
        with self.assertRaises(NotImplementedError):
            class X:
                @Autodata.create_arguments(str, str, str)
                def not_test_method(self):
                    pass
            X().not_test_method()

    def test_create_arguments_throws_error_when_used_without_arguments(self):
        with self.assertRaises(NotImplementedError):
            class X:
                @Autodata.create_arguments()
                def not_test_method(self):
                    pass
            X().not_test_method()

    def test_create_arguments_throws_error_when_used_without_arguments_annotation(self):
        with self.assertRaises(ValueError):
            class X(unittest.TestCase):
                @Autodata.create_arguments()
                def not_test_method(self, text, number, decimal):
                    pass
            X().not_test_method()
