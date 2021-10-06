import unittest

from pyautodata import Fixture


class AutoSutTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sut: Person = Fixture.create(Person)

    def test_create_sut_call_function(self):
        self.sut.introduce()

    def test_create_sut_call_function_with_return(self):
        self.assertIsNotNone(self.sut.get_introduction())


class Person:
    age = 10
    name = 'test'

    def get_introduction(self):
        return f"Hi! My name is {self.name} and I'm {self.age} years old"

    def introduce(self):
        print(self.get_introduction())
