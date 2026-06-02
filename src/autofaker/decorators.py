"""
Provides anonymous object creation functions to help minimize
the setup/arrange phase when writing unit tests
"""

import inspect
import unittest
from typing import List

from autofaker import Autodata, PandasDataFrameGenerator


def autodata(*types: object, use_fake_data: bool = False):
    """
    Creates anonymous variable of the requested types
    and pass them as arguments to a unit test function

    Example:

    import unittest

    from autofaker import autodata

    class SampleTest(unittest.TestCase):
        @autodata(str, int, float, bool)

        def test_create_str_argument_using_decorator(self, text, number, decimal, boolean):
            self.assertIsNotNone(text)


    :param use_fake_data: bool
        Set this to True to use Faker to generate data,
        otherwise False to generate anonymous data

    :param type types: tuple
        The types to generate data.
        This is optional and will use the arguments
        from the function being decorated if not specified
    """
    if _is_bare_decoration(types):
        return _make_arg_decorator((), use_fake_data=use_fake_data)(types[0])
    return _make_arg_decorator(types, use_fake_data=use_fake_data)


def fakedata(*types: object):
    """
    Creates fake values for the variables of the requested types
    and pass them as arguments to a unit test function

    Example:

    import unittest

    from autofaker import fakedata

    class SampleTest(unittest.TestCase):
        @fakedata()

        def test_create_fake_arguments(self, text: str, number: int, decimal: float, boolean: bool):
            self.assertIsNotNone(text)


    :param types: object
        The types to generate data.
        This is optional and will use the arguments from the function
        being decorated if not specified
    """
    if _is_bare_decoration(types):
        return _make_arg_decorator((), use_fake_data=True)(types[0])
    return _make_arg_decorator(types, use_fake_data=True)


def autopandas(t: object, rows: int = 3, use_fake_data: bool = False):
    """
    Create a Pandas DataFrame containing anonymous data
    with the specified number of rows (default 3)

    :param type t: object
        The class that represents the DataFrame.
        This can be a plain old class or a @dataclass

    :param type rows: int
        The number of rows to generate for the DataFrame (default 3)

    :param use_fake_data: bool
        Set this to True to use Faker to generate data,
        otherwise False to generate anonymous data
    """

    def decorator(function):
        def wrapper(*args):
            pdf = PandasDataFrameGenerator(
                t, rows, use_fake_data=use_fake_data
            ).generate()
            return _invoke(function, args, lambda: [pdf])

        return wrapper

    return decorator


def fakepandas(t, rows: int = 3):
    """
    Create a Pandas DataFrame containing fake data with
    the specified number of rows (default 3)

    :param type t: object
        The class that represents the DataFrame.
        This can be a plain old class or a @dataclass

    :param type rows: int
        The number of rows to generate for the DataFrame (default 3)
    """
    return autopandas(t, rows, use_fake_data=True)


def _is_bare_decoration(types) -> bool:
    """True when a decorator was applied without parentheses (``@autodata``).

    In that case the decorated function itself is passed as the single
    positional argument. Distinguished from a callable type argument by the
    presence of ``__code__`` and not being a class.
    """
    return (
        len(types) == 1
        and callable(types[0])
        and not isinstance(types[0], type)
        and hasattr(types[0], "__code__")
    )


def _make_arg_decorator(types, use_fake_data: bool):
    """Build a decorator that injects generated arguments into a test function.

    When ``types`` is empty the argument types are taken from the decorated
    function's annotations; otherwise the explicit ``types`` are used.
    """

    def decorator(function):
        def wrapper(*args):
            return _invoke(
                function,
                args,
                lambda: __create_function_args(
                    function, *tuple(types), use_fake_data=use_fake_data
                ),
            )

        return wrapper

    return decorator


def _invoke(function, call_args, build_args):
    """Call ``function`` with generated arguments.

    When the decorated function is a ``unittest.TestCase`` method, its instance
    (``self``) is recovered from the wrapper's call arguments and prepended.
    The test-class check runs before ``build_args`` so an invalid target raises
    ``NotImplementedError`` ahead of any argument-shape error. ``build_args`` is
    a thunk to defer that work until the target is known.
    """
    if __get_class_that_defined_method(function) is None:
        function(*build_args())
        return None
    test_class = __get_test_class(*call_args)
    function(test_class, *build_args())
    return None


def __get_test_class(*args):
    test_class = args[0]
    if not issubclass(test_class.__class__, unittest.TestCase):
        raise NotImplementedError(
            "This way of creating anonymous objects are only supported from unit tests"
        )
    return test_class


def __get_class_that_defined_method(meth):
    if inspect.isfunction(meth):
        cls = getattr(
            inspect.getmodule(meth),
            meth.__qualname__.split(".<locals>", 1)[0].rsplit(".", 1)[0],
            None,
        )
        if isinstance(cls, type):
            return cls
    return getattr(meth, "__objclass__", None)  # handle special descriptor objects


def __create_function_args(function, *types, use_fake_data: bool = False) -> List:
    values = []
    argtypes = inspect.getfullargspec(function)
    annotations = {
        k: v for k, v in argtypes.annotations.items() if k != 'return'
    }
    args = annotations.values() if types is None or len(types) == 0 else types
    for t in args:
        value = Autodata.create(t, use_fake_data)
        values.append(value)
    pos = 1
    if __get_class_that_defined_method(function) is None:
        pos = 0
    if len(argtypes.args) - pos != len(values):
        raise ValueError(
            "Missing argument annotations. Please declare the type of every argument"
        )
    return values
