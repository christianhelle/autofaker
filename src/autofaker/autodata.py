"""
Provides classes for anonymous object creation to help minimize the setup/arrange phase when writing unit tests
"""

import typing
import unittest
from typing import List

from pyspark.sql import DataFrame

from autofaker.dataframe import PandasDataFrameGenerator, SparkDataFrameGenerator
from autofaker.generator import TypeDataGenerator


class Autodata:
    """
    Provides anonymous object creation functions to help minimize the setup/arrange phase when writing unit tests
    """

    @staticmethod
    def create(t, use_fake_data: bool = False):
        """
        Creates an anonymous variable of the requested type

        :param use_fake_data:
        :type t: object
        """
        return TypeDataGenerator.create(t, use_fake_data=use_fake_data).generate()

    @staticmethod
    def create_many(t, size: int = 3, use_fake_data: bool = False) -> List[typing.Any]:
        """
        Creates a list of anonymous variables of the requested type using the specified length (default 3)

        :param use_fake_data:
        :type size: int
        :type t: object
        """
        items = []
        for _ in range(size):
            items.append(Autodata.create(t, use_fake_data=use_fake_data))
        return items

    @staticmethod
    def create_pandas_dataframe(t, rows: int = 3, use_fake_data: bool = False):
        """
        Create a Pandas DataFrame containing anonymous data with the specified number of rows (default 3)

        :param use_fake_data:
        :type rows: int
        :type t: object
        """
        return PandasDataFrameGenerator(t, rows, use_fake_data=use_fake_data).generate()

    @staticmethod
    def create_spark_dataframe(t, rows: int = 3, use_fake_data: bool = False) -> DataFrame:
        """
        Create a Spark DataFrame containing anonymous data with the specified number of rows (default 3)

        :param use_fake_data:
        :type rows: int
        :type t: object
        """
        return SparkDataFrameGenerator(t, rows, use_fake_data=use_fake_data).generate()

    @staticmethod
    def create_arguments(*types: object, use_fake_data: bool = False):
        """
        Creates anonymous variable of the requested types and pass them as arguments to a unit test function

        Example:

        import unittest

        from autofaker import Autodata

        class SampleTest(unittest.TestCase):
            @Autodata.create_arguments(str, int, float, bool)

            def test_create_str_argument_using_decorator(self, text, number, decimal, boolean):
                self.assertIsNotNone(text)


        :param use_fake_data:
        :type types: tuple
        """
        def decorator(function):
            def wrapper(*args):
                if len(args) == 0:
                    raise NotImplementedError("This way of creating anonymous objects are only supported from unit tests")
                test_class = args[0]
                if issubclass(test_class.__class__, unittest.TestCase) is False:
                    raise NotImplementedError("This way of creating anonymous objects are only supported from unit tests")
                values = []
                for t in types:
                    value = Autodata.create(t, use_fake_data)
                    values.append(value)
                return function(test_class, *tuple(values))
            return wrapper
        return decorator
