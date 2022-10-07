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


# Anonymous Pandas DataFrame Via Decorator

@autopandas(SimpleClassA)
def test_create_anonymous_pandas_dataframe_returns_not_none(df: pandas.DataFrame):
    assert df is not None


@autopandas(SimpleClassA, 10)
def test_create_anonymous_pandas_dataframe_with_rowcount_returns_not_empty(df: pandas.DataFrame):
    assert len(df.index) != 0


@fakepandas(SimpleClassA)
def test_create_fake_pandas_dataframe_returns_not_none(df: pandas.DataFrame):
    assert df is not None


@fakepandas(SimpleClassA, 10)
def test_create_fake_pandas_dataframe_with_rowcount_returns_not_empty(df: pandas.DataFrame):
    assert len(df.index) != 0


@autopandas(SimpleClassA)
def test_can_create_anonymous_pandas_dataframes(cls):
    print(cls)
    assert not cls.empty


@autopandas(SimpleClassB)
def test_can_create_anonymous_pandas_dataframes_from_class_with_constructor_arguments(cls):
    print(cls)
    assert not cls.empty


@autopandas(SimpleClassC)
def test_can_create_anonymous_pandas_dataframes_from_class_with_constructor_class_arguments(cls):
    print(cls)
    assert not cls.empty


@dataclass
class DataClass:
    id: int
    name: str
    text: str


# Anonymous Pandas DataFrame Via Decorator From DataClass

@autopandas(DataClass)
def test_create_anonymous_pandas_dataframe_returns_not_none(df: pandas.DataFrame):
    assert df is not None


@autopandas(DataClass, 10)
def test_create_anonymous_pandas_dataframe_with_rowcount_returns_not_empty(df: pandas.DataFrame):
    assert len(df.index) != 0


@fakepandas(DataClass, 10)
def test_create_fake_pandas_dataframe_with_rowcount_returns_not_empty(df: pandas.DataFrame):
    assert len(df.index) != 0


@fakepandas(DataClass)
def test_create_fake_pandas_dataframe_returns_not_none(df: pandas.DataFrame):
    assert df is not None


# Autodata Decorator Ignores Pandas

@autodata()
def test_autodata_decorator_ignores_pandas_dataframe(df: pandas.DataFrame):
    assert df is None


@autodata()
def test_autodata_decorator_ignores_only_pandas_dataframe(text: str, df: pandas.DataFrame):
    assert None is not text
    assert df is None
