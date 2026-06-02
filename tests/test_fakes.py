import io
import unittest
from contextlib import redirect_stdout

from autofaker.fakes import (
    FakeIntegerGenerator,
    FakeStringGenerator,
    generate,
)


class FakesTestCase(unittest.TestCase):
    def test_generate_returns_callable_result(self):
        result = generate("name")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_generate_returns_none_for_unknown_field(self):
        # faker has no method named "definitely_not_a_faker_method_xyz";
        # the AttributeError is caught and None is returned.
        result = generate("definitely_not_a_faker_method_xyz")
        self.assertIsNone(result)

    def test_fake_string_generator_falls_back_to_plain_string(self):
        # Unknown field name -> generate() returns None -> StringGenerator
        # is used as the fallback. Capture stdout to keep test output clean.
        buf = io.StringIO()
        with redirect_stdout(buf):
            value = FakeStringGenerator("definitely_not_a_faker_method_xyz").generate()
        self.assertIsInstance(value, str)
        self.assertGreater(len(value), 0)

    def test_fake_integer_generator_returns_int(self):
        value = FakeIntegerGenerator().generate()
        self.assertIsInstance(value, int)
        self.assertGreaterEqual(value, 1)
        self.assertLessEqual(value, 10000)


if __name__ == "__main__":
    unittest.main()
