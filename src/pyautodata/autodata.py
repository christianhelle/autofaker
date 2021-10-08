import typing
from typing import List
from pyspark.sql import DataFrame

from pyautodata.generator import TypeDataGenerator


class Autodata:
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
    def create_dataframe(t, rows: int = 3) -> DataFrame:
        """
        Create a Spark DataFrame containing anonymous data with the specified number of rows (default 3)

        :type rows: int
        :type t: object
        """
        raise NotImplementedError
