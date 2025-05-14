import unittest
from dataclasses import dataclass
from typing import Literal

from autofaker import Autodata

string_literal = Literal["pending", "approved", "rejected"]
number_literal = Literal[1, 2, 3]


class AnonymousStringLiteralTypeTestCase(unittest.TestCase):
    def test_create_literal_returns_not_none(self):
        data = Autodata.create(string_literal)
        self.assertIsNotNone(data)

    def test_create_literal_returns_valid_value(self):
        data = Autodata.create(string_literal)
        self.assertIn(data, ["pending", "approved", "rejected"])


class AnonymousNumberLiteralTypeTestCase(unittest.TestCase):
    def test_create_literal_returns_not_none(self):
        data = Autodata.create(number_literal)
        self.assertIsNotNone(data)

    def test_create_literal_returns_valid_value(self):
        data = Autodata.create(number_literal)
        self.assertIn(data, [1, 2, 3])


@dataclass
class DataClassWithLiteral:
    id: int
    status: string_literal
    number: number_literal


class AnonymousDataClassWithLiteralTypeTestCase(unittest.TestCase):
    def test_create_literal_returns_not_none(self):
        data = Autodata.create(DataClassWithLiteral)
        self.assertIsNotNone(data)

    def test_create_literal_returns_valid_value(self):
        data = Autodata.create(DataClassWithLiteral)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
        self.assertIn(data.number, [1, 2, 3])

    def test_create_literal_returns_fake_value(self):
        data = Autodata.create(DataClassWithLiteral, use_fake_data=True)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
        self.assertIn(data.number, [1, 2, 3])


class SimpleClassWithLiteral:
    id = -1
    text = "test"
    status: string_literal
    number: number_literal


class NestedClassWithLiteral:
    id = -1
    text = "test"
    status: string_literal
    number: number_literal
    inner = SimpleClassWithLiteral()


class DoubleNestedClassWithLiteral:
    id = -1
    text = "test"
    status: string_literal
    number: number_literal
    inner = NestedClassWithLiteral()


class AnonymousSimpleClassWithLiteralTestCase(unittest.TestCase):
    def test_create_simple_class_with_literal_returns_not_none(self):
        data = Autodata.create(SimpleClassWithLiteral)
        self.assertIsNotNone(data)

    def test_create_simple_class_with_literal_returns_instance(self):
        data = Autodata.create(SimpleClassWithLiteral)
        self.assertIsInstance(data, SimpleClassWithLiteral)

    def test_create_simple_class_with_literal_returns_valid_values(self):
        data = Autodata.create(SimpleClassWithLiteral)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
        self.assertIn(data.number, [1, 2, 3])

    def test_create_simple_class_with_literal_returns_non_default(self):
        data = Autodata.create(SimpleClassWithLiteral)
        default = SimpleClassWithLiteral()
        self.assertNotEqual(data.id, default.id)
        self.assertNotEqual(data.text, default.text)


class AnonymousNestedClassWithLiteralTestCase(unittest.TestCase):
    def test_create_nested_class_with_literal_returns_not_none(self):
        data = Autodata.create(NestedClassWithLiteral)
        self.assertIsNotNone(data)

    def test_create_nested_class_with_literal_returns_instance(self):
        data = Autodata.create(NestedClassWithLiteral)
        self.assertIsInstance(data, NestedClassWithLiteral)

    def test_create_nested_class_with_literal_returns_valid_values(self):
        data = Autodata.create(NestedClassWithLiteral)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
        self.assertIn(data.number, [1, 2, 3])
        self.assertIn(data.inner.status, ["pending", "approved", "rejected"])
        self.assertIn(data.inner.number, [1, 2, 3])

    def test_create_nested_class_with_literal_returns_non_default(self):
        data = Autodata.create(NestedClassWithLiteral)
        default = NestedClassWithLiteral()
        self.assertNotEqual(data.id, default.id)
        self.assertNotEqual(data.text, default.text)
        self.assertNotEqual(data.inner.id, default.inner.id)
        self.assertNotEqual(data.inner.text, default.inner.text)


