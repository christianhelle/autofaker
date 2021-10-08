"""
Provides classes for anonymous object creation to help minimize the setup/arrange phase when writing unit tests
"""

import typing
from typing import List

from pyspark.sql import DataFrame, SparkSession

from pyautodata.dataframe import PandasDataFrameGenerator, SparkDataFrameGenerator
from pyautodata.generator import TypeDataGenerator


class Autodata:
    """
    Provides anonymous object creation functions to help minimize the setup/arrange phase when writing unit tests
    """

    @staticmethod
    def create(t):
        """
        Creates an anonymous variable of the requested type

        :type t: object
        """
        return TypeDataGenerator.create(t).generate()

    @staticmethod
    def create_many(t, size: int = 3) -> List[typing.Any]:
        """
        Creates a list of anonymous variables of the requested type using the specified length (default 3)

        :type size: int
        :type t: object
        """
        items = []
        for i in range(size):
            items.append(Autodata.create(t))
        return items

    @staticmethod
    def create_pandas_dataframe(t, rows: int = 3):
        """
        Create a Pandas DataFrame containing anonymous data with the specified number of rows (default 3)

        :type rows: int
        :type t: object
        """
        return PandasDataFrameGenerator(t, rows).generate()

    @staticmethod
    def create_spark_dataframe(t, rows: int = 3) -> DataFrame:
        """
        Create a Spark DataFrame containing anonymous data with the specified number of rows (default 3)

        :type rows: int
        :type t: object
        """
        return SparkDataFrameGenerator(t, rows).generate()
