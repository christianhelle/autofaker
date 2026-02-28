import datetime
import random

from autofaker.base import TypeDataGeneratorBase


def is_date_type(type_name) -> bool:
    return type_name in ["datetime", "date", "time", "timedelta"]


class DatetimeGenerator(TypeDataGeneratorBase):
    def generate(self):
        year = datetime.date.today().year
        return datetime.datetime(
            random.randint(year - 10, year + 10),
            random.randint(1, 12),
            random.randint(1, 28),
            random.randint(0, 23),
            random.randint(0, 59),
            random.randint(0, 59),
            random.randint(0, 999),
        )


class DateGenerator(TypeDataGeneratorBase):
    def generate(self):
        year = datetime.date.today().year
        return datetime.date(
            random.randint(year - 10, year + 10),
            random.randint(1, 12),
            random.randint(1, 28),
        )


class TimeGenerator(TypeDataGeneratorBase):
    def generate(self):
        return datetime.time(
            random.randint(0, 23),
            random.randint(0, 59),
            random.randint(0, 59),
            random.randint(0, 999999),
        )


class TimedeltaGenerator(TypeDataGeneratorBase):
    def generate(self):
        return datetime.timedelta(
            days=random.randint(0, 365),
            seconds=random.randint(0, 86399),
            microseconds=random.randint(0, 999999),
        )
