import random
from enum import Enum

from autofaker.base import TypeDataGeneratorBase


def is_enum(t) -> bool:
    return isinstance(t, Enum.__class__)


class EnumGenerator(TypeDataGeneratorBase):
    def __init__(self, enum):
        self.enum = enum

    def generate(self):
        members = list(self.enum)
        if not members:
            raise ValueError("Cannot generate value from empty enum")
        return random.choice(members)
