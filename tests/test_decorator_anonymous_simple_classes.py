import unittest

from autofaker import Autodata


class SimpleClass:
    id = 123
    name = 'name'
    text = 'test'


class AnonymousSimpleClassViaDecoratorTestCase(unittest.TestCase):

    @Autodata.create_arguments(SimpleClass)
    def test_create_simple_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @Autodata.create_arguments(SimpleClass)
    def test_create_simple_class_using_decorator_returns_instance(self, instance):
        self.assertIsInstance(instance, SimpleClass)

    @Autodata.create_arguments(SimpleClass)
    def test_create_simple_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)

    @Autodata.create_arguments()
    def test_create_simple_class_argument_returns_instance_with_new_values(self, instance: SimpleClass):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)

    @Autodata.create_anonymous_arguments
    def test_create_anonymous_simple_class_returns_instance_with_new_values(self, instance: SimpleClass):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)

    @Autodata.create_fake_arguments
    def test_create_fake_simple_class_returns_instance_with_new_values(self, instance: SimpleClass):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)


class AnonymousSimpleClassViaDecoratorWithFakesTestCase(unittest.TestCase):

    @Autodata.create_arguments(SimpleClass, use_fake_data=True)
    def test_create_simple_class_using_decorator_returns_not_none(self, instance):
        self.assertIsNotNone(instance)

    @Autodata.create_arguments(SimpleClass, use_fake_data=True)
    def test_create_simple_class_using_decorator_returns_instance(self, instance):
        self.assertIsInstance(instance, SimpleClass)

    @Autodata.create_arguments(SimpleClass, use_fake_data=True)
    def test_create_simple_class_returns_instance_with_new_values(self, instance):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.text, SimpleClass().text)

    @Autodata.create_arguments(use_fake_data=True)
    def test_create_simple_class_argument_returns_instance_with_new_values(self, instance: SimpleClass):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)

    @Autodata.create_fake_arguments
    def test_create_fake_simple_class_returns_instance_with_new_values(self, instance: SimpleClass):
        self.assertNotEqual(instance.id, SimpleClass().id)
        self.assertNotEqual(instance.name, SimpleClass().name)
        self.assertNotEqual(instance.text, SimpleClass().text)
