import datetime
import random

from autofaker.base import TypeDataGeneratorBase


def is_date_type(type_name) -> bool:
    return type_name in [
        'datetime',
        'date'
    ]


class DatetimeGenerator(TypeDataGeneratorBase):
    def generate(self):
        year = datetime.date.today().year
        return datetime.datetime(random.randint(year - 10, year + 10),
                                 random.randint(1, 12),
                                 random.randint(1, 28),
                                 random.randint(0, 23),
                                 random.randint(0, 59),
                                 random.randint(0, 59),
                                 random.randint(0, 999))


class DateGenerator(TypeDataGeneratorBase):
    def generate(self):
        year = datetime.date.today().year
        return datetime.datetime(random.randint(year - 10, year + 10),
                                 random.randint(1, 12),
                                 random.randint(1, 28))
