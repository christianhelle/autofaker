import unittest
from typing import List

from pyautodata import Fixture


class AutoSutTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sut: Person = Fixture.create(Person)

    def test_create_sut_call_function(self):
        self.sut.introduce()

    def test_get_age_returns_non_default_value(self):
        self.assertNotEqual(Person().get_age(), self.sut.get_age())

    def test_get_name_returns_non_default_value(self):
        self.assertNotEqual(Person().get_name(), self.sut.get_name())

    def test_create_sut_call_function_with_return(self):
        self.assertIsNotNone(self.sut.get_introduction())


class Person:
    age = 10
    name = 'test'

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_introduction(self):
        return f"Hi! My name is {self.name} and I'm {self.age} years old"

    def introduce(self):
        print(self.get_introduction())


class Staff:
    def __init__(self):
        self.people = []

    def add_person(self, person: Person):
        self.people.append(person)

    def add_people(self, people: List[Person]):
        for person in people:
            self.add_person(person)

    def get_head_count(self):
        return len(self.people)


class StaffTests(unittest.TestCase):

    def test_introduce_everyone(self):
        people = Fixture.create_many(Person)
        sut = Fixture.create(Staff)
        sut.add_people(people)
        self.assertEqual(len(people), sut.get_head_count())
