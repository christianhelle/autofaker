import unittest
from dataclasses import dataclass
from typing import List

from autofaker import Autodata


@dataclass
class Person:
    age: int
    name: str


class Staff:
    def __init__(self, people: List[Person] = None):
        self.people = people if people is not None else []

    def add_person(self, person: Person):
        self.people.append(person)

    def add_people(self, people: List[Person]):
        for person in people:
            self.add_person(person)

    def get_head_count(self):
        return len(self.people)


class Organization:
    def __init__(self, staff: Staff):
        self.staff = staff

    def get_staff(self):
        return self.staff


class ConstructorWithPrimitiveArguments:
    def __init__(self, name: str, text: str, age: int):
        self.age = age
        self.text = text
        self.name = name


class ConstructorWithPrimitiveArgumentsTests(unittest.TestCase):
    def test_can_construct_sut(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithPrimitiveArguments))

    def test_constructed_sut_age_not_none(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithPrimitiveArguments).age)

    def test_constructed_sut_name_not_none(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithPrimitiveArguments).name)

    def test_constructed_sut_text_not_none(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithPrimitiveArguments).text)


class ConstructorWithClassArguments:
    def __init__(self, cls: ConstructorWithPrimitiveArguments):
        self.inner = cls


class ConstructorWithClassArgumentsTests(unittest.TestCase):
    def test_can_construct_sut(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithClassArguments))

    def test_constructed_sut_inner_not_none(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithClassArguments).inner)

    def test_constructed_sut_inner_has_correct_type(self):
        self.assertIsInstance(Autodata.create(ConstructorWithClassArguments).inner, ConstructorWithPrimitiveArguments)


class ConstructorWithNestedClassArguments:
    def __init__(self, cls: ConstructorWithClassArguments):
        self.inner = cls


class ConstructorWithNestedClassArgumentsTests(unittest.TestCase):
    def test_can_construct_sut(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithNestedClassArguments))

    def test_constructed_sut_inner_not_none(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithNestedClassArguments).inner)

    def test_constructed_sut_inner_has_correct_type(self):
        self.assertIsInstance(Autodata.create(ConstructorWithNestedClassArguments).inner, ConstructorWithClassArguments)

    def test_constructed_sut_inner_inner_has_correct_type(self):
        self.assertIsInstance(Autodata.create(ConstructorWithNestedClassArguments).inner.inner, ConstructorWithPrimitiveArguments)


class ConstructorWithDoubleNestedClassArguments:
    def __init__(self, cls: ConstructorWithNestedClassArguments):
        self.inner = cls


class ConstructorWithDoubleNestedClassArgumentsTests(unittest.TestCase):
    def test_can_construct_sut(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithDoubleNestedClassArguments))

    def test_constructed_sut_inner_not_none(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithDoubleNestedClassArguments).inner)

    def test_constructed_sut_inner_has_correct_type(self):
        self.assertIsInstance(Autodata.create(ConstructorWithDoubleNestedClassArguments).inner, ConstructorWithNestedClassArguments)

    def test_constructed_sut_inner_inner_has_correct_type(self):
        self.assertIsInstance(Autodata.create(ConstructorWithDoubleNestedClassArguments).inner.inner, ConstructorWithClassArguments)

    def test_constructed_sut_inner_inner_inner_has_correct_type(self):
        self.assertIsInstance(Autodata.create(ConstructorWithDoubleNestedClassArguments).inner.inner.inner, ConstructorWithPrimitiveArguments)


@dataclass
class DataClass:
    id: int
    name: str
    age: int
    email: str


class ConstructorWithDataClassArguments:
    def __init__(self, data: DataClass):
        self.data = data


class ConstructorWithDataClassArgumentsTests(unittest.TestCase):
    def test_can_construct_sut(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithDataClassArguments))

    def test_constructed_sut_id_not_none(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithDataClassArguments).data.id)

    def test_constructed_sut_age_not_none(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithDataClassArguments).data.age)

    def test_constructed_sut_name_not_none(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithDataClassArguments).data.name)

    def test_constructed_sut_email_not_none(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithDataClassArguments).data.email)


class ConstructorWithListArguments:
    def __init__(self, texts: List[str], numbers: List[int]):
        self.numbers = numbers
        self.texts = texts


class ConstructorWithListArgumentsTests(unittest.TestCase):
    def test_can_construct_sut(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithListArguments))


class ConstructorWithClassListArguments:
    def __init__(self, items: List[ConstructorWithPrimitiveArguments]):
        self.items = items


class ConstructorWithClassListArgumentsTests(unittest.TestCase):
    def test_can_construct_sut(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithClassListArguments))


class ConstructorWithDataClassListArguments:
    def __init__(self, items: List[DataClass]):
        self.items = items


class ConstructorWithDataClassListArgumentsTests(unittest.TestCase):
    def test_can_construct_sut(self):
        self.assertIsNotNone(Autodata.create(ConstructorWithDataClassListArguments))
