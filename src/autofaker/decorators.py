import inspect
import unittest
from typing import List

from autofaker import Autodata, PandasDataFrameGenerator, SparkDataFrameGenerator


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


def autopandas(t, rows: int = 3, use_fake_data: bool = False):
    """
    Create a Pandas DataFrame containing anonymous data with the specified number of rows (default 3)

    :param use_fake_data:
    :type rows: int
    :type t: object
    """
    def decorator(function):
        def wrapper(*args):
            pdf = PandasDataFrameGenerator(t, rows, use_fake_data=use_fake_data).generate()
            return function(__get_test_class(*args), pdf)
        return wrapper
    return decorator


def fakepandas(t, rows: int = 3):
    """
    Create a Pandas DataFrame containing fake data with the specified number of rows (default 3)

    :type rows: int
    :type t: object
    """
    return autopandas(t, rows, use_fake_data=True)


def autospark(t, rows: int = 3, use_fake_data: bool = False):
    """
    Create a Spark DataFrame containing anonymous data with the specified number of rows (default 3)

    :param use_fake_data:
    :type rows: int
    :type t: object
    """
    def decorator(function):
        def wrapper(*args):
            df = SparkDataFrameGenerator(t, rows, use_fake_data=use_fake_data).generate()
            return function(__get_test_class(*args), df)
        return wrapper
    return decorator


def fakespark(t, rows: int = 3):
    """
    Create a Spark DataFrame containing fake data with the specified number of rows (default 3)

    :type rows: int
    :type t: object
    """
    return autospark(t, rows, use_fake_data=True)


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
