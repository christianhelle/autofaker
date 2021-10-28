import unittest
from dataclasses import dataclass

import pandas

from autofaker import autopandas, fakepandas


class SimpleClass:
    id = -1
    name: 'test'
    text = 'test'


class AnonymousPandasDataFrameViaDecoratorTests(unittest.TestCase):

    @autopandas(SimpleClass)
    def test_create_anonymous_pandas_dataframe_returns_not_none(self, df: pandas.DataFrame):
        self.assertIsNotNone(df)

    @autopandas(SimpleClass, 10)
    def test_create_anonymous_pandas_dataframe_with_rowcount_returns_not_empty(self, df: pandas.DataFrame):
        self.assertNotEqual(len(df.index), 0)

    @fakepandas(SimpleClass)
    def test_create_fake_pandas_dataframe_returns_not_none(self, df: pandas.DataFrame):
        self.assertIsNotNone(df)

    @fakepandas(SimpleClass, 10)
    def test_create_fake_pandas_dataframe_with_rowcount_returns_not_empty(self, df: pandas.DataFrame):
        self.assertNotEqual(len(df.index), 0)


@dataclass
class DataClass:
    id: int
    name: str
    text: str


class AnonymousPandasDataFrameViaDecoratorFromDataClassTests(unittest.TestCase):

    @autopandas(DataClass)
    def test_create_anonymous_pandas_dataframe_returns_not_none(self, df: pandas.DataFrame):
        self.assertIsNotNone(df)

    @autopandas(DataClass, 10)
    def test_create_anonymous_pandas_dataframe_with_rowcount_returns_not_empty(self, df: pandas.DataFrame):
        self.assertNotEqual(len(df.index), 0)

    @fakepandas(DataClass, 10)
    def test_create_fake_pandas_dataframe_with_rowcount_returns_not_empty(self, df: pandas.DataFrame):
        self.assertNotEqual(len(df.index), 0)

    @fakepandas(DataClass)
    def test_create_fake_pandas_dataframe_returns_not_none(self, df: pandas.DataFrame):
        self.assertIsNotNone(df)
