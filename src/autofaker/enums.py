import random
from enum import Enum

from autofaker.base import TypeDataGeneratorBase


def is_enum(t) -> bool:
    return isinstance(t, Enum.__class__)


class EnumGenerator(TypeDataGeneratorBase):
    def __init__(self, enum):
        self.enum = enum

    def generate(self):
        return random.choice(list(self.enum))
