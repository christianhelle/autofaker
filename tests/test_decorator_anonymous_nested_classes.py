import unittest

from autofaker import Autodata


class SimpleClass:
    id = 123
    text = 'test'


class NestedClass:
    id = 123
    text = 'test'
    inner = SimpleClass()


class DoubleNestedClass:
    id = 123
    text = 'test'
    inner = NestedClass()


class AnonymousNestedClassViaDecoratorTestCase(unittest.TestCase):

    @Autodata.create_arguments(NestedClass)
    def test_create_nested_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @Autodata.create_arguments(NestedClass)
    def test_create_nested_class_using_decorator_returns_instance(self, instance):
        self.assertIsInstance(instance, NestedClass)

    @Autodata.create_arguments(NestedClass)
    def test_create_nested_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, NestedClass().id)
        self.assertNotEqual(instance.inner.id, SimpleClass().id)
        self.assertNotEqual(instance.inner.text, SimpleClass().text)


class AnonymousDoubleNestedClassViaDecoratorWithFakesTestCase(unittest.TestCase):

    @Autodata.create_arguments(DoubleNestedClass, use_fake_data=True)
    def test_create_double_nested_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @Autodata.create_arguments(DoubleNestedClass, use_fake_data=True)
    def test_create_double_nested_class_using_decorator_returns_instance(self, instance):
        self.assertIsInstance(instance, DoubleNestedClass)

    @Autodata.create_arguments(DoubleNestedClass, use_fake_data=True)
    def test_create_double_nested_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, DoubleNestedClass().id)
        self.assertNotEqual(instance.inner, DoubleNestedClass().inner)
        self.assertNotEqual(instance.inner.inner.id, SimpleClass().id)
        self.assertNotEqual(instance.inner.inner.text, SimpleClass().text)
