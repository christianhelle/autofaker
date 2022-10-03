from datetime import datetime, date

from autofaker import autodata, fakedata


# Anonymous Primitives Via Decorator Tests

@autodata(str)
def test_create_str_using_decorator(text):
    assert text is not None

@autodata(int)
def test_create_int_using_decorator(number):
    assert None != (number)

@autodata(float)
def test_create_float_using_decorator(number):
    assert None != (number)

@autodata(bool)
def test_create_boolean_using_decorator(boolean):
    assert None != (boolean)

@autodata(complex)
def test_create_complex_using_decorator(complex_type):
    assert None != (complex_type)

@autodata(range)
def test_create_range_using_decorator(r):
    assert None != (r)

@autodata(bytes)
def test_create_bytes_using_decorator(b):
    assert None != (b)

@autodata(bytearray)
def test_create_bytearray_using_decorator(b):
    assert None != (b)

@autodata(memoryview)
def test_create_memoryview_using_decorator(b):
    assert None != (b)

@autodata(datetime)
def test_create_datetime_using_decorator(dt):
    assert None != (dt)

@autodata(date)
def test_create_date_using_decorator(d):
    assert None != (d)


# Anonymous Primitives Via Decorator With Fakes

@autodata(str, use_fake_data=True)
def test_create_str_using_decorator(text):
    assert text is not None

@autodata(int, use_fake_data=True)
def test_create_int_using_decorator(number):
    assert None != (number)

@autodata(float, use_fake_data=True)
def test_create_float_using_decorator(number):
    assert None != (number)

@autodata(bool, use_fake_data=True)
def test_create_boolean_using_decorator(boolean):
    assert None != (boolean)

@autodata(complex, use_fake_data=True)
def test_create_complex_using_decorator(complex_type):
    assert None != (complex_type)

@autodata(range, use_fake_data=True)
def test_create_range_using_decorator(r):
    assert None != (r)

@autodata(bytes, use_fake_data=True)
def test_create_bytes_using_decorator(b):
    assert None != (b)

@autodata(bytearray, use_fake_data=True)
def test_create_bytearray_using_decorator(b):
    assert None != (b)

@autodata(memoryview, use_fake_data=True)
def test_create_memoryview_using_decorator(b):
    assert None != (b)

@autodata(datetime, use_fake_data=True)
def test_create_datetime_using_decorator(dt):
    assert None != (dt)

@autodata(date, use_fake_data=True)
def test_create_date_using_decorator(d):
