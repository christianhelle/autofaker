import unittest
from dataclasses import dataclass

import pandas

from autofaker import autopandas, fakepandas, autodata


class SimpleClassA:
    id = -1
    name: 'test'
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


class AnonymousPandasDataFrameViaDecoratorTests(unittest.TestCase):

    @autopandas(SimpleClassA)
    def test_create_anonymous_pandas_dataframe_returns_not_none(self, df: pandas.DataFrame):
        self.assertIsNotNone(df)

    @autopandas(SimpleClassA, 10)
    def test_create_anonymous_pandas_dataframe_with_rowcount_returns_not_empty(self, df: pandas.DataFrame):
        self.assertNotEqual(len(df.index), 0)

    @fakepandas(SimpleClassA)
    def test_create_fake_pandas_dataframe_returns_not_none(self, df: pandas.DataFrame):
        self.assertIsNotNone(df)

    @fakepandas(SimpleClassA, 10)
    def test_create_fake_pandas_dataframe_with_rowcount_returns_not_empty(self, df: pandas.DataFrame):
        self.assertNotEqual(len(df.index), 0)

    @autopandas(SimpleClassA)
    def test_can_create_anonymous_pandas_dataframes(self, cls):
        self.assertIsNotNone(cls)

    @autopandas(SimpleClassB)
    def test_can_create_anonymous_pandas_dataframes_from_class_with_constructor_arguments(self, cls):
        self.assertIsNotNone(cls)

    @autopandas(SimpleClassC)
    def test_can_create_anonymous_pandas_dataframes_from_class_with_constructor_class_arguments(self, cls):
        self.assertIsNotNone(cls)


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


class AutodataDecoratorIgnoresPandas(unittest.TestCase):

    @autodata()
    def test_autodata_decorator_ignores_pandas_dataframe(self, df: pandas.DataFrame):
        self.assertIsNone(df)

    @autodata()
    def test_autodata_decorator_ignores_only_pandas_dataframe(self, text: str, df: pandas.DataFrame):
        self.assertIsNotNone(text)
        self.assertIsNone(df)
