import unittest

from autofaker.generator import TypeDataGenerator


class TypeDataGeneratorGetTypeNameTestCase(unittest.TestCase):
    def test_get_type_name_for_regular_type(self):
        """Test that regular types return their __name__ attribute"""
        result = TypeDataGenerator._get_type_name(int)
        self.assertEqual(result, "int")

    def test_get_type_name_for_str_type(self):
        """Test that str type returns correct name"""
        result = TypeDataGenerator._get_type_name(str)
        self.assertEqual(result, "str")

    def test_get_type_name_for_string_literal(self):
        """Bug fix: t.isinstance(str) was incorrectly used instead of isinstance(t, str)
        
        When __future__.annotations is used, types become strings.
        The code now correctly uses isinstance(t, str) to check for string types.
        """
        result = TypeDataGenerator._get_type_name("str")
        self.assertEqual(result, "str")

    def test_get_type_name_for_primitive_type_strings(self):
        """Test that primitive type names are correctly recognized as strings"""
        primitive_types = ["int", "float", "str", "complex", "range", "bytes", "bytearray", "bool", "memoryview"]
        for type_name in primitive_types:
            result = TypeDataGenerator._get_type_name(type_name)
            self.assertEqual(result, type_name)