class AnonymousDoubleNestedClassWithLiteralTestCase(unittest.TestCase):
    def test_create_double_nested_class_with_literal_returns_not_none(self):
        data = Autodata.create(DoubleNestedClassWithLiteral)
        self.assertIsNotNone(data)

    def test_create_double_nested_class_with_literal_returns_instance(self):
        data = Autodata.create(DoubleNestedClassWithLiteral)
        self.assertIsInstance(data, DoubleNestedClassWithLiteral)

    def test_create_double_nested_class_with_literal_returns_valid_values(self):
        data = Autodata.create(DoubleNestedClassWithLiteral)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
        self.assertIn(data.number, [1, 2, 3])
        self.assertIn(data.inner.status, ["pending", "approved", "rejected"])
        self.assertIn(data.inner.number, [1, 2, 3])
        self.assertIn(data.inner.inner.status, ["pending", "approved", "rejected"])
        self.assertIn(data.inner.inner.number, [1, 2, 3])

    def test_create_double_nested_class_with_literal_returns_non_default(self):
        data = Autodata.create(DoubleNestedClassWithLiteral)
        default = DoubleNestedClassWithLiteral()
        self.assertNotEqual(data.id, default.id)
        self.assertNotEqual(data.text, default.text)
        self.assertNotEqual(data.inner.id, default.inner.id)
        self.assertNotEqual(data.inner.text, default.inner.text)
        self.assertNotEqual(data.inner.inner.id, default.inner.inner.id)
        self.assertNotEqual(data.inner.inner.text, default.inner.inner.text)


class CreateManySimpleClassWithLiteralTestCase(unittest.TestCase):
    def test_create_many_simple_class_with_literal_returns_not_none(self):
        data = Autodata.create_many(SimpleClassWithLiteral)
        self.assertIsNotNone(data)

    def test_create_many_simple_class_with_literal_returns_list(self):
        data = Autodata.create_many(SimpleClassWithLiteral)
        self.assertIsInstance(data, list)

    def test_create_many_simple_class_with_literal_returns_valid_values(self):
        data = Autodata.create_many(SimpleClassWithLiteral)
        for item in data:
            self.assertIn(item.status, ["pending", "approved", "rejected"])
            self.assertIn(item.number, [1, 2, 3])

    def test_create_many_simple_class_with_literal_returns_non_default(self):
        data = Autodata.create_many(SimpleClassWithLiteral)
        default = SimpleClassWithLiteral()
        for item in data:
            self.assertNotEqual(item.id, default.id)
            self.assertNotEqual(item.text, default.text)


class CreateManyNestedClassWithLiteralTestCase(unittest.TestCase):
    def test_create_many_nested_class_with_literal_returns_not_none(self):
        data = Autodata.create_many(NestedClassWithLiteral)
        self.assertIsNotNone(data)

    def test_create_many_nested_class_with_literal_returns_list(self):
        data = Autodata.create_many(NestedClassWithLiteral)
        self.assertIsInstance(data, list)

    def test_create_many_nested_class_with_literal_returns_valid_values(self):
        data = Autodata.create_many(NestedClassWithLiteral)
        for item in data:
            self.assertIn(item.status, ["pending", "approved", "rejected"])
            self.assertIn(item.number, [1, 2, 3])
            self.assertIn(item.inner.status, ["pending", "approved", "rejected"])
            self.assertIn(item.inner.number, [1, 2, 3])

    def test_create_many_nested_class_with_literal_returns_non_default(self):
        data = Autodata.create_many(NestedClassWithLiteral)
        default = NestedClassWithLiteral()
        for item in data:
            self.assertNotEqual(item.id, default.id)
            self.assertNotEqual(item.text, default.text)
            self.assertNotEqual(item.inner.id, default.inner.id)
            self.assertNotEqual(item.inner.text, default.inner.text)


class CreateManyDoubleNestedClassWithLiteralTestCase(unittest.TestCase):
    def test_create_many_double_nested_class_with_literal_returns_not_none(self):
        data = Autodata.create_many(DoubleNestedClassWithLiteral)
        self.assertIsNotNone(data)

    def test_create_many_double_nested_class_with_literal_returns_list(self):
        data = Autodata.create_many(DoubleNestedClassWithLiteral)
        self.assertIsInstance(data, list)

    def test_create_many_double_nested_class_with_literal_returns_valid_values(self):
        data = Autodata.create_many(DoubleNestedClassWithLiteral)
        for item in data:
            self.assertIn(item.status, ["pending", "approved", "rejected"])
            self.assertIn(item.number, [1, 2, 3])
            self.assertIn(item.inner.status, ["pending", "approved", "rejected"])
            self.assertIn(item.inner.number, [1, 2, 3])
            self.assertIn(item.inner.inner.status, ["pending", "approved", "rejected"])
            self.assertIn(item.inner.inner.number, [1, 2, 3])

    def test_create_many_double_nested_class_with_literal_returns_non_default(self):
        data = Autodata.create_many(DoubleNestedClassWithLiteral)
        default = DoubleNestedClassWithLiteral()
        for item in data:
            self.assertNotEqual(item.id, default.id)
            self.assertNotEqual(item.text, default.text)
            self.assertNotEqual(item.inner.id, default.inner.id)
            self.assertNotEqual(item.inner.text, default.inner.text)
            self.assertNotEqual(item.inner.inner.id, default.inner.inner.id)
            self.assertNotEqual(item.inner.inner.text, default.inner.inner.text)


