import inspect
import unittest
from typing import List

from autofaker import Autodata


def autodata(*types: object, use_fake_data: bool = False):
    """
    Creates anonymous variable of the requested types and pass them as arguments to a unit test function

    Example:

    import unittest

    from autofaker import autodata

    class SampleTest(unittest.TestCase):
        @autodata(str, int, float, bool)

        def test_create_str_argument_using_decorator(self, text, number, decimal, boolean):
            self.assertIsNotNone(text)


    :param use_fake_data:
    :type types: tuple
    """
    def decorator(function):
        def wrapper(*args):
            return function(__get_test_class(*args),
                            *tuple(__create_function_args(function, *tuple(types), use_fake_data=use_fake_data)))
        return wrapper
    return decorator


def fakedata(*types: object):
    """
    Creates fake values for the variables of the requested types and pass them as arguments to a unit test function

    Example:

    import unittest

    from autofaker import fakedata

    class SampleTest(unittest.TestCase):
        @fakedata

        def test_create_fake_arguments(self, text: str, number: int, decimal: float, boolean: bool):
            self.assertIsNotNone(text)
    """
    def decorator(function):
        def wrapper(*args):
            return function(__get_test_class(*args),
                            *tuple(__create_function_args(function, *tuple(types), use_fake_data=True)))
        return wrapper
    return decorator


def __get_test_class(*args):
    if len(args) == 0:
        raise NotImplementedError("This way of creating anonymous objects are only supported from unit tests")
    test_class = args[0]
    if issubclass(test_class.__class__, unittest.TestCase) is False:
        raise NotImplementedError("This way of creating anonymous objects are only supported from unit tests")
    return test_class


def __create_function_args(function, *types, use_fake_data: bool = False) -> List:
    values = []
    argtpes = inspect.getfullargspec(function)
    args = argtpes.annotations.values() if types is None or len(types) == 0 else types
    for t in args:
        value = Autodata.create(t, use_fake_data)
        values.append(value)
    if len(argtpes.args) - 1 != len(values):
        raise ValueError("Missing argument annotations. Please declare the type of every argument")
    return values
