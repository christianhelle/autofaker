import unittest
from dataclasses import dataclass
from typing import List

from autofaker import Autodata, autodata, fakedata


class Calculator:
    def add(self, number1: int, number2: int):
        return number1 + number2


class CalculatorTests(unittest.TestCase):

    def test_can_add_two_numbers(self):
        numbers = Autodata.create_many(int, 2)
        sut = Autodata.create(Calculator)
        result = sut.add(numbers[0], numbers[1])
        self.assertEqual(numbers[0] + numbers[1], result)

    @autodata(Calculator, int, int)
    def test_can_add_two_numbers_using_test_arguments(self, sut, number1, number2):
        result = sut.add(number1, number2)
        self.assertEqual(number1 + number2, result)

    @autodata
    def test_can_add_two_numbers_using_annotated_arguments(self, sut: Calculator, number1: int, number2: int):
        result = sut.add(number1, number2)
        self.assertEqual(number1 + number2, result)

    @autodata
    def test_can_add_two_numbers_using_anonymous_arguments(self, sut: Calculator, number1: int, number2: int):
        result = sut.add(number1, number2)
        self.assertEqual(number1 + number2, result)

    @fakedata
    def test_can_add_two_numbers_using_fake_arguments(self, sut: Calculator, number1: int, number2: int):
        result = sut.add(number1, number2)
        self.assertEqual(number1 + number2, result)


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
