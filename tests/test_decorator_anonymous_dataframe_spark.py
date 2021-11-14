import sys
import unittest
from dataclasses import dataclass

from pyspark.sql import DataFrame

from autofaker import autospark, fakespark


class SimpleClassA:
    id = -1
    name = 'test'
    text = 'test'


class SimpleClassB:
    def __init__(self, id: int, name: str, text: str):
        self.text = text
        self.name = name
        self.id = id


class SimpleClassC:
    def __init__(self, a: SimpleClassA, b: SimpleClassB):
        self.b = b
        self.a = a


@unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
class AnonymousSparkDataFrameViaDecoratorTests(unittest.TestCase):

    @autospark(SimpleClassA)
    def test_create_anonymous_spark_dataframe_returns_not_none(self, df: DataFrame):
        self.assertIsNotNone(df)

    @autospark(SimpleClassA, 10)
    def test_create_anonymous_spark_dataframe_with_rowcount_returns_not_empty(self, df: DataFrame):
        self.assertNotEqual(df.count(), 0)

    @fakespark(SimpleClassA)
    def test_create_fake_spark_dataframe_returns_not_none(self, df: DataFrame):
        self.assertIsNotNone(df)

    @fakespark(SimpleClassA, 10)
    def test_create_fake_spark_dataframe_with_rowcount_returns_not_empty(self, df: DataFrame):
        self.assertNotEqual(df.count(), 0)

    @autospark(SimpleClassA)
    def test_can_create_anonymous_spark_dataframes(self, cls):
        print(cls)
        self.assertIsNotNone(cls)

    @autospark(SimpleClassB)
    def test_can_create_anonymous_spark_dataframes_from_class_with_constructor_arguments(self, cls):
        print(cls)
        self.assertIsNotNone(cls)

    @autospark(SimpleClassC)
    def test_can_create_anonymous_spark_dataframes_from_class_with_constructor_class_arguments(self, cls):
        cls.show()
        self.assertIsNotNone(cls.a)
        self.assertIsNotNone(cls.b)


@dataclass
class DataClass:
    id: int
    name: str
    text: str


@unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
class AnonymousSparkDataFrameViaDecoratorFromDataClassTests(unittest.TestCase):

    @autospark(DataClass)
    def test_create_anonymous_spark_dataframe_returns_not_none(self, df: DataFrame):
        self.assertIsNotNone(df)

    @autospark(DataClass, 10)
    def test_create_anonymous_spark_dataframe_with_rowcount_returns_not_empty(self, df: DataFrame):
        self.assertNotEqual(df.count(), 0)

    @fakespark(DataClass, 10)
    def test_create_fake_spark_dataframe_with_rowcount_returns_not_empty(self, df: DataFrame):
        self.assertNotEqual(df.count(), 0)

    @fakespark(DataClass)
    def test_create_fake_spark_dataframe_returns_not_none(self, df: DataFrame):
        self.assertIsNotNone(df)
