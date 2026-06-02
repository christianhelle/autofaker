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

    def test_returns_name_for_typing_optional(self):
        from typing import Optional
        self.assertEqual(get_type_name(Optional[str]), "Optional")

    def test_returns_type_name_for_non_primitive_string(self):
        self.assertEqual(get_type_name("datetime"), "str")


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

    def test_register_type_does_not_collide_on_shared_name(self):
        # two distinct classes that share a __name__ must not hijack each other
        def make_money():
            class Money:
                pass
            return Money

        money_a = make_money()
        money_b = make_money()
        self.assertEqual(money_a.__name__, money_b.__name__)

        register_type(money_a, lambda t, f, u: _Const("a-value"))
        self.assertEqual(Autodata.create(money_a), "a-value")
        # money_b is a different type object -> falls back to class generation
        self.assertIsInstance(Autodata.create(money_b), money_b)

    def test_override_true_beats_builtin(self):
        # sentinel of a non-int type: the built-in int generator can never
        # produce this, so the assertion proves the override won
        register_type(int, lambda t, f, u: _Const("OVERRIDDEN"), override=True)
        self.assertEqual(Autodata.create(int), "OVERRIDDEN")

    def test_override_false_does_not_beat_builtin(self):
        # custom rule returns a non-int sentinel; with override=False the
        # built-in int generator must win, so the result is a real int
        register_type(int, lambda t, f, u: _Const("SHOULD_NOT_WIN"), override=False)
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
        # non-int sentinel makes the test deterministic: a real int generator
        # could otherwise produce the same int by chance
        register_predicate(
            lambda t, n: n == "int",
            lambda t, f, u: _Const("PREDICATE_WON"),
            priority="before_builtins",
        )
        self.assertEqual(Autodata.create(int), "PREDICATE_WON")

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


class ResolveErrorTestCase(unittest.TestCase):
    def test_no_generator_raises_typeerror(self):
        import autofaker.registry as registry
        saved_rules = list(registry._builtin_rules)
        saved_fallback = registry._fallback
        saved_front = list(registry._user_front)
        saved_back = list(registry._user_back)
        try:
            reset_registry()
            registry._builtin_rules.clear()
            registry._fallback = None
            with self.assertRaises(TypeError) as ctx:
                registry.resolve(int)
            self.assertIn("int", str(ctx.exception))
        finally:
            registry._user_front[:] = saved_front
            registry._user_back[:] = saved_back
            registry._builtin_rules[:] = saved_rules
            registry._fallback = saved_fallback


class _Const:
    def __init__(self, value):
        self.value = value

    def generate(self):
        return self.value


if __name__ == "__main__":
    unittest.main()
