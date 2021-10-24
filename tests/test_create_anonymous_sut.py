import unittest
from typing import List

from autofaker import Autodata


class Calculator:
  def add(self, number1: int, number2: int):
    return number1 + number2


class CalculatorTests(unittest.TestCase):

    def test_can_add_two_numbers(self):
        numbers = Autodata.create_many(int, 2)
        sut = Autodata.create(Calculator)
        result = sut.add(numbers[0], numbers[1])
        self.assertEqual(numbers[0] + numbers[1], result)

    @Autodata.create_arguments(Calculator, int, int)
    def test_can_add_two_numbers_using_test_arguments(self, sut, number1, number2):
        result = sut.add(number1, number2)
        self.assertEqual(number1 + number2, result)

    @Autodata.create_arguments()
    def test_can_add_two_numbers_using_annotated_arguments(self, sut: Calculator, number1: int, number2: int):
        result = sut.add(number1, number2)
        self.assertEqual(number1 + number2, result)

    @Autodata.create_anonymous_arguments
    def test_can_add_two_numbers_using_anonymous_arguments(self, sut: Calculator, number1: int, number2: int):
        result = sut.add(number1, number2)
        self.assertEqual(number1 + number2, result)

    @Autodata.create_fake_arguments
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
