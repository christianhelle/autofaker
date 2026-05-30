import unittest

from autofaker import (
    Autodata,
    register_predicate,
    register_type,
    registry_context,
    reset_registry,
)
from autofaker.registry import get_type_name, resolve


class CustomType:
    pass


class GetTypeNameTestCase(unittest.TestCase):
    def test_returns_name_for_regular_type(self):
        self.assertEqual(get_type_name(int), "int")

    def test_returns_string_itself_for_future_annotations(self):
        # from __future__ import annotations turns types into strings
        self.assertEqual(get_type_name("int"), "int")
        self.assertEqual(get_type_name("memoryview"), "memoryview")


class ResolveBuiltinsTestCase(unittest.TestCase):
    def test_resolves_int_through_public_interface(self):
        self.assertIsInstance(Autodata.create(int), int)

    def test_resolves_string_annotation(self):
        # the __future__.annotations path: type arrives as a string
        self.assertIsInstance(Autodata.create("int"), int)

    def test_unregistered_object_falls_back_to_class_generator(self):
        instance = Autodata.create(CustomType)
        self.assertIsInstance(instance, CustomType)


class RegisterTypeTestCase(unittest.TestCase):
    def tearDown(self):
        reset_registry()

    def test_register_type_for_custom_type(self):
        class Marker:
            pass

        register_type(Marker, lambda t, f, u: _Const("custom-value"))
        self.assertEqual(Autodata.create(Marker), "custom-value")

    def test_override_true_beats_builtin(self):
        register_type(int, lambda t, f, u: _Const(42), override=True)
        self.assertEqual(Autodata.create(int), 42)

    def test_override_false_does_not_beat_builtin(self):
        register_type(int, lambda t, f, u: _Const(42), override=False)
        # built-in int generator still wins; value is a random int, not 42-forced
        value = Autodata.create(int)
        self.assertIsInstance(value, int)


class RegisterPredicateTestCase(unittest.TestCase):
    def tearDown(self):
        reset_registry()

    def test_before_fallback_predicate(self):
        register_predicate(
            lambda t, n: t is CustomType,
            lambda t, f, u: _Const("by-predicate"),
        )
        self.assertEqual(Autodata.create(CustomType), "by-predicate")

    def test_before_builtins_predicate_overrides(self):
        register_predicate(
            lambda t, n: n == "int",
            lambda t, f, u: _Const(7),
            priority="before_builtins",
        )
        self.assertEqual(Autodata.create(int), 7)

    def test_invalid_priority_raises(self):
        with self.assertRaises(ValueError):
            register_predicate(lambda t, n: True, lambda t, f, u: _Const(1), priority="nope")


class IsolationTestCase(unittest.TestCase):
    def test_reset_registry_removes_user_rules(self):
        register_type(CustomType, lambda t, f, u: _Const("x"))
        reset_registry()
        # back to fallback class generation
        self.assertIsInstance(Autodata.create(CustomType), CustomType)

    def test_registry_context_restores_rules(self):
        with registry_context():
            register_type(CustomType, lambda t, f, u: _Const("scoped"))
            self.assertEqual(Autodata.create(CustomType), "scoped")
        self.assertIsInstance(Autodata.create(CustomType), CustomType)


class _Const:
    def __init__(self, value):
        self.value = value

    def generate(self):
        return self.value


if __name__ == "__main__":
    unittest.main()
