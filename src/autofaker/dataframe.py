import pandas as pd

from autofaker.attributes import Attributes
from autofaker.generator import TypeDataGenerator


class PandasDataFrameGenerator:
    """
    Create a Pandas DataFrame containing anonymous data with the specified number of rows (default 3)
    """

    def __init__(self, t, rows: int = 3, use_fake_data: bool = False):
        """
        Create a Pandas DataFrame containing anonymous data with the specified number of rows (default 3)

        :type rows: int
        :type t: object
        :type use_fake_data: bool
        """
        self.__data = []
        for _ in range(rows):
            self.__data.append(TypeDataGenerator.create(t, use_fake_data=use_fake_data).generate())

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
    """

    def __init__(self, t, rows: int = 3, use_fake_data: bool = False):
        """
        Create a Pandas DataFrame containing anonymous data with the specified number of rows (default 3)

        :type rows: int
        :type t: object
        :type use_fake_data: bool
        """
        self.use_fake_data = use_fake_data
        self.t = t
        self.rows = rows

    def generate(self):
        from pyspark.sql import SparkSession
        pdf = PandasDataFrameGenerator(self.t, self.rows, use_fake_data=self.use_fake_data).generate()
        spark = SparkSession.builder.getOrCreate()
        return spark.createDataFrame(pdf)
