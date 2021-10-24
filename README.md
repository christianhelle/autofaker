[![build](https://github.com/christianhelle/autofaker/actions/workflows/build-linux.yml/badge.svg)](https://github.com/christianhelle/autofaker/actions/workflows/build-linux.yml)
[![build](https://github.com/christianhelle/autofaker/actions/workflows/build-macos.yml/badge.svg)](https://github.com/christianhelle/autofaker/actions/workflows/build-macos.yml)
[![build](https://github.com/christianhelle/autofaker/actions/workflows/build-windows.yml/badge.svg)](https://github.com/christianhelle/autofaker/actions/workflows/build-windows.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=christianhelle_autofaker&metric=alert_status)](https://sonarcloud.io/dashboard?id=christianhelle_autofaker)
[![PyPI](https://img.shields.io/pypi/dm/autofaker)](https://pypi.org/project/autofaker)

# AutoFaker

A Python library designed to minimize the setup/arrange phase of your unit tests by removing the need to manually 
write code to create anonymous variables as part of a test cases setup/arrange phase. 

This library is heavily inspired by [AutoFixture](https://github.com/AutoFixture/AutoFixture) and was initially created 
for simplifying how to write unit tests for ETL (Extract-Transform-Load) code running from a python library on an 
Apache Spark cluster in Big Data solutions.

When writing unit tests you normally start with creating objects that represent the initial state of the test.
This phase is called the **arrange** or setup phase of the test.
In most cases, the system you want to test will force you to specify much more information than you really care about, 
so you frequently end up creating objects with no influence on the test itself just simply to satisfy the compiler/interpreter

AutoFaker can help by creating such anonymous variables for you. Here's a simple example:

```python
import unittest
from autofaker import Autodata

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

Since the point of this library is to simplify the **arrange** step of writing unit tests, we can use the
`@Autodata.create_arguments()` decorator to create anonymous variables and construct our system under test.
To use this you can either define the types or the arguments as function arguments to the decorator, or specify 
argument annotations

Alternative decorators like `@Autodata.create_anonmyous_arguments` and `@Autodata.create_fake_arguments` 
are available to explicitly state whether to use anonymous variables or fake data

```python
import unittest
from autofaker import Autodata

class Calculator:
  def add(self, number1: int, number2: int):
    return number1 + number2

class CalculatorTests(unittest.TestCase):
    @Autodata.create_arguments(Calculator, int, int)
    def test_can_add_two_numbers_using_test_arguments(self, sut, number1, number2):
        result = sut.add(number1, number2)
        self.assertEqual(number1 + number2, result)

    @Autodata.create_arguments()
    def test_can_add_two_numbers_using_annotated_arguments(self, 
                                                           sut: Calculator, 
                                                           number1: int, 
                                                           number2: int):
        result = sut.add(number1, number2)
        self.assertEqual(number1 + number2, result)
```

There are times when completely anonymous variables don't make much sense, especially in data centric scenarios. 
For these use cases this library uses [Faker](https://github.com/joke2k/faker) for generating fake data. This option 
is enabled by setting `use_fake_data` to `True` when calling the `Autodata.create()` function

```python
from dataclasses import dataclass
from autofaker import Autodata

@dataclass
class DataClass:
    id: int
    first_name: str
    last_name: str
    address: str
    job: str

data = Autodata.create(DataClass, use_fake_data=True)

print(f'id:     {data.id}')
print(f'name:   {data.name}')
print(f'job:    {data.job}\n')
```

The following code above might output something like:

```
id:     8952
name:   Justin Wise
job:    Chief Operating Officer
```

## Supported data types

Currently autofaker supports creating anonymous variables for the following data types:

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

[autofaker](https://pypi.org/project/autofaker/) is available from PyPI and should be installed using `pip`

```
pip install autofaker
```

Next you need to import the `Autodata` class

```python
from autofaker import Autodata
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

Creates an anonymous dataclass using fake data

```python
@dataclass
class DataClass:
    id: int

    name: str
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


data = Autodata.create(DataClass, use_fake_data=True)

print(f'id:               {data.id}')
print(f'name:             {data.name}')
print(f'job:              {data.job}\n')
print(f'address:\n{data.address}\n')

print(f'country:          {data.country}')
print(f'currency name:    {data.currency_name}')
print(f'currency code:    {data.currency_code}\n')

print(f'email:            {data.email}')
print(f'safe email:       {data.safe_email}')
print(f'work email:       {data.company_email}\n')

print(f'hostname:         {data.hostname}')
print(f'IPv4:             {data.ipv4}')
print(f'IPv6:             {data.ipv6}\n')

print(f'text:\n{data.text}')
```

The code above might output the following

```
id:               8952
name:             Justin Wise
job:              Chief Operating Officer

address:
65939 Hernandez Parks
Rochaport, NC 41760

country:          Equatorial Guinea
currency name:    Burmese kyat
currency code:    ERN

email:            smithjohn@example.com
safe email:       kent11@example.com
work email:       marissagreen@brown-cole.com

hostname:         db-90.hendricks-west.org
IPv4:             66.139.143.242
IPv6:             895d:82f7:7c13:e7cb:f35d:c93:aeb2:8eeb

text:
Movie author culture represent. Enjoy myself over physical green lead but home.
Share wind factor far minute produce significant. Sense might fact leader.
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

Create a Pandas DataFrame using fake data generated from a specified type

```python
class DataClass:
    id = 0
    type = '' 
    value = 0

pdf = Autodata.create_pandas_dataframe(DataClass, use_fake_data=True)
print(pdf)
```

The code above might output the following

```
  first_name    id last_name          phone_number
0   Lawrence  7670   Jimenez  001-172-307-0561x471
1      Bryan  9084    Walker         (697)893-6767
2       Paul  9824    Thomas    960.555.3577x65487
```

Create a Spark DataFrame using fake data generated from a specified type

```python
class DataClass:
    id = 0
    type = '' 
    value = 0

df = Autodata.create_spark_dataframe(DataClass, use_fake_data=True)
df.printSchema()
df.show()
```

The code above might output the following

```
root
 |-- id: long (nullable = true)
 |-- type: string (nullable = true)
 |-- value: long (nullable = true)

+----------+----+--------------------+---------+
|first_name|  id|                 job|last_name|
+----------+----+--------------------+---------+
|   Valerie|9010|Operational resea...|    Huber|
|     Linda|9367|               Actor|    Mills|
|    Sheena|4773|Civil Service adm...|    Perez|
+----------+----+--------------------+---------+
```
