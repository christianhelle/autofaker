import typing
from typing import List
from pyspark.sql import DataFrame

from pyautodata.generator import TypeDataGenerator


class Fixture:
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
            items.append(Fixture.create(t))
        return items
