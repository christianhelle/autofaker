[![build](https://github.com/christianhelle/pyautodata/actions/workflows/build.yml/badge.svg)](https://github.com/christianhelle/pyautodata/actions/workflows/build.yml)

# PyAutodata
A Python library designed to minimize the setup/arrange phase of your unit tests by removing the need to manually 
write code to create anonymous variables as part of a test cases setup/arrange phase.

When writing unit tests, you normally start with creating objects that represent the initial state of the test.
This phase is called the **arrange** or setup phase of the test.
In most cases, the system you want to test will force you to specify much more information than you really care about, 
so you frequently end up creating objects with no influence on the test itself, simply to satisfy the compiler/interpreter.

PyAutodata can help by creating such anonymous variables for you. Here's a simple example:

```python
import unittest
from pyautodata import Autodata

class Calculator:
  def add(self, number1: int, number2: int):
    return number1 + number2

class CalculatorTests(unittest.TestCase):

    def test_can_add_two_numbers(self):      
        # arrange
        numbers = Autodata.create_many(int, 2)
        sut = Autodata.create(Calculator)
        
        # act
        result = sut.add(numbers[0], numbers[1])
        
        # assert
        self.assertEqual(numbers[0] + numbers[1], result)
```

## Supported data types

Currently PyAutodata supports creating anonymous variables for the following data types:

Built-in types:
- int
- float
- str

Datetime types:
- datetime
- date

Classes:
- Simple classes
- @dataclass
- Nested classes (and recursion)
- Classes containing lists of other types

Dataframes:
- Pandas dataframe
- Spark dataframe


## Getting Started

[PyAutodata](https://pypi.org/project/pyautodata/) is available from PyPI and should be installed using `pip`

```
pip install pyautodata
```

Next you need to import the `Autodata` class

```python
from pyautodata import Autodata
```

Create anonymous built-in types like `int`, `float`, `str` and datetime types like `datetime` and `date`

```python
print(f'anonymous string:    {Autodata.create(str)}')
print(f'anonymous int:       {Autodata.create(int)}')
print(f'anonymous float:     {Autodata.create(float)}')
print(f'anonymous datetime:  {Autodata.create(datetime)}')
print(f'anonymous date:      {Autodata.create(datetime.date)}')
```

The code above might output the following

```
anonymous string:    f91954f1-96df-463f-a427-665c99213395
anonymous int:       2066712686
anonymous float:     725758222.8712853
anonymous datetime:  2017-06-19 02:40:41.000084
anonymous date:      2019-11-10 00:00:00
```

Ceate collections containing anonymous variables of built-in types and dates

```python
print(f'anonymous strings:    {Autodata.create_many(str)}')
print(f'anonymous ints:       {Autodata.create_many(int, 10)}')
print(f'anonymous floats:     {Autodata.create_many(float, 5)}')
print(f'anonymous datetime:   {Autodata.create_many(datetime)}')
print(f'anonymous date:       {Autodata.create_many(datetime.date)}')
```

The code above might output the following

```
anonymous strings:    ['f7ebaf30-468b-4282-9189-1c9f5a98c6e4', '6736ccdd-fb06-4fd0-89d7-0979a8493d79', 'f15736eb-2860-4f42-91c1-e48c8d25ea24']
anonymous ints:       [706865421, 1670005830, 1966806327, 434303989, 454137879, 1940686334, 307384148, 1090980019, 936257994, 9154693]
anonymous floats:     [684196408.4474499, 1188750352.5678303, 963320036.0875875, 1702383000.8534415, 1865911801.1348956]
anonymous datetime:   [datetime.datetime(2028, 12, 2, 13, 0, 52, 140), datetime.datetime(2021, 9, 7, 22, 39, 58, 919), datetime.datetime(2027, 12, 25, 13, 15, 28, 694)]
anonymous date:       [datetime.datetime(2019, 3, 3, 0, 0), datetime.datetime(2026, 4, 13, 0, 0), datetime.datetime(2016, 2, 24, 0, 0)]
```

Creates an anonymous class

```python

class SimpleClass:
    id = 123
    text = 'test'

cls = Autodata.create(SimpleClass)
print(f'id = {cls.id}')
print(f'text = {cls.text}')
```

The code above might output the following

```
id = 2020177162
text = ac54a65d-b4a3-4eda-a840-eb948ad10d5f
```

Create a collection of an anonymous class

```python
class SimpleClass:
    id = 123
    text = 'test'

classes = Autodata.create_many(SimpleClass)
for cls in classes:
  print(f'id = {cls.id}')
  print(f'text = {cls.text}')
  print()
```

The code above might output the following

```
id = 242996515
text = 5bb60504-ccca-4104-9b7f-b978e52a6518

id = 836984239
text = 079df61e-a87e-4f26-8196-3f44157aabd6

id = 570703150
text = a3b86f08-c73a-4730-bde7-4bdff5360ef4
```

Creates an anonymous dataclass

```python
from dataclasses import dataclass

@dataclass
class DataClass:
    id: int
    text: str

cls = Autodata.create(DataClass)
print(f'id = {cls.id}')
print(f'text = {cls.text}')
```

The code above might output the following

```
id = 314075507
text = 4a3b3cae-f4cf-4502-a7f3-61115a1e0d2a
```

Create an anonymous class with nested types

```python

class NestedClass:
    id = 123
    text = 'test'
    inner = SimpleClass()

cls = Autodata.create(NestedClass)
print(f'id = {cls.id}')
print(f'text = {cls.text}')
print(f'inner.id = {cls.inner.id}')
print(f'inner.text = {cls.inner.text}')
```

The code above might output the following

```
id = 1565737216
text = e66ecd5c-c17a-4426-b755-36dfd2082672
inner.id = 390282329
inner.text = eef94b5c-aa95-427a-a9e6-d99e2cc1ffb2
```

Create a collection of an anonymous class with nested types

```python
class NestedClass:
    id = 123
    text = 'test'
    inner = SimpleClass()

classes = Autodata.create_many(NestedClass)
for cls in classes:
  print(f'id = {cls.id}')
  print(f'text = {cls.text}')
  print(f'inner.id = {cls.inner.id}')
  print(f'inner.text = {cls.inner.text}')
  print()
```

The code above might output the following

```
id = 1116454042
text = ceeecf0c-7375-4f3a-8d4b-6d7a4f2b20fd
inner.id = 1067027444
inner.text = 079573ce-1ef4-408d-8984-1dbc7b0d0b80

id = 730390288
text = ff3ca474-a69d-4ff6-95b4-fbdb1bea7cdb
inner.id = 1632771208
inner.text = 9423e824-dc8f-4145-ba47-7301351a91f8

id = 187364960
text = b31ca191-5031-43a2-870a-7bc7c99e4110
inner.id = 1705149100
inner.text = e703a117-ba4f-4201-a31b-10ab8e54a673
```

Create a Pandas DataFrame using anonymous data generated from a specified type

```python
class DataClass:
    id = 0
    type = '' 
    value = 0

pdf = Autodata.create_pandas_dataframe(DataClass)
print(pdf)
```

The code above might output the following

```
          id                                  type       value
0  778090854  13537c5a-62e7-488b-836e-a4b17f2f3ae9  1049015695
1  602015506  c043ca8d-e280-466a-8bba-ec1e0539fe28  1016359353
2  387753717  986b3b1c-abf4-4bc1-95cf-0e979390e4f3   766159839
```

Create a Spark DataFrame using anonymous data generated from a specified type

```python
class DataClass:
    id = 0
    type = '' 
    value = 0

df = Autodata.create_spark_dataframe(DataClass)
df.printSchema()
df.show()
```

The code above might output the following

```
root
 |-- id: long (nullable = true)
 |-- type: string (nullable = true)
 |-- value: long (nullable = true)

+----------+--------------------+----------+
|        id|                type|     value|
+----------+--------------------+----------+
| 938634666|630040b1-0703-437...|1417827879|
| 239684437|69ca65d5-81a6-418...|1932787106|
|1978525110|dfdc19df-ba47-43d...| 366058214|
+----------+--------------------+----------+
```
