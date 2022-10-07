from datetime import datetime, date

from autofaker import autodata, fakedata


# Anonymous Primitives Via Decorator Tests

@autodata(str)
def test_create_str_using_decorator(text):
    assert text is not None


@autodata(int)
def test_create_int_using_decorator(number):
    assert None is not number


@autodata(float)
def test_create_float_using_decorator(number):
    assert None is not number


@autodata(bool)
def test_create_boolean_using_decorator(boolean):
    assert None is not boolean


@autodata(complex)
def test_create_complex_using_decorator(complex_type):
    assert None is not complex_type


@autodata(range)
def test_create_range_using_decorator(r):
    assert None is not r


@autodata(bytes)
def test_create_bytes_using_decorator(b):
    assert None is not b


@autodata(bytearray)
def test_create_bytearray_using_decorator(b):
    assert None is not b


@autodata(memoryview)
def test_create_memoryview_using_decorator(b):
    assert None is not b


@autodata(datetime)
def test_create_datetime_using_decorator(dt):
    assert None is not dt


@autodata(date)
def test_create_date_using_decorator(d):
    assert None is not d


# Anonymous Primitives Via Decorator With Fakes

@autodata(str, use_fake_data=True)
def test_create_str_using_decorator_with_fake_data(text):
    assert text is not None


@autodata(int, use_fake_data=True)
def test_create_int_using_decorator_with_fake_data(number):
    assert None is not number


@autodata(float, use_fake_data=True)
def test_create_float_using_decorator_with_fake_data(number):
    assert None is not number


@autodata(bool, use_fake_data=True)
def test_create_boolean_using_decorator_with_fake_data(boolean):
    assert None is not boolean


@autodata(complex, use_fake_data=True)
def test_create_complex_using_decorator_with_fake_data(complex_type):
    assert None is not complex_type


@autodata(range, use_fake_data=True)
def test_create_range_using_decorator_with_fake_data(r):
    assert None is not r


@autodata(bytes, use_fake_data=True)
def test_create_bytes_using_decorator_with_fake_data(b):
    assert None is not b


@autodata(bytearray, use_fake_data=True)
def test_create_bytearray_using_decorator_with_fake_data(b):
    assert None is not b


@autodata(memoryview, use_fake_data=True)
def test_create_memoryview_using_decorator_with_fake_data(b):
    assert None is not b


@autodata(datetime, use_fake_data=True)
def test_create_datetime_using_decorator_with_fake_data(dt):
    assert None is not dt


@autodata(date, use_fake_data=True)
def test_create_date_using_decorator_with_fake_data(d):
    assert None is not d


# Multiple Anonymous Primitives Via Decorator Tests

@autodata(str, int, float, complex, range, bytes, bytearray, memoryview)
def test_create_primitives_using_decorator(text, number, decimal, complex_type, range_type, buffer, buffer2, memview):
    assert text is not None
    assert number != 0
    assert decimal != float()
    assert complex_type != complex()
    assert range_type != range(0)
    assert buffer != bytes()
    assert buffer2 != bytearray()
    assert memview != memoryview(bytes())


@autodata(str, int, float, complex, range, bytes, bytearray, memoryview, use_fake_data=True)
def test_create_primitives_using_decorator_with_fakes(text, number, decimal, complex_type, range_type, buffer, buffer2, memview):
    assert text is not None
    assert number != 0
    assert decimal != float()
    assert complex_type != complex()
    assert range_type != range(0)
    assert buffer != bytes()
    assert buffer2 != bytearray()
    assert memview != memoryview(bytes())


# Multiple Arguments Via Decorator Tests

@fakedata()
def test_create_anonymous_arguments_using_decorator(text: str,
                                                    number: int,
                                                    decimal: float,
                                                    complex_type: complex,
                                                    range_type: range,
                                                    buffer: bytes,
                                                    buffer2: bytearray,
                                                    memview: memoryview):
    print(text)
    print(number)
    print(decimal)
    print(complex_type)
    assert text is not None
    assert number != 0
    assert decimal != float()
    assert complex_type != complex()
    assert range_type != range(0)
    assert buffer != bytes()
    assert buffer2 != bytearray()
    assert memview != memoryview(bytes())


@fakedata()
def test_create_fake_arguments_using_decorator(text: str,
                                               number: int,
                                               decimal: float,
                                               complex_type: complex,
                                               range_type: range,
                                               buffer: bytes,
                                               buffer2: bytearray,
                                               memview: memoryview):
    print(text)
    print(number)
    print(decimal)
    print(complex_type)
    assert text is not None
    assert number != 0
    assert decimal != float()
    assert complex_type != complex()
    assert range_type != range(0)
    assert buffer != bytes()
    assert buffer2 != bytearray()
    assert memview != memoryview(bytes())


@autodata()
def test_create_arguments_using_decorator(text: str,
                                          number: int,
                                          decimal: float,
                                          complex_type: complex,
                                          range_type: range,
                                          buffer: bytes,
                                          buffer2: bytearray,
                                          memview: memoryview):
    print(text)
    print(number)
    print(decimal)
    print(complex_type)
    assert text is not None
    assert number != 0
    assert decimal != float()
    assert complex_type != complex()
    assert range_type != range(0)
    assert buffer != bytes()
    assert buffer2 != bytearray()
    assert memview != memoryview(bytes())


@autodata(use_fake_data=True)
def test_create_arguments_using_decorator_with_fakes(text: str,
                                                     number: int,
                                                     decimal: float,
                                                     complex_type: complex,
                                                     range_type: range,
                                                     buffer: bytes,
                                                     buffer2: bytearray,
                                                     memview: memoryview):
    print(text)
    print(number)
    print(decimal)
    print(complex_type)
    assert text is not None
    assert number != 0
    assert decimal != float()
    assert complex_type != complex()
    assert range_type != range(0)
    assert buffer != bytes()
    assert buffer2 != bytearray()
    assert memview != memoryview(bytes())
