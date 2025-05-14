from dataclasses import dataclass
from typing import Literal, get_origin, get_args

try:
    MyLiteral = Literal['a', 'b']

    print(f"Type: {MyLiteral}")
    print(f"Type type: {type(MyLiteral)}")
    print(f"Origin: {get_origin(MyLiteral)}")
    print(f"Args: {get_args(MyLiteral)}")

    @dataclass
    class DataClassWithLiteral:
        id: int
        status: MyLiteral

    # Get dataclass field types
    for field in DataClassWithLiteral.__dataclass_fields__.values():
        print(f"Field name: {field.name}")
        print(f"Field type: {field.type}")
        print(f"Field type type: {type(field.type)}")
        if field.name == 'status':
            print(f"Field type origin: {get_origin(field.type)}")
            print(f"Field type args: {get_args(field.type)}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
