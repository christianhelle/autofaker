"""
Provides anonymous object creation functions to help minimize the setup/arrange phase when writing unit tests
"""

import inspect
import unittest
from typing import List

from autofaker import Autodata, PandasDataFrameGenerator


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


    :param use_fake_data: bool - Set this to True to use Faker to generate data, otherwise False to generate anonymous data
    :param type types: tuple - The types to generate data. This is optional and will use the arguments from the function being decorated if not specified
    """

    def decorator(function):
        def wrapper(*args):
            if __get_class_that_defined_method(function) is None:
                return function(*tuple(__create_function_args(function, *tuple(types), use_fake_data=use_fake_data)))
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
        @fakedata()

        def test_create_fake_arguments(self, text: str, number: int, decimal: float, boolean: bool):
            self.assertIsNotNone(text)


    :param types: object - The types to generate data. This is optional and will use the arguments from the function being decorated if not specified
    """

    def decorator(function):
        def wrapper(*args):
            if __get_class_that_defined_method(function) is None:
                return function(*tuple(__create_function_args(function, *tuple(types), use_fake_data=True)))
            return function(__get_test_class(*args),
                            *tuple(__create_function_args(function, *tuple(types), use_fake_data=True)))

        return wrapper

    return decorator


def autopandas(t: object, rows: int = 3, use_fake_data: bool = False):
    """
    Create a Pandas DataFrame containing anonymous data with the specified number of rows (default 3)

    :param type t: object - The class that represents the DataFrame. This can be a plain old class or a @dataclass
    :param type rows: int - The number of rows to generate for the DataFrame (default 3)
    :param use_fake_data: bool - Set this to True to use Faker to generate data, otherwise False to generate anonymous data
    """

    def decorator(function):
        def wrapper(*args):
            pdf = PandasDataFrameGenerator(t, rows, use_fake_data=use_fake_data).generate()
            if __get_class_that_defined_method(function) is None:
                return function(pdf)
            return function(__get_test_class(*args), pdf)

        return wrapper

    return decorator


def fakepandas(t, rows: int = 3):
    """
    Create a Pandas DataFrame containing fake data with the specified number of rows (default 3)

    :param type t: object - The class that represents the DataFrame. This can be a plain old class or a @dataclass
    :param type rows: int - The number of rows to generate for the DataFrame (default 3)
    """
    return autopandas(t, rows, use_fake_data=True)


def __get_test_class(*args):
    test_class = args[0]
    if issubclass(test_class.__class__, unittest.TestCase) is False:
        raise NotImplementedError("This way of creating anonymous objects are only supported from unit tests")
    return test_class


def __get_class_that_defined_method(meth):
    if inspect.isfunction(meth):
        cls = getattr(inspect.getmodule(meth),
                      meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0],
                      None)
        if isinstance(cls, type):
            return cls
    return getattr(meth, '__objclass__', None)  # handle special descriptor objects


def __create_function_args(function, *types, use_fake_data: bool = False) -> List:
    values = []
    argtpes = inspect.getfullargspec(function)
    args = argtpes.annotations.values() if types is None or len(types) == 0 else types
    for t in args:
        value = Autodata.create(t, use_fake_data)
        values.append(value)
    pos = 1
    if __get_class_that_defined_method(function) is None:
        pos = 0
    if len(argtpes.args) - pos != len(values):
        raise ValueError("Missing argument annotations. Please declare the type of every argument")
    return values
