"""
Provides classes for anonymous object creation to help minimize the setup/arrange phase when writing unit tests
"""

import typing
from typing import List

from autofaker.dataframe import PandasDataFrameGenerator
from autofaker.generator import TypeDataGenerator


class Autodata:
    """
    Provides anonymous object creation functions to help minimize the setup/arrange phase when writing unit tests
    """

    @staticmethod
    def create(t, use_fake_data: bool = False):
        """
        Creates an anonymous variable of the requested type

        :param type t: type - The type to generate data for
        :param use_fake_data: bool - Set this to True to use Faker to generate data, otherwise False to generate anonymous data
        """
        return TypeDataGenerator.create(t, use_fake_data=use_fake_data).generate()

    @staticmethod
    def create_many(t, size: int = 3, use_fake_data: bool = False) -> List[typing.Any]:
        """
        Creates a list of anonymous variables of the requested type using the specified length (default 3)

        :param type t: type - The type to generate data for
        :type size: int - The number of items to generate (default 3)
        :param use_fake_data: bool - Set this to True to use Faker to generate data, otherwise False to generate anonymous data
        """
        items = []
        for _ in range(size):
            items.append(Autodata.create(t, use_fake_data=use_fake_data))
        return items

    @staticmethod
    def create_pandas_dataframe(t, rows: int = 3, use_fake_data: bool = False):
        """
        Create a Pandas DataFrame containing anonymous data with the specified number of rows (default 3)

        :param type t: object - The class that represents the DataFrame. This can be a plain old class or a @dataclass
        :param type rows: int - The number of rows to generate for the DataFrame (default 3)
        :param use_fake_data: bool - Set this to True to use Faker to generate data, otherwise False to generate anonymous data
        """
        return PandasDataFrameGenerator(t, rows, use_fake_data=use_fake_data).generate()
