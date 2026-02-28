"""Tests for bug fixes."""

import unittest
from dataclasses import dataclass
from typing import List

import pandas as pd

from autofaker import Autodata, autodata, fakedata


class ClassWithReturnAnnotation:
    def __init__(self, x: int, y: str) -> None:
        self.x = x
        self.y = y


class ClassWithReturnAnnotationAndList:
    def __init__(self, values: List[int], name: str) -> None:
        self.values = values
        self.name = name


@dataclass
class DataClassWithIntList:
    numbers: List[int]


@dataclass
class SimpleDataClass:
    id: int
    name: str


class TestListGeneratorUseFakeData(unittest.TestCase):
    """Bug fix: ListGenerator was not receiving use_fake_data parameter."""

    def test_create_list_with_fake_data_passes_flag(self):
        result = Autodata.create(DataClassWithIntList, use_fake_data=True)
        self.assertIsNotNone(result)
        self.assertIsInstance(result.numbers, list)
        self.assertEqual(len(result.numbers), 3)
        for n in result.numbers:
            self.assertIsInstance(n, int)

    def test_create_list_without_fake_data(self):
        result = Autodata.create(DataClassWithIntList, use_fake_data=False)
        self.assertIsNotNone(result)
        self.assertIsInstance(result.numbers, list)
        self.assertEqual(len(result.numbers), 3)


class TestClassWithReturnAnnotation(unittest.TestCase):
    """Bug fix: _create_with_init_args included 'return' annotation."""

    def test_create_class_with_return_annotation(self):
        result = Autodata.create(ClassWithReturnAnnotation)
        self.assertIsNotNone(result)
        self.assertIsInstance(result.x, int)
        self.assertIsInstance(result.y, str)

    def test_create_class_with_return_annotation_and_list(self):
        result = Autodata.create(ClassWithReturnAnnotationAndList)
        self.assertIsNotNone(result)
        self.assertIsInstance(result.values, list)
        self.assertIsInstance(result.name, str)

    def test_create_many_class_with_return_annotation(self):
        results = Autodata.create_many(ClassWithReturnAnnotation, size=3)
        self.assertEqual(len(results), 3)
        for result in results:
            self.assertIsInstance(result.x, int)
            self.assertIsInstance(result.y, str)


class TestDecoratorWithReturnAnnotation(unittest.TestCase):
    """Bug fix: __create_function_args included 'return' annotation."""

    @autodata()
    def test_autodata_with_return_annotation(self, x: int, y: str) -> None:
        self.assertIsNotNone(x)
        self.assertIsNotNone(y)
        self.assertIsInstance(x, int)
        self.assertIsInstance(y, str)

    @fakedata()
    def test_fakedata_with_return_annotation(self, x: int, y: str) -> None:
        self.assertIsNotNone(x)
        self.assertIsNotNone(y)
        self.assertIsInstance(x, int)
        self.assertIsInstance(y, str)

    @autodata(int, str)
    def test_autodata_explicit_types_with_return_annotation(self, x, y) -> None:
        self.assertIsNotNone(x)
        self.assertIsNotNone(y)
        self.assertIsInstance(x, int)
        self.assertIsInstance(y, str)


class TestPrimitiveTypesForFutureAnnotations(unittest.TestCase):
    """Bug fix: PRIMITIVE_TYPES was missing 'bool' and 'memoryview'."""

    def test_get_type_name_for_bool_string(self):
        from autofaker.generator import TypeDataGenerator
        type_name = TypeDataGenerator._get_type_name("bool").lower()
        self.assertEqual(type_name, "bool")

    def test_get_type_name_for_memoryview_string(self):
        from autofaker.generator import TypeDataGenerator
        type_name = TypeDataGenerator._get_type_name("memoryview").lower()
        self.assertEqual(type_name, "memoryview")


class TestDataFrameWithZeroRows(unittest.TestCase):
    """Bug fix: PandasDataFrameGenerator crashed with rows=0."""

    def test_create_dataframe_with_zero_rows(self):
        df = Autodata.create_pandas_dataframe(SimpleDataClass, rows=0)
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.empty)
        self.assertEqual(len(df), 0)

    def test_create_dataframe_with_one_row(self):
        df = Autodata.create_pandas_dataframe(SimpleDataClass, rows=1)
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 1)


if __name__ == "__main__":
    unittest.main()
