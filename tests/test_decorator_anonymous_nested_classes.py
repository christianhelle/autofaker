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

    @Autodata.create_argument(NestedClass)
    def test_create_nested_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @Autodata.create_argument(NestedClass)
    def test_create_nested_class_using_decorator_returns_instance(self, instance):
        self.assertIsInstance(instance, NestedClass)

    @Autodata.create_argument(NestedClass)
    def test_create_nested_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, NestedClass().id)
        self.assertNotEqual(instance.inner.id, SimpleClass().id)
        self.assertNotEqual(instance.inner.text, SimpleClass().text)


class AnonymousNestedClassViaDecoratorWithFakesTestCase(unittest.TestCase):

    @Autodata.create_argument(NestedClass, use_fake_data=True)
    def test_create_simple_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @Autodata.create_argument(NestedClass, use_fake_data=True)
    def test_create_simple_class_using_decorator_returns_instance(self, instance):
        self.assertIsInstance(instance, NestedClass)

    @Autodata.create_argument(NestedClass, use_fake_data=True)
    def test_create_simple_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, NestedClass().id)
        self.assertNotEqual(instance.inner.id, SimpleClass().id)
        self.assertNotEqual(instance.inner.text, SimpleClass().text)
