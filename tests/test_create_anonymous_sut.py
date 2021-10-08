import unittest
from typing import List

from pyautodata import Autodata


class Person:
    age = 10
    name = 'test'

    def get_introduction(self):
        return f"Hi! My name is {self.name} and I'm {self.age} years old"


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

    def introduce(self):
        for person in self.people:
            print(person.get_introduction())


class StaffTests(unittest.TestCase):

    def test_introduce_everyone(self):
        people = Autodata.create_many(Person)
        sut = Autodata.create(Staff)
        sut.add_people(people)
        sut.introduce()
        self.assertEqual(len(people), sut.get_head_count())