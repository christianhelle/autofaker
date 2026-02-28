import unittest
from typing import Dict, FrozenSet, Optional, Set, Tuple

from autofaker import Autodata


class AnonymousTypedTupleTestCase(unittest.TestCase):
    def test_create_typed_tuple_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(Tuple[int, str]))

    def test_create_typed_tuple_returns_tuple(self):
        self.assertIsInstance(Autodata.create(Tuple[int, str]), tuple)

    def test_create_typed_tuple_has_correct_length(self):
        result = Autodata.create(Tuple[int, str])
        self.assertEqual(len(result), 2)

    def test_create_typed_tuple_has_correct_types(self):
        result = Autodata.create(Tuple[int, str])
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], str)

    def test_create_typed_tuple_with_three_types(self):
        result = Autodata.create(Tuple[int, str, float])
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], str)
        self.assertIsInstance(result[2], float)

    def test_create_typed_tuple_with_single_type(self):
        result = Autodata.create(Tuple[int])
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], int)

    def test_create_typed_tuple_variable_length(self):
        result = Autodata.create(Tuple[int, ...])
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
        for item in result:
            self.assertIsInstance(item, int)

    def test_create_typed_tuple_variable_length_str(self):
        result = Autodata.create(Tuple[str, ...])
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
        for item in result:
            self.assertIsInstance(item, str)


class AnonymousTypedSetTestCase(unittest.TestCase):
    def test_create_typed_set_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(Set[int]))

    def test_create_typed_set_returns_set(self):
        self.assertIsInstance(Autodata.create(Set[int]), set)

    def test_create_typed_set_has_correct_element_types(self):
        result = Autodata.create(Set[int])
        for item in result:
            self.assertIsInstance(item, int)

    def test_create_typed_set_returns_non_empty(self):
        result = Autodata.create(Set[int])
        self.assertGreater(len(result), 0)

    def test_create_typed_set_of_strings(self):
        result = Autodata.create(Set[str])
        self.assertIsInstance(result, set)
        for item in result:
            self.assertIsInstance(item, str)

    def test_create_typed_set_of_bool_does_not_hang(self):
        result = Autodata.create(Set[bool])
        self.assertIsInstance(result, set)
        self.assertGreater(len(result), 0)
        self.assertLessEqual(len(result), 2)
        for item in result:
            self.assertIsInstance(item, bool)


class AnonymousTypedFrozenSetTestCase(unittest.TestCase):
    def test_create_typed_frozenset_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(FrozenSet[str]))

    def test_create_typed_frozenset_returns_frozenset(self):
        self.assertIsInstance(Autodata.create(FrozenSet[str]), frozenset)

    def test_create_typed_frozenset_has_correct_element_types(self):
        result = Autodata.create(FrozenSet[str])
        for item in result:
            self.assertIsInstance(item, str)

    def test_create_typed_frozenset_returns_non_empty(self):
        result = Autodata.create(FrozenSet[int])
        self.assertGreater(len(result), 0)

    def test_create_typed_frozenset_of_bool_does_not_hang(self):
        result = Autodata.create(FrozenSet[bool])
        self.assertIsInstance(result, frozenset)
        self.assertGreater(len(result), 0)
        self.assertLessEqual(len(result), 2)
        for item in result:
            self.assertIsInstance(item, bool)


class AnonymousTypedDictTestCase(unittest.TestCase):
    def test_create_typed_dict_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(Dict[str, int]))

    def test_create_typed_dict_returns_dict(self):
        self.assertIsInstance(Autodata.create(Dict[str, int]), dict)

    def test_create_typed_dict_has_correct_key_types(self):
        result = Autodata.create(Dict[str, int])
        for key in result.keys():
            self.assertIsInstance(key, str)

    def test_create_typed_dict_has_correct_value_types(self):
        result = Autodata.create(Dict[str, int])
        for value in result.values():
            self.assertIsInstance(value, int)

    def test_create_typed_dict_returns_non_empty(self):
        result = Autodata.create(Dict[str, int])
        self.assertGreater(len(result), 0)

    def test_create_typed_dict_with_int_keys(self):
        result = Autodata.create(Dict[int, str])
        for key in result.keys():
            self.assertIsInstance(key, int)
        for value in result.values():
            self.assertIsInstance(value, str)

    def test_create_typed_dict_with_bool_keys_does_not_hang(self):
        result = Autodata.create(Dict[bool, int])
        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)
        self.assertLessEqual(len(result), 2)
        for key in result.keys():
            self.assertIsInstance(key, bool)


class AnonymousOptionalTestCase(unittest.TestCase):
    def test_create_optional_int_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(Optional[int]))

    def test_create_optional_int_returns_int(self):
        self.assertIsInstance(Autodata.create(Optional[int]), int)

    def test_create_optional_str_returns_str(self):
        self.assertIsInstance(Autodata.create(Optional[str]), str)

    def test_create_optional_float_returns_float(self):
        self.assertIsInstance(Autodata.create(Optional[float]), float)

    def test_create_optional_bool_returns_bool(self):
        self.assertIsInstance(Autodata.create(Optional[bool]), bool)
