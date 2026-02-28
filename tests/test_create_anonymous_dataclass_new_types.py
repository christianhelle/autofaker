import datetime
import decimal
import pathlib
import unittest
import uuid
from dataclasses import dataclass
from typing import Dict, FrozenSet, Optional, Set, Tuple

from autofaker import Autodata


@dataclass
class DataClassWithNewBuiltins:
    id: int
    name: str
    amount: decimal.Decimal
    uid: uuid.UUID
    file_path: pathlib.Path


@dataclass
class DataClassWithDateTimeTypes:
    id: int
    created_at: datetime.datetime
    created_date: datetime.date
    created_time: datetime.time
    duration: datetime.timedelta


@dataclass
class DataClassWithTypingGenerics:
    id: int
    tags: Set[str]
    scores: Tuple[int, float, str]
    frozen_ids: FrozenSet[int]
    metadata: Dict[str, int]
    optional_name: Optional[str]
    optional_count: Optional[int]


@dataclass
class DataClassWithAllNewTypes:
    id: int
    name: str
    amount: decimal.Decimal
    uid: uuid.UUID
    file_path: pathlib.Path
    created_time: datetime.time
    duration: datetime.timedelta
    tags: Set[str]
    scores: Tuple[int, str]
    metadata: Dict[str, int]
    optional_name: Optional[str]


class AnonymousDataClassWithNewBuiltinsTestCase(unittest.TestCase):
    def test_create_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(DataClassWithNewBuiltins))

    def test_create_returns_correct_type(self):
        self.assertIsInstance(
            Autodata.create(DataClassWithNewBuiltins), DataClassWithNewBuiltins
        )

    def test_create_returns_decimal_field(self):
        result = Autodata.create(DataClassWithNewBuiltins)
        self.assertIsInstance(result.amount, decimal.Decimal)

    def test_create_returns_uuid_field(self):
        result = Autodata.create(DataClassWithNewBuiltins)
        self.assertIsInstance(result.uid, uuid.UUID)

    def test_create_returns_path_field(self):
        result = Autodata.create(DataClassWithNewBuiltins)
        self.assertIsInstance(result.file_path, pathlib.Path)

    def test_create_returns_unique_instances(self):
        result1 = Autodata.create(DataClassWithNewBuiltins)
        result2 = Autodata.create(DataClassWithNewBuiltins)
        self.assertNotEqual(result1.uid, result2.uid)


class AnonymousDataClassWithDateTimeTypesTestCase(unittest.TestCase):
    def test_create_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(DataClassWithDateTimeTypes))

    def test_create_returns_correct_type(self):
        self.assertIsInstance(
            Autodata.create(DataClassWithDateTimeTypes), DataClassWithDateTimeTypes
        )

    def test_create_returns_time_field(self):
        result = Autodata.create(DataClassWithDateTimeTypes)
        self.assertIsInstance(result.created_time, datetime.time)

    def test_create_returns_timedelta_field(self):
        result = Autodata.create(DataClassWithDateTimeTypes)
        self.assertIsInstance(result.duration, datetime.timedelta)

    def test_create_returns_datetime_field(self):
        result = Autodata.create(DataClassWithDateTimeTypes)
        self.assertIsInstance(result.created_at, datetime.datetime)

    def test_create_returns_date_field(self):
        result = Autodata.create(DataClassWithDateTimeTypes)
        self.assertIsInstance(result.created_date, datetime.date)


class AnonymousDataClassWithTypingGenericsTestCase(unittest.TestCase):
    def test_create_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(DataClassWithTypingGenerics))

    def test_create_returns_correct_type(self):
        self.assertIsInstance(
            Autodata.create(DataClassWithTypingGenerics), DataClassWithTypingGenerics
        )

    def test_create_returns_set_field(self):
        result = Autodata.create(DataClassWithTypingGenerics)
        self.assertIsInstance(result.tags, set)
        for item in result.tags:
            self.assertIsInstance(item, str)

    def test_create_returns_tuple_field(self):
        result = Autodata.create(DataClassWithTypingGenerics)
        self.assertIsInstance(result.scores, tuple)
        self.assertEqual(len(result.scores), 3)

    def test_create_returns_frozenset_field(self):
        result = Autodata.create(DataClassWithTypingGenerics)
        self.assertIsInstance(result.frozen_ids, frozenset)
        for item in result.frozen_ids:
            self.assertIsInstance(item, int)

    def test_create_returns_dict_field(self):
        result = Autodata.create(DataClassWithTypingGenerics)
        self.assertIsInstance(result.metadata, dict)

    def test_create_returns_optional_str_field(self):
        result = Autodata.create(DataClassWithTypingGenerics)
        self.assertIsInstance(result.optional_name, str)

    def test_create_returns_optional_int_field(self):
        result = Autodata.create(DataClassWithTypingGenerics)
        self.assertIsInstance(result.optional_count, int)


class AnonymousDataClassWithAllNewTypesTestCase(unittest.TestCase):
    def test_create_returns_not_none(self):
        self.assertIsNotNone(Autodata.create(DataClassWithAllNewTypes))

    def test_create_returns_correct_type(self):
        self.assertIsInstance(
            Autodata.create(DataClassWithAllNewTypes), DataClassWithAllNewTypes
        )

    def test_create_many_returns_list(self):
        results = Autodata.create_many(DataClassWithAllNewTypes)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 3)

    def test_create_many_returns_unique_instances(self):
        results = Autodata.create_many(DataClassWithAllNewTypes)
        uids = [r.uid for r in results]
        self.assertEqual(len(set(str(u) for u in uids)), 3)

    def test_create_with_fake_data_returns_not_none(self):
        self.assertIsNotNone(
            Autodata.create(DataClassWithAllNewTypes, use_fake_data=True)
        )
