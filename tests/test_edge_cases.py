"""
Tests for edge cases and bug fixes in autofaker.
"""
import unittest
from dataclasses import dataclass
from enum import Enum
from typing import List

from autofaker import Autodata, autodata, fakedata


class EmptyListTypeTestCase(unittest.TestCase):
    """Test that empty list types don't cause IndexError."""
    
    def test_create_unparameterized_list_returns_empty_list(self):
        """Creating an unparameterized list type should return an empty list."""
        result = Autodata.create(list)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)


class EmptyDataFrameTestCase(unittest.TestCase):
    """Test that DataFrames with zero rows don't cause IndexError."""
    
    def test_create_dataframe_with_zero_rows(self):
        """Creating a DataFrame with zero rows should return an empty DataFrame."""
        @dataclass
        class DataRow:
            id: int
            name: str
        
        df = Autodata.create_pandas_dataframe(DataRow, rows=0)
        self.assertEqual(len(df), 0)


class DatetimeMicrosecondRangeTestCase(unittest.TestCase):
    """Test that datetime microseconds are in the correct range."""
    
    def test_datetime_microsecond_in_valid_range(self):
        """Microseconds should be in range 0-999999, not 0-999."""
        import datetime
        for _ in range(10):  # Test multiple times due to randomness
            dt = Autodata.create(datetime.datetime)
            self.assertGreaterEqual(dt.microsecond, 0)
            self.assertLessEqual(dt.microsecond, 999999)


class DecoratorWithoutParenthesesTestCase(unittest.TestCase):
    """Test that decorators work with and without parentheses."""
    
    @autodata
    def test_autodata_without_parentheses(self, a: int, b: str):
        """@autodata should work without parentheses using type annotations."""
        self.assertIsInstance(a, int)
        self.assertIsInstance(b, str)
    
    @autodata()
    def test_autodata_with_empty_parentheses(self, a: int, b: str):
        """@autodata() should work with empty parentheses using type annotations."""
        self.assertIsInstance(a, int)
        self.assertIsInstance(b, str)
    
    @autodata(int, str)
    def test_autodata_with_types(self, a, b):
        """@autodata(int, str) should work with explicit types."""
        self.assertIsInstance(a, int)
        self.assertIsInstance(b, str)
    
    @fakedata
    def test_fakedata_without_parentheses(self, a: int, b: str):
        """@fakedata should work without parentheses using type annotations."""
        self.assertIsInstance(a, int)
        self.assertIsInstance(b, str)
    
    @fakedata()
    def test_fakedata_with_empty_parentheses(self, a: int, b: str):
        """@fakedata() should work with empty parentheses using type annotations."""
        self.assertIsInstance(a, int)
        self.assertIsInstance(b, str)
    
    @fakedata(int, str)
    def test_fakedata_with_types(self, a, b):
        """@fakedata(int, str) should work with explicit types."""
        self.assertIsInstance(a, int)
        self.assertIsInstance(b, str)


class EnumGeneratorEdgeCaseTestCase(unittest.TestCase):
    """Test enum generation edge cases."""
    
    def test_single_value_enum(self):
        """Enum with single value should be generated correctly."""
        class SingleValueEnum(Enum):
            ONLY = "only"
        
        result = Autodata.create(SingleValueEnum)
        self.assertIsInstance(result, SingleValueEnum)
        self.assertEqual(result, SingleValueEnum.ONLY)


if __name__ == "__main__":
    unittest.main()
