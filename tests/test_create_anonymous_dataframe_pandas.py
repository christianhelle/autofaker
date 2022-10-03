import unittest
from dataclasses import dataclass

from autofaker import Autodata


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


class CreateAnonymousPandasDataFrameTests(unittest.TestCase):

    def test_create_anonymous_pandas_dataframe_returns_not_none(self):
        df = Autodata.create_pandas_dataframe(SimpleClassA)
        self.assertIsNotNone(df)

    def test_create_anonymous_pandas_dataframe_returns_not_empty(self):
        df = Autodata.create_pandas_dataframe(SimpleClassA)
        self.assertNotEqual(len(df.index), 0)

    def test_create_anonymous_pandas_dataframe_with_rowcount_returns_not_empty(self):
        df = Autodata.create_pandas_dataframe(SimpleClassA, 10)
        self.assertEqual(len(df.index), 10)

    def test_can_create_anonymous_pandas_dataframes_from_class_with_constructor_arguments(self):
        df = Autodata.create_pandas_dataframe(SimpleClassB)
        self.assertTrue('id' in df.columns)
        self.assertTrue('name' in df.columns)
        self.assertTrue('text' in df.columns)

    def test_can_create_anonymous_pandas_dataframes_from_class_with_constructor_class_arguments(self):
        df = Autodata.create_pandas_dataframe(SimpleClassC)
        self.assertTrue('a' in df.columns)
        self.assertTrue('b' in df.columns)


class CreateFakePandasDataFrameTests(unittest.TestCase):

    def test_create_fake_pandas_dataframe_returns_not_none(self):
        df = Autodata.create_pandas_dataframe(SimpleClassA, use_fake_data=True)
        self.assertIsNotNone(df)

    def test_create_fake_pandas_dataframe_returns_not_empty(self):
        df = Autodata.create_pandas_dataframe(SimpleClassA, use_fake_data=True)
        self.assertNotEqual(len(df.index), 0)

    def test_create_fake_pandas_dataframe_with_rowcount_returns_not_empty(self):
        df = Autodata.create_pandas_dataframe(SimpleClassA, 10, use_fake_data=True)
        self.assertEqual(len(df.index), 10)

    def test_can_create_fake_pandas_dataframes_from_class_with_constructor_arguments(self):
        df = Autodata.create_pandas_dataframe(SimpleClassB, use_fake_data=True)
        self.assertTrue('id' in df.columns)
        self.assertTrue('name' in df.columns)
        self.assertTrue('text' in df.columns)

    def test_can_create_fake_pandas_dataframes_from_class_with_constructor_class_arguments(self):
        df = Autodata.create_pandas_dataframe(SimpleClassC, use_fake_data=True)
        self.assertTrue('a' in df.columns)
        self.assertTrue('b' in df.columns)


@dataclass
class DataClass:
    id: int
    name: str
    text: str


class HybridClassA:
    def __init__(self, a: DataClass, b: SimpleClassA):
        self.b = b
        self.a = a


class HybridClassB:
    def __init__(self, a: DataClass, b: SimpleClassA, c: HybridClassA):
        self.c = c
        self.b = b
        self.a = a


class CreateAnonymousPandasDataFrameFromDataClassTests(unittest.TestCase):

    def test_create_anonymous_pandas_dataframe_returns_not_none(self):
        df = Autodata.create_pandas_dataframe(DataClass)
        self.assertIsNotNone(df)

    def test_create_anonymous_pandas_dataframe_returns_not_empty(self):
        df = Autodata.create_pandas_dataframe(DataClass)
        self.assertNotEqual(len(df.index), 0)

    def test_create_anonymous_pandas_dataframe_with_rowcount_returns_not_empty(self):
        df = Autodata.create_pandas_dataframe(DataClass, 10)
        self.assertEqual(len(df.index), 10)

    def test_can_create_anonymous_pandas_dataframes_from_class_with_constructor_class_arguments(self):
        df = Autodata.create_pandas_dataframe(HybridClassA)
        self.assertTrue('b' in df.columns)
        self.assertTrue('a' in df.columns)

    def test_can_create_anonymous_pandas_dataframes_from_class_with_constructor_hybrid_class_arguments(self):
        df = Autodata.create_pandas_dataframe(HybridClassB)
        self.assertTrue('c' in df.columns)
        self.assertTrue('b' in df.columns)
        self.assertTrue('a' in df.columns)


class CreateFakePandasDataFrameFromDataClassTests(unittest.TestCase):

    def test_create_fake_pandas_dataframe_returns_not_none(self):
        df = Autodata.create_pandas_dataframe(DataClass, use_fake_data=True)
        self.assertIsNotNone(df)

    def test_create_fake_pandas_dataframe_returns_not_empty(self):
        df = Autodata.create_pandas_dataframe(DataClass, use_fake_data=True)
        self.assertNotEqual(len(df.index), 0)

    def test_create_fake_pandas_dataframe_with_rowcount_returns_not_empty(self):
        df = Autodata.create_pandas_dataframe(DataClass, 10, use_fake_data=True)
        self.assertEqual(len(df.index), 10)

    def test_can_create_fake_pandas_dataframes_from_class_with_constructor_class_arguments(self):
        df = Autodata.create_pandas_dataframe(HybridClassA, use_fake_data=True)
        self.assertTrue('b' in df.columns)
        self.assertTrue('a' in df.columns)

    def test_can_create_anonymous_pandas_dataframes_from_class_with_constructor_hybrid_class_arguments(self):
        df = Autodata.create_pandas_dataframe(HybridClassB, use_fake_data=True)
        self.assertTrue('c' in df.columns)
        self.assertTrue('b' in df.columns)
        self.assertTrue('a' in df.columns)
