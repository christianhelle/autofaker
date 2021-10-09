[![build](https://github.com/christianhelle/pyautodata/actions/workflows/build.yml/badge.svg)](https://github.com/christianhelle/pyautodata/actions/workflows/build.yml)

# pyautodata
Python library designed to minimize the setup/arrange phase of your unit tests

```python
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

```

output for `Staff.introduce()` will be something like this:

```
Hi! My name is a88b64ac-69d8-4aef-8d8f-17fb6354654a and I'm 1090228300 years old
Hi! My name is bb424fad-14a4-4c79-9b9b-82a57dee59a4 and I'm 2059376420 years old
Hi! My name is 847ed9be-ab86-4637-b4f6-76a5b0a4e2f8 and I'm 987924894 years old
```
