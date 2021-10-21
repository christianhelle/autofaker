import sys
import unittest
from dataclasses import dataclass

from autofaker import Autodata


@dataclass
class DataClass:
    id: int

    name: str
    first_name: str
    last_name: str
    address: str
    job: str

    country: str
    currency_name: str
    currency_code: str

    email: str
    safe_email: str
    company_email: str

    hostname: str
    ipv4: str
    ipv6: str

    text: str
    word: str


def is_uuid(s: str):
    try:
        from uuid import UUID
        UUID(s)
        return True
    except ValueError:
        return False


class AnonymousDataClassWithFakesTestCase(unittest.TestCase):

    def test_create_pandas_dataframe_returns_not_none(self):
        pdf = Autodata.create_pandas_dataframe(DataClass, use_fake_data=True)
        print()
        print(pdf)
        self.assertIsNotNone(pdf)

    @unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
    def test_create_spark_dataframe_returns_not_none(self):
        df = Autodata.create_spark_dataframe(DataClass, use_fake_data=True)
        self.assertIsNotNone(df)
