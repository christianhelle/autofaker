import unittest

from pyautodata import Fixture


class AnonymousClassesTestCase(unittest.TestCase):

    def test_create_local_class_returns_not_none(self):
        class X:
            pass
        self.assertIsNotNone(Fixture.create(X))

    def test_create_local_class_returns_instance(self):
        class X:
            pass
        self.assertIsInstance(Fixture.create(X), X)

    def test_create_module_class_returns_not_none(self):
        self.assertIsNotNone(Fixture.create(TestClass))

    def test_create_module_class_returns_instance(self):
        self.assertIsInstance(Fixture.create(TestClass), TestClass)

    def test_create_module_class_returns_instance_with_new_values(self):
        result = Fixture.create(TestClass)
        self.assertNotEqual(result.id, TestClass().id)
        self.assertNotEqual(result.text, TestClass().text)
        print(f'id: {result.id}')
        print('text: ' + result.text)


class TestClass:
    id = 123
    text = 'test'
