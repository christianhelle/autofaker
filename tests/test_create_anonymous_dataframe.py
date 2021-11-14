import sys
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


@unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
class CreateAnonymousSparkDataFrameTests(unittest.TestCase):

    def test_create_anonymous_spark_dataframe_returns_not_none(self):
        df = Autodata.create_spark_dataframe(SimpleClassA)
        self.assertIsNotNone(df)

    def test_create_anonymous_spark_dataframe_returns_not_empty(self):
        df = Autodata.create_spark_dataframe(SimpleClassA)
        self.assertNotEqual(df.count(), 0)

    def test_create_anonymous_spark_dataframe_with_rowcount_returns_not_empty(self):
        df = Autodata.create_spark_dataframe(SimpleClassA, 10)
        self.assertEqual(df.count(), 10)

    def test_can_create_anonymous_spark_dataframes_from_class_with_constructor_arguments(self):
        df = Autodata.create_spark_dataframe(SimpleClassB)
        self.assertTrue('id' in df.schema.fieldNames())
        self.assertTrue('name' in df.schema.fieldNames())
        self.assertTrue('text' in df.schema.fieldNames())

    def test_can_create_anonymous_spark_dataframes_from_class_with_constructor_class_arguments(self):
        df = Autodata.create_spark_dataframe(SimpleClassC)
        self.assertTrue('a' in df.schema.fieldNames())
        self.assertTrue('b' in df.schema.fieldNames())


@unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
class CreateFakeSparkDataFrameTests(unittest.TestCase):

    def test_create_fake_spark_dataframe_returns_not_none(self):
        df = Autodata.create_spark_dataframe(SimpleClassA, use_fake_data=True)
        self.assertIsNotNone(df)

    def test_create_fake_spark_dataframe_returns_not_empty(self):
        df = Autodata.create_spark_dataframe(SimpleClassA, use_fake_data=True)
        self.assertNotEqual(df.count(), 0)

    def test_create_fake_spark_dataframe_with_rowcount_returns_not_empty(self):
        df = Autodata.create_spark_dataframe(SimpleClassA, 10, use_fake_data=True)
        self.assertEqual(df.count(), 10)

    def test_can_create_fake_spark_dataframes_from_class_with_constructor_arguments(self):
        df = Autodata.create_spark_dataframe(SimpleClassB, use_fake_data=True)
        self.assertTrue('id' in df.schema.fieldNames())
        self.assertTrue('name' in df.schema.fieldNames())
        self.assertTrue('text' in df.schema.fieldNames())

    def test_can_create_fake_spark_dataframes_from_class_with_constructor_class_arguments(self):
        df = Autodata.create_spark_dataframe(SimpleClassC, use_fake_data=True)
        self.assertTrue('a' in df.schema.fieldNames())
        self.assertTrue('b' in df.schema.fieldNames())
