import unittest

import dataclasses
from dataclasses import dataclass

from autofaker import Autodata


@dataclass
class DataClass:
    id: int
    name: str
    text: str


class AnonymousDataClassViaDecoratorTestCase(unittest.TestCase):

    @Autodata.create_arguments(DataClass)
    def test_create_data_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @Autodata.create_arguments(DataClass)
    def test_create_data_class_using_decorator_returns_dataclass(self, instance):
        self.assertTrue(dataclasses.is_dataclass(instance))

    @Autodata.create_arguments(DataClass)
    def test_create_data_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, int())
        self.assertNotEqual(instance.name, str())
        self.assertNotEqual(instance.text, str())

    @Autodata.create_arguments()
    def test_create_data_class_argument_returns_instance_with_new_values(self, instance: DataClass):
        self.assertNotEqual(instance.id, int())
        self.assertNotEqual(instance.name, str())
        self.assertNotEqual(instance.text, str())

    @Autodata.create_anonymous_arguments
    def test_create_anonymous_data_class_returns_instance_with_new_values(self, instance: DataClass):
        self.assertNotEqual(instance.id, int())
        self.assertNotEqual(instance.name, str())
        self.assertNotEqual(instance.text, str())

    @Autodata.create_fake_arguments
    def test_create_fake_data_class_returns_instance_with_new_values(self, instance: DataClass):
        self.assertNotEqual(instance.id, int())
        self.assertNotEqual(instance.name, str())
        self.assertNotEqual(instance.text, str())


class AnonymousDataClassViaDecoratorWithFakesTestCase(unittest.TestCase):

    @Autodata.create_arguments(DataClass, use_fake_data=True)
    def test_create_data_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @Autodata.create_arguments(DataClass, use_fake_data=True)
    def test_create_data_class_using_decorator_returns_dataclass(self, instance):
        self.assertTrue(dataclasses.is_dataclass(instance))

    @Autodata.create_arguments(DataClass, use_fake_data=True)
    def test_create_data_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, int())
        self.assertNotEqual(instance.text, str())

    @Autodata.create_arguments(use_fake_data=True)
    def test_create_data_class_argument_returns_instance_with_new_values(self, instance: DataClass):
        self.assertNotEqual(instance.id, int())
        self.assertNotEqual(instance.name, str())
        self.assertNotEqual(instance.text, str())

    @Autodata.create_fake_arguments
    def test_create_fake_data_class_returns_instance_with_new_values(self, instance: DataClass):
        self.assertNotEqual(instance.id, int())
        self.assertNotEqual(instance.name, str())
        self.assertNotEqual(instance.text, str())
