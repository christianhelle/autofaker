import random
from typing import get_args, get_origin

from autofaker.base import TypeDataGeneratorBase


def is_literal_type(t):
    origin = get_origin(t)
    if origin is None:
        return False
    return str(origin) == "typing.Literal"


class LiteralGenerator(TypeDataGeneratorBase):
    def __init__(self, t):
        self.allowed_values = get_args(t)

    def generate(self):
        return random.choice(self.allowed_values)
