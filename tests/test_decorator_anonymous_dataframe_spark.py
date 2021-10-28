import sys
import unittest
from dataclasses import dataclass

from pyspark.sql import DataFrame

from autofaker import autospark, fakespark


class SimpleClass:
    id = -1
    name = 'test'
    text = 'test'


class AnonymousSparkDataFrameViaDecoratorTests(unittest.TestCase):

    @autospark(SimpleClass)
    @unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
    def test_create_anonymous_spark_dataframe_returns_not_none(self, df: DataFrame):
        self.assertIsNotNone(df)

    @autospark(SimpleClass, 10)
    @unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
    def test_create_anonymous_spark_dataframe_with_rowcount_returns_not_empty(self, df: DataFrame):
        self.assertNotEqual(df.count(), 0)

    @fakespark(SimpleClass)
    @unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
    def test_create_fake_spark_dataframe_returns_not_none(self, df: DataFrame):
        self.assertIsNotNone(df)

    @fakespark(SimpleClass, 10)
    @unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
    def test_create_fake_spark_dataframe_with_rowcount_returns_not_empty(self, df: DataFrame):
        self.assertNotEqual(df.count(), 0)


@dataclass
class DataClass:
    id: int
    name: str
    text: str


class AnonymousSparkDataFrameViaDecoratorFromDataClassTests(unittest.TestCase):

    @autospark(DataClass)
    @unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
    def test_create_anonymous_spark_dataframe_returns_not_none(self, df: DataFrame):
        self.assertIsNotNone(df)

    @autospark(DataClass, 10)
    @unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
    def test_create_anonymous_spark_dataframe_with_rowcount_returns_not_empty(self, df: DataFrame):
        self.assertNotEqual(df.count(), 0)

    @fakespark(DataClass, 10)
    @unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
    def test_create_fake_spark_dataframe_with_rowcount_returns_not_empty(self, df: DataFrame):
        self.assertNotEqual(df.count(), 0)

    @fakespark(DataClass)
    @unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
    def test_create_fake_spark_dataframe_returns_not_none(self, df: DataFrame):
        self.assertIsNotNone(df)
