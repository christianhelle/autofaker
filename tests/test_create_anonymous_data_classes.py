import dataclasses
import unittest
from dataclasses import dataclass

from autofaker import Autodata


@dataclass
class DataClass:
    id: int
    text: str


class AnonymousDataClassTestCase(unittest.TestCase):

    def test_create_data_class_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(DataClass))

    def test_create_data_class_returns_dataclass(self):
        self.assertTrue(dataclasses.is_dataclass(Autodata.create(DataClass)))

    def test_create_many_data_class_returns_not_none(self):
        self.assertIsNotNone(Autodata.create_many(DataClass))

    def test_create_many_data_class_returns_list(self):
        self.assertIsInstance(Autodata.create_many(DataClass), list)

    def test_create_many_data_class_returns_dataclass(self):
        data = Autodata.create(DataClass)
        self.assertNotEqual(0, data.id)
        self.assertNotEqual('', data.text)


@dataclass
class NestedDataClass:
    id: int
    text: str
    inner: DataClass


class AnonymousNestedClassTestCase(unittest.TestCase):

    def test_create_nested_class_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(NestedDataClass))

    def test_create_data_class_returns_dataclass(self):
        self.assertTrue(dataclasses.is_dataclass(Autodata.create(NestedDataClass)))

    def test_create_nested_class_returns_instance_with_nested_not_none(self):
        self.assertIsNotNone(Autodata.create(NestedDataClass).inner)

    def test_create_nested_class_returns_instance_with_new_nested_instance(self):
        result = Autodata.create(NestedDataClass)
        self.assertNotEqual(result.id, 0)
        self.assertNotEqual(result.inner.id, 0)
        self.assertNotEqual(result.inner.text, '')


@dataclass
class DoubleNestedDataClass:
    id: int
    text: str
    inner: NestedDataClass


class AnonymousDoubleNestedDataClassTestCase(unittest.TestCase):

    def test_create_nested_class_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(DoubleNestedDataClass))

    def test_create_data_class_returns_dataclass(self):
        self.assertTrue(dataclasses.is_dataclass(Autodata.create(DoubleNestedDataClass)))

    def test_create_nested_class_returns_instance_with_nested_not_none(self):
        self.assertIsNotNone(Autodata.create(DoubleNestedDataClass).inner)

    def test_create_nested_class_returns_instance_with_new_nested_instance(self):
        result = Autodata.create(DoubleNestedDataClass)
        self.assertNotEqual(result.id, 0)
        self.assertNotEqual(result.inner.id, 0)
        self.assertNotEqual(result.inner.text, '')
        self.assertNotEqual(result.inner.inner.id, 0)
        self.assertNotEqual(result.inner.inner.text, '')


class AnonymousInlineDataClassTestCase(unittest.TestCase):

    def test_create_data_class_returns_not_none(self):
        @dataclass
        class InlineDataClass:
            id: int
            text: str
        self.assertIsNotNone(Autodata.create(InlineDataClass))

    def test_create_data_class_returns_dataclass(self):
        @dataclass
        class InlineDataClass:
            id: int
            text: str
        self.assertTrue(dataclasses.is_dataclass(Autodata.create(InlineDataClass)))

    def test_create_many_data_class_returns_not_none(self):
        @dataclass
        class InlineDataClass:
            id: int
            text: str
        self.assertIsNotNone(Autodata.create_many(InlineDataClass))

    def test_create_many_data_class_returns_list(self):
        @dataclass
        class InlineDataClass:
            id: int
            text: str
        self.assertIsInstance(Autodata.create_many(InlineDataClass), list)

    def test_create_many_data_class_returns_dataclass(self):
        @dataclass
        class InlineDataClass:
            id: int
            text: str
        data = Autodata.create(InlineDataClass)
        self.assertNotEqual(0, data.id)
        self.assertNotEqual('', data.text)
