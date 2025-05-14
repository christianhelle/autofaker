from dataclasses import dataclass
from typing import Literal, get_origin, get_args
import typing_inspect

from autofaker.generator import TypeDataGenerator

MyLiteral = Literal['a', 'b']

@dataclass
class DataClassWithLiteral:
    id: int
    status: MyLiteral

# Inspect the type annotation
print(f"Type: {MyLiteral}")
print(f"Type type: {type(MyLiteral)}")
print(f"Origin: {get_origin(MyLiteral)}")
print(f"Args: {get_args(MyLiteral)}")
print(f"typing_inspect origin: {typing_inspect.get_origin(MyLiteral)}")
print(f"typing_inspect args: {typing_inspect.get_args(MyLiteral)}")

# Try the autofaker type name method
try:
    type_name = TypeDataGenerator._get_type_name(MyLiteral)
    print(f"TypeDataGenerator._get_type_name: {type_name}")
except Exception as e:
    print(f"TypeDataGenerator._get_type_name error: {e}")
print()

# Get dataclass field types
for field in DataClassWithLiteral.__dataclass_fields__.values():
    print(f"Field name: {field.name}")
    print(f"Field type: {field.type}")
    print(f"Field type type: {type(field.type)}")
    if field.name == 'status':
        print(f"Field type origin: {get_origin(field.type)}")
        print(f"Field type args: {get_args(field.type)}")
        print(f"Field typing_inspect origin: {typing_inspect.get_origin(field.type)}")
        print(f"Field typing_inspect args: {typing_inspect.get_args(field.type)}")

