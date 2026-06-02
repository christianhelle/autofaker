import contextlib
import io
import unittest
from typing import List, Optional
from unittest.mock import patch

import pandas as pd

from autofaker.generator import ClassGenerator, TypeDataGenerator


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


class TypeDataGeneratorIsOptionalTestCase(unittest.TestCase):
    def test_is_optional_true_for_optional(self):
        self.assertTrue(TypeDataGenerator._is_optional(Optional[int]))

    def test_is_optional_false_for_plain_type(self):
        self.assertFalse(TypeDataGenerator._is_optional(int))


class ClassGeneratorDataFrameTestCase(unittest.TestCase):
    def test_is_supported_false_for_dataframe(self):
        gen = object.__new__(ClassGenerator)
        gen.instance = pd.DataFrame({"a": [1]})
        self.assertFalse(gen._is_supported())

    def test_generate_returns_none_for_dataframe(self):
        gen = object.__new__(ClassGenerator)
        gen.use_fake_data = False
        gen.instance = pd.DataFrame({"a": [1]})
        self.assertIsNone(gen.generate())


class _NoAnnotations:
    """Class with no class-level annotations, but instances can carry them."""


class ClassGeneratorInstanceAnnotationsTestCase(unittest.TestCase):
    def test_generate_reads_instance_annotations_when_class_lacks_them(self):
        gen = object.__new__(ClassGenerator)
        gen.use_fake_data = False
        instance = _NoAnnotations()
        # Set annotations only on the instance, not on the class
        instance.__annotations__ = {"note": int}
        gen.instance = instance

        # PEP 526 makes Python always expose a class-level __annotations__.
        # Force the elif branch by hiding it for the class lookup only.
        real_hasattr = hasattr
        def fake_hasattr(obj, name):
            if name == "__annotations__" and obj is type(instance):
                return False
            return real_hasattr(obj, name)

        with patch("builtins.hasattr", side_effect=fake_hasattr):
            result = gen.generate()

        # The annotations are processed but produce no changes since "note"
        # is not a Literal. The point is to exercise the elif branch.
        self.assertIs(result, instance)


class ClassGeneratorTryGenerateTestCase(unittest.TestCase):
    def test_try_generate_swallows_typeerror(self):
        gen = object.__new__(ClassGenerator)
        gen.use_fake_data = False

        class _Holder:
            attr = 1

        gen.instance = _Holder()

        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), \
             patch("autofaker.generator.registry.resolve",
                   side_effect=TypeError("nope")):
            result = gen._try_generate("attr")

        self.assertIsNone(result)
        self.assertIn("nope", buf.getvalue())


class _BareListInit:
    def __init__(self, items: List, name: str = "x") -> None:
        self.items = items
        self.name = name


class ClassGeneratorBareListInitTestCase(unittest.TestCase):
    def test_create_with_bare_list_annotation_uses_empty_list(self):
        # Annotation ``List`` (capital L, no []) yields an empty list at
        # construction time. Verify the generator succeeds and the list is
        # empty rather than populated.
        gen = ClassGenerator(_BareListInit, use_fake_data=False)
        instance = gen.generate()
        self.assertIsInstance(instance, _BareListInit)
        self.assertEqual(instance.items, [])


if __name__ == "__main__":
    unittest.main()
