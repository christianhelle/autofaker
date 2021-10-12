from faker import Faker

from autofaker.attributes import Attributes
from autofaker.base import TypeDataGeneratorBase
from autofaker.builtins import StringGenerator

faker = Faker()


def generate(field_name: str):
    try:
        attributes = Attributes(faker)
        func = attributes.get_attribute(field_name)
        return func()
    except AttributeError:
        return None


class FakeStringGenerator(TypeDataGeneratorBase):
    def __init__(self, field_name: str):
        self.field_name = field_name

    def generate(self):
        fake = generate(self.field_name)
        return fake if fake is not None else StringGenerator().generate()


class FakeIntegerGenerator(TypeDataGeneratorBase):
    def generate(self):
        return faker.random_int()

