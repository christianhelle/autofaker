from typing import Literal, get_origin, get_args

print("Testing Literal types")
MyLiteral = Literal['a', 'b']
print(f"Type: {repr(MyLiteral)}")
print(f"Type type: {type(MyLiteral)}")
print(f"Origin: {get_origin(MyLiteral)}")
print(f"Args: {get_args(MyLiteral)}")
