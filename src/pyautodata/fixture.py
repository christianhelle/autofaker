import typing
from typing import List

from pyautodata.generator import TypeDataGenerator


class Fixture:
    @staticmethod
    def create(t):
        return TypeDataGenerator.create(t).generate()

    @staticmethod
    def create_many(t, size: int = 3) -> List[typing.Any]:
        items = []
        for i in range(size):
            items.append(Fixture.create(t))
        return items
