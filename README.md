[![Build](https://github.com/christianhelle/pyautodata/workflows/build/badge.svg)](https://github.com/christianhelle/pyautodata/actions/workflows/build.yml)


# pyautodata
Python library designed to minimize the setup/arrange phase of your unit tests


```python
import unittest
from typing import List
from pyautodata import Fixture

class Person:
    age = 10
    name = 'test'
    
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
```
