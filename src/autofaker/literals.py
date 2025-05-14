import random
from typing import get_args, get_origin, Literal

from autofaker.base import TypeDataGeneratorBase


def is_literal_type(t):
    origin = get_origin(t)
    if origin is None:
        return False
    return origin is Literal


class LiteralGenerator(TypeDataGeneratorBase):
    def __init__(self, t):
        if not is_literal_type(t):
            raise ValueError(f"Expected Literal type, got {t}")
        self.allowed_values = get_args(t)
        if not self.allowed_values:
            raise ValueError("Literal type must have at least one value")

    def generate(self):
        return random.choice(self.allowed_values)
