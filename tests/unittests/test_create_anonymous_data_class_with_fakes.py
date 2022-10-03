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

    def test_create_dataclass_name_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).name))

    def test_create_dataclass_first_name_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).first_name))

    def test_create_dataclass_last_name_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).last_name))

    def test_create_dataclass_address_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).address))

    def test_create_dataclass_job_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).job))

    def test_create_dataclass_country_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).country))

    def test_create_dataclass_currency_name_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).currency_name))

    def test_create_dataclass_currency_code_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).currency_code))

    def test_create_dataclass_email_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).email))

    def test_create_dataclass_safe_email_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).safe_email))

    def test_create_dataclass_company_email_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).company_email))

    def test_create_dataclass_hostname_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).hostname))

    def test_create_dataclass_ipv4_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).ipv4))

    def test_create_dataclass_ipv6_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).ipv6))

    def test_create_dataclass_text_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).text))

    def test_create_dataclass_word_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create(DataClass, use_fake_data=True).word))
