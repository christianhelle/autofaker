import unittest

from autofaker import autodata, fakedata


class SimpleClass:
    id = -1
    name = 'name'
    text = 'test'


class AnonymousSimpleClassViaDecoratorTestCase(unittest.TestCase):

    @autodata(SimpleClass)
    def test_create_simple_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @autodata(SimpleClass)
    def test_create_simple_class_using_decorator_returns_instance(self, instance):
        self.assertIsInstance(instance, SimpleClass)

    @autodata(SimpleClass)
    def test_create_simple_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)

    @autodata()
    def test_create_simple_class_argument_returns_instance_with_new_values(self, instance: SimpleClass):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)

    @autodata()
    def test_create_anonymous_simple_class_returns_instance_with_new_values(self, instance: SimpleClass):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)

    @fakedata()
    def test_create_fake_simple_class_returns_instance_with_new_values(self, instance: SimpleClass):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)


class AnonymousSimpleClassViaDecoratorWithFakesTestCase(unittest.TestCase):

    @autodata(SimpleClass, use_fake_data=True)
    def test_create_simple_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @autodata(SimpleClass, use_fake_data=True)
    def test_create_simple_class_using_decorator_returns_instance(self, instance):
        self.assertIsInstance(instance, SimpleClass)

    @autodata(SimpleClass, use_fake_data=True)
    def test_create_simple_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.text, SimpleClass().text)

    @autodata(use_fake_data=True)
    def test_create_simple_class_argument_returns_instance_with_new_values(self, instance: SimpleClass):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)

    @fakedata()
    def test_create_fake_simple_class_returns_instance_with_new_values(self, instance: SimpleClass):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)