class CreateManyWithSizeTestCase(unittest.TestCase):
    def test_create_many_simple_class_with_literal_with_size(self):
        size = 5
        data = Autodata.create_many(SimpleClassWithLiteral, size)
        self.assertEqual(len(data), size)
        for item in data:
            self.assertIn(item.status, ["pending", "approved", "rejected"])
            self.assertIn(item.number, [1, 2, 3])

    def test_create_many_nested_class_with_literal_with_size(self):
        size = 3
        data = Autodata.create_many(NestedClassWithLiteral, size)
        self.assertEqual(len(data), size)
        for item in data:
            self.assertIn(item.status, ["pending", "approved", "rejected"])
            self.assertIn(item.number, [1, 2, 3])
            self.assertIn(item.inner.status, ["pending", "approved", "rejected"])
            self.assertIn(item.inner.number, [1, 2, 3])

    def test_create_many_double_nested_class_with_literal_with_size(self):
        size = 2
        data = Autodata.create_many(DoubleNestedClassWithLiteral, size)
        self.assertEqual(len(data), size)
        for item in data:
            self.assertIn(item.status, ["pending", "approved", "rejected"])
            self.assertIn(item.number, [1, 2, 3])
            self.assertIn(item.inner.status, ["pending", "approved", "rejected"])
            self.assertIn(item.inner.number, [1, 2, 3])
            self.assertIn(item.inner.inner.status, ["pending", "approved", "rejected"])
            self.assertIn(item.inner.inner.number, [1, 2, 3])


class FakeDataWithLiteralTestCase(unittest.TestCase):
    def test_create_simple_class_with_literal_with_fake_data(self):
        data = Autodata.create(SimpleClassWithLiteral, use_fake_data=True)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
        self.assertIn(data.number, [1, 2, 3])

    def test_create_nested_class_with_literal_with_fake_data(self):
        data = Autodata.create(NestedClassWithLiteral, use_fake_data=True)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
        self.assertIn(data.number, [1, 2, 3])
        self.assertIn(data.inner.status, ["pending", "approved", "rejected"])
        self.assertIn(data.inner.number, [1, 2, 3])

    def test_create_double_nested_class_with_literal_with_fake_data(self):
        data = Autodata.create(DoubleNestedClassWithLiteral, use_fake_data=True)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
        self.assertIn(data.number, [1, 2, 3])
        self.assertIn(data.inner.status, ["pending", "approved", "rejected"])
        self.assertIn(data.inner.number, [1, 2, 3])
        self.assertIn(data.inner.inner.status, ["pending", "approved", "rejected"])
        self.assertIn(data.inner.inner.number, [1, 2, 3])

    def test_create_many_with_literal_with_fake_data(self):
        size = 3
        data = Autodata.create_many(SimpleClassWithLiteral, size, use_fake_data=True)
        self.assertEqual(len(data), size)
        for item in data:
            self.assertIn(item.status, ["pending", "approved", "rejected"])
            self.assertIn(item.number, [1, 2, 3])

    def test_create_local_class_with_literal(self):
        class LocalWithLiteral:
            id = -1
            status: string_literal
            number: number_literal

        data = Autodata.create(LocalWithLiteral)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, LocalWithLiteral)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
        self.assertIn(data.number, [1, 2, 3])

    def test_create_local_nested_class_with_literal(self):
        class LocalInner:
            id = -1
            status: string_literal
            number: number_literal

        class LocalOuter:
            id = -1
            status: string_literal
            number: number_literal
            inner = LocalInner()

        data = Autodata.create(LocalOuter)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, LocalOuter)
        self.assertIn(data.status, ["pending", "approved", "rejected"])
        self.assertIn(data.number, [1, 2, 3])
        self.assertIn(data.inner.status, ["pending", "approved", "rejected"])
        self.assertIn(data.inner.number, [1, 2, 3])

    def test_create_many_local_class_with_literal(self):
        class LocalWithLiteral:
            id = -1
            status: string_literal
            number: number_literal

        size = 3
        data = Autodata.create_many(LocalWithLiteral, size)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), size)
        for item in data:
            self.assertIn(item.status, ["pending", "approved", "rejected"])
            self.assertIn(item.number, [1, 2, 3])
