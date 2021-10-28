import unittest

from autofaker import autodata, fakedata


class SimpleClass:
    id = -1
    name = 'name'
    text = 'test'


class NestedClass:
    id = -1
    name = 'name'
    text = 'test'
    inner = SimpleClass()


class DoubleNestedClass:
    id = -1
    name = 'name'
    text = 'test'
    inner = NestedClass()


class AnonymousNestedClassViaDecoratorTestCase(unittest.TestCase):

    @autodata(NestedClass)
    def test_create_nested_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @autodata(NestedClass)
    def test_create_nested_class_using_decorator_returns_instance(self, instance):
        self.assertIsInstance(instance, NestedClass)

    @autodata(NestedClass)
    def test_create_nested_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, NestedClass().id)
        self.assertNotEqual(instance.inner.id, SimpleClass().id)
        self.assertNotEqual(instance.inner.text, SimpleClass().text)

    @autodata()
    def test_create_nested_class_argument_returns_instance_with_new_values(self, instance: NestedClass):
        self.assertNotEqual(instance.id, NestedClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)

    @autodata()
    def test_create_anonymous_nested_class_returns_instance_with_new_values(self, instance: NestedClass):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)

    @fakedata()
    def test_create_fake_nested_class_returns_instance_with_new_values(self, instance: NestedClass):
        print(instance)
        self.assertNotEqual(instance.id, NestedClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)


class AnonymousDoubleNestedClassViaDecoratorWithFakesTestCase(unittest.TestCase):

    @autodata(DoubleNestedClass, use_fake_data=True)
    def test_create_double_nested_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @autodata(DoubleNestedClass, use_fake_data=True)
    def test_create_double_nested_class_using_decorator_returns_instance(self, instance):
        self.assertIsInstance(instance, DoubleNestedClass)

    @autodata(DoubleNestedClass, use_fake_data=True)
    def test_create_double_nested_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, DoubleNestedClass().id)
        self.assertNotEqual(instance.inner, DoubleNestedClass().inner)
        self.assertNotEqual(instance.inner.inner.id, SimpleClass().id)
        self.assertNotEqual(instance.inner.inner.text, SimpleClass().text)

    @autodata(use_fake_data=True)
    def test_create_double_nested_class_argument_using_decorator_returns_not_none(self, instance: DoubleNestedClass):
        self.assertIsNotNone(instance)

    @autodata(use_fake_data=True)
    def test_create_double_nested_class_argument_using_decorator_returns_instance(self, instance: DoubleNestedClass):
        self.assertIsInstance(instance, DoubleNestedClass)

    @fakedata()
    def test_create_double_nested_class_argument_returns_instance_with_new_values(self, instance: DoubleNestedClass):
        self.assertNotEqual(instance.id, DoubleNestedClass().id)
        self.assertNotEqual(instance.inner, DoubleNestedClass().inner)
        self.assertNotEqual(instance.inner.inner.id, SimpleClass().id)
        self.assertNotEqual(instance.inner.inner.text, SimpleClass().text)
