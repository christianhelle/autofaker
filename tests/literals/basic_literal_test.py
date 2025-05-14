from typing import Literal
import random

# Create a Literal type
MyLiteral = Literal['a', 'b']

# Print basic info
print(f"MyLiteral: {MyLiteral}")

# Try to get the values using get_args from typing
try:
    from typing import get_args
    print(f"Values using get_args: {get_args(MyLiteral)}")
except Exception as e:
    print(f"Error with get_args: {e}")

# Try to manually select a random value
try:
    values = ('a', 'b')  # Hard-coded values for testing
    selected = random.choice(values)
    print(f"Randomly selected: {selected}")
except Exception as e:
    print(f"Error with random selection: {e}")
