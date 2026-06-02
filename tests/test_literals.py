import unittest
from typing import Literal
from unittest.mock import patch

from autofaker.literals import LiteralGenerator, is_literal_type


class IsLiteralTypeTestCase(unittest.TestCase):
    def test_returns_true_for_literal(self):
        self.assertTrue(is_literal_type(Literal["a", "b"]))

    def test_returns_false_for_non_literal(self):
        self.assertFalse(is_literal_type(int))
        self.assertFalse(is_literal_type("Literal"))


class LiteralGeneratorTestCase(unittest.TestCase):
    def test_raises_for_non_literal_type(self):
        with self.assertRaises(ValueError) as ctx:
            LiteralGenerator(int)
        self.assertIn("Expected Literal type", str(ctx.exception))

    def test_raises_for_literal_with_no_values(self):
        # is_literal_type must accept the object for the constructor to reach
        # the empty-args check. Patch the helpers to simulate a degenerate case.
        with patch("autofaker.literals.is_literal_type", return_value=True), \
             patch("autofaker.literals.get_args", return_value=()):
            with self.assertRaises(ValueError) as ctx:
                LiteralGenerator(object())
            self.assertIn("at least one value", str(ctx.exception))

    def test_generate_picks_from_allowed_values(self):
        gen = LiteralGenerator(Literal["x", "y", "z"])
        self.assertIn(gen.generate(), {"x", "y", "z"})


if __name__ == "__main__":
    unittest.main()
