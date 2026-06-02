import unittest

from autofaker.base import TypeDataGeneratorBase


class TypeDataGeneratorBaseTestCase(unittest.TestCase):
    def test_abstract_generate_body_returns_none(self):
        # Calling the abstract method on a subclass that has not overridden
        # it executes the base body (pass) and returns None. This keeps the
        # abstract contract in place while covering the base implementation.
        class _Unimplemented(TypeDataGeneratorBase):
            pass

        instance = object.__new__(_Unimplemented)
        self.assertIsNone(TypeDataGeneratorBase.generate(instance))


if __name__ == "__main__":
    unittest.main()
