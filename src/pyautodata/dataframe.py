import pandas as pd

from pyautodata.generator import TypeDataGenerator


class PandasDataFrameGenerator:
    """
    Create a Pandas DataFrame containing anonymous data with the specified number of rows (default 3)

    :type rows: int
    :type t: object
    """

    def __init__(self, t, rows: int = 3):
        self.__data = []
        for i in range(rows):
            self.__data.append(TypeDataGenerator.create(t).generate())

    def generate(self):
        members = [
            attr for attr in dir(self.__data[0])
            if not callable(getattr(self.__data[0], attr)) and not attr.startswith("__")
        ]
        rows = []
        for d in self.__data:
            row = []
            for member in members:
                attr = getattr(d, member)
                row.append(attr)
            rows.append(row)

        print(members)
        print(rows)
        return pd.DataFrame(rows, columns=members)


class SparkDataFrameGenerator:
    """
    Create a Spark DataFrame containing anonymous data with the specified number of rows (default 3)

    :type rows: int
    :type t: object
    """

    def __init__(self, t, rows: int = 3):
        self.__data = []
        for i in range(rows):
            self.__data.append(TypeDataGenerator.create(t).generate())

    def generate(self):
        # TODO: Build schema and add data
        raise NotImplementedError
