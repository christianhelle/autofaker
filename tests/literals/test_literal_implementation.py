from dataclasses import dataclass
from typing import Literal, get_origin, get_args
import sys
import traceback

try:
    # Import the needed modules directly
    import random
    
    # Define a simple test for Literal functionality
    print("Step 1: Basic Literal test")
    MyLiteral = Literal['a', 'b']
    print(f"MyLiteral: {MyLiteral}")
    print(f"get_args: {get_args(MyLiteral)}")
    print(f"get_origin: {get_origin(MyLiteral)}")
    
    # Select a random value from the Literal
    values = get_args(MyLiteral)
    choice = random.choice(values)
    print(f"Random choice: {choice}")
    
    # Now import our implementation
    print("\nStep 2: Testing our implementation")
    from autofaker.literals import is_literal_type, LiteralGenerator
    
    # Test the is_literal_type function
    print(f"is_literal_type check: {is_literal_type(MyLiteral)}")
    
    # Try creating a generator and generating a value
    generator = LiteralGenerator(MyLiteral)
    value = generator.generate()
    print(f"Generated value: {value}")
    
    # Test with a dataclass
    print("\nStep 3: Testing with autofaker")
    from autofaker import Autodata
    
    @dataclass
    class DataClassWithLiteral:
        id: int
        status: Literal["pending", "approved", "rejected"]
    
    # Try creating an instance
    print("Creating instance...")
    instance = Autodata.create(DataClassWithLiteral)
    print(f"Created instance: id={instance.id}, status={instance.status}")
    
except Exception as e:
    print(f"\nError: {e}")
    print(f"Python version: {sys.version}")
    traceback.print_exc()
