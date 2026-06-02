import unittest
from typing import Dict, FrozenSet, List, Set, Tuple

from autofaker.generator import CollectionGenerator, DEFAULT_COLLECTION_SIZE


class CollectionGeneratorTestCase(unittest.TestCase):
    def test_typed_list_produces_default_size(self):
        result = CollectionGenerator("list", List[int]).generate()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), DEFAULT_COLLECTION_SIZE)
        self.assertTrue(all(isinstance(x, int) for x in result))

    def test_untyped_list_is_empty(self):
        result = CollectionGenerator("list", list).generate()
        self.assertEqual(result, [])

    def test_fixed_length_tuple_matches_declared_types(self):
        result = CollectionGenerator("tuple", Tuple[int, str]).generate()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], str)

    def test_variable_length_tuple_uses_default_size(self):
        result = CollectionGenerator("tuple", Tuple[int, ...]).generate()
        self.assertEqual(len(result), DEFAULT_COLLECTION_SIZE)
        self.assertTrue(all(isinstance(x, int) for x in result))

    def test_set_returns_set(self):
        result = CollectionGenerator("set", Set[str]).generate()
        self.assertIsInstance(result, set)
        self.assertTrue(all(isinstance(x, str) for x in result))

    def test_frozenset_returns_frozenset(self):
        result = CollectionGenerator("frozenset", FrozenSet[str]).generate()
        self.assertIsInstance(result, frozenset)

    def test_dict_returns_typed_mapping(self):
        result = CollectionGenerator("dict", Dict[str, int]).generate()
        self.assertIsInstance(result, dict)
        self.assertTrue(all(isinstance(k, str) for k in result))
        self.assertTrue(all(isinstance(v, int) for v in result.values()))

    def test_unique_container_partial_result_when_values_exhaust(self):
        # bool has only two distinct values, so a set of bool cannot reach 3
        result = CollectionGenerator("set", Set[bool]).generate()
        self.assertLessEqual(len(result), 2)
        self.assertTrue(result.issubset({True, False}))

    def test_custom_size_is_respected(self):
        result = CollectionGenerator("list", List[int], size=5).generate()
        self.assertEqual(len(result), 5)

    def test_unknown_kind_raises(self):
        with self.assertRaises(ValueError):
            CollectionGenerator("bag", List[int]).generate()


if __name__ == "__main__":
    unittest.main()
