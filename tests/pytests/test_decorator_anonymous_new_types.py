import datetime
import decimal
import pathlib
import uuid
from typing import Dict, FrozenSet, Optional, Set, Tuple

from autofaker import autodata, fakedata


# Anonymous New Builtin Types Via Decorator Tests


@autodata(tuple)
def test_create_tuple_using_decorator(t):
    assert t is not None
    assert isinstance(t, tuple)


@autodata(set)
def test_create_set_using_decorator(s):
    assert s is not None
    assert isinstance(s, set)


@autodata(frozenset)
def test_create_frozenset_using_decorator(fs):
    assert fs is not None
    assert isinstance(fs, frozenset)


@autodata(dict)
def test_create_dict_using_decorator(d):
    assert d is not None
    assert isinstance(d, dict)


@autodata(decimal.Decimal)
def test_create_decimal_using_decorator(d):
    assert d is not None
    assert isinstance(d, decimal.Decimal)


@autodata(uuid.UUID)
def test_create_uuid_using_decorator(u):
    assert u is not None
    assert isinstance(u, uuid.UUID)


@autodata(pathlib.Path)
def test_create_path_using_decorator(p):
    assert p is not None
    assert isinstance(p, pathlib.Path)


@autodata(datetime.time)
def test_create_time_using_decorator(t):
    assert t is not None
    assert isinstance(t, datetime.time)


@autodata(datetime.timedelta)
def test_create_timedelta_using_decorator(td):
    assert td is not None
    assert isinstance(td, datetime.timedelta)


# Anonymous New Builtin Types Via Decorator With Fakes


@autodata(tuple, use_fake_data=True)
def test_create_tuple_using_decorator_with_fakes(t):
    assert t is not None
    assert isinstance(t, tuple)


@autodata(set, use_fake_data=True)
def test_create_set_using_decorator_with_fakes(s):
    assert s is not None
    assert isinstance(s, set)


@autodata(frozenset, use_fake_data=True)
def test_create_frozenset_using_decorator_with_fakes(fs):
    assert fs is not None
    assert isinstance(fs, frozenset)


@autodata(dict, use_fake_data=True)
def test_create_dict_using_decorator_with_fakes(d):
    assert d is not None
    assert isinstance(d, dict)


@autodata(decimal.Decimal, use_fake_data=True)
def test_create_decimal_using_decorator_with_fakes(d):
    assert d is not None
    assert isinstance(d, decimal.Decimal)


@autodata(uuid.UUID, use_fake_data=True)
def test_create_uuid_using_decorator_with_fakes(u):
    assert u is not None
    assert isinstance(u, uuid.UUID)


@autodata(pathlib.Path, use_fake_data=True)
def test_create_path_using_decorator_with_fakes(p):
    assert p is not None
    assert isinstance(p, pathlib.Path)


@autodata(datetime.time, use_fake_data=True)
def test_create_time_using_decorator_with_fakes(t):
    assert t is not None
    assert isinstance(t, datetime.time)


@autodata(datetime.timedelta, use_fake_data=True)
def test_create_timedelta_using_decorator_with_fakes(td):
    assert td is not None
    assert isinstance(td, datetime.timedelta)


# Annotated Arguments Via Decorator With New Types


@autodata()
def test_create_annotated_tuple_using_decorator(t: tuple):
    assert t is not None
    assert isinstance(t, tuple)


@autodata()
def test_create_annotated_set_using_decorator(s: set):
    assert s is not None
    assert isinstance(s, set)


@autodata()
def test_create_annotated_frozenset_using_decorator(fs: frozenset):
    assert fs is not None
    assert isinstance(fs, frozenset)


@autodata()
def test_create_annotated_dict_using_decorator(d: dict):
    assert d is not None
    assert isinstance(d, dict)


@autodata()
def test_create_annotated_decimal_using_decorator(d: decimal.Decimal):
    assert d is not None
    assert isinstance(d, decimal.Decimal)


@autodata()
def test_create_annotated_uuid_using_decorator(u: uuid.UUID):
    assert u is not None
    assert isinstance(u, uuid.UUID)


@autodata()
def test_create_annotated_path_using_decorator(p: pathlib.Path):
    assert p is not None
    assert isinstance(p, pathlib.Path)


@autodata()
def test_create_annotated_time_using_decorator(t: datetime.time):
    assert t is not None
    assert isinstance(t, datetime.time)


@autodata()
def test_create_annotated_timedelta_using_decorator(td: datetime.timedelta):
    assert td is not None
    assert isinstance(td, datetime.timedelta)


# Multiple New Types Via Decorator


@autodata(
    tuple, set, frozenset, dict, decimal.Decimal, uuid.UUID,
    pathlib.Path, datetime.time, datetime.timedelta,
)
def test_create_all_new_types_using_decorator(
    t, s, fs, d, dec, uid, p, tm, td
):
    assert isinstance(t, tuple)
    assert isinstance(s, set)
    assert isinstance(fs, frozenset)
    assert isinstance(d, dict)
    assert isinstance(dec, decimal.Decimal)
    assert isinstance(uid, uuid.UUID)
    assert isinstance(p, pathlib.Path)
    assert isinstance(tm, datetime.time)
    assert isinstance(td, datetime.timedelta)


# Fakedata Decorator With Annotated Arguments


@fakedata()
def test_create_new_types_using_fakedata_decorator(
    t: tuple,
    s: set,
    d: dict,
    dec: decimal.Decimal,
    uid: uuid.UUID,
    p: pathlib.Path,
    tm: datetime.time,
    td: datetime.timedelta,
):
    assert isinstance(t, tuple)
    assert isinstance(s, set)
    assert isinstance(d, dict)
    assert isinstance(dec, decimal.Decimal)
    assert isinstance(uid, uuid.UUID)
    assert isinstance(p, pathlib.Path)
    assert isinstance(tm, datetime.time)
    assert isinstance(td, datetime.timedelta)
