import pandas as pd

from pyautodata.attributes import Attributes
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
        members = Attributes(self.__data[0]).get_members()
        rows = []
        for d in self.__data:
            row = []
            for member in members:
                row.append(Attributes(d).get_attribute(member))
            rows.append(row)
        return pd.DataFrame(rows, columns=members)


class SparkDataFrameGenerator:
    """
    Create a Spark DataFrame containing anonymous data with the specified number of rows (default 3)

    :type rows: int
    :type t: object
    """

    def __init__(self, t, rows: int = 3):
        self.t = t
        self.rows = rows

    def generate(self):
        from pyspark.sql import SparkSession
        pdf = PandasDataFrameGenerator(self.t, self.rows).generate()
        spark = SparkSession.builder.getOrCreate()
        return spark.createDataFrame(pdf)
