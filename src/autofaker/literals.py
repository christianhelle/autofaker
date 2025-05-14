import random
from typing import get_args, get_origin

from autofaker.base import TypeDataGeneratorBase


def is_literal_type(t):
    try:
        origin = get_origin(t)
        if origin is None:
            return False
        return str(origin) == "typing.Literal"
    except (AttributeError, TypeError):
        try:
            return t.__origin__._name == "Literal"
        except (AttributeError, TypeError):
            return False


class LiteralGenerator(TypeDataGeneratorBase):
    def __init__(self, t):
        try:
            self.allowed_values = get_args(t)
        except (AttributeError, TypeError):
            try:
                self.allowed_values = t.__args__
            except (AttributeError, TypeError):
                self.allowed_values = []

    def generate(self):
        if not self.allowed_values:
            return None
        return random.choice(self.allowed_values)
