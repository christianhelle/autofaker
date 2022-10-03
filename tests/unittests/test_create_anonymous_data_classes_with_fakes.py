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

    def test_create_many_dataclass_name_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].name))

    def test_create_many_dataclass_first_name_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].first_name))

    def test_create_many_dataclass_last_name_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].last_name))

    def test_create_many_dataclass_address_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].address))

    def test_create_many_dataclass_job_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].job))

    def test_create_many_dataclass_country_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].country))

    def test_create_many_dataclass_currency_name_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].currency_name))

    def test_create_many_dataclass_currency_code_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].currency_code))

    def test_create_many_dataclass_email_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].email))

    def test_create_many_dataclass_safe_email_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].safe_email))

    def test_create_many_dataclass_company_email_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].company_email))

    def test_create_many_dataclass_hostname_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].hostname))

    def test_create_many_dataclass_ipv4_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].ipv4))

    def test_create_many_dataclass_ipv6_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].ipv6))

    def test_create_many_dataclass_text_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].text))

    def test_create_many_dataclass_word_returns_not_uuid(self):
        self.assertFalse(is_uuid(Autodata.create_many(DataClass, use_fake_data=True)[2].word))
