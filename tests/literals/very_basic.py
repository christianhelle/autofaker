from typing import Literal
import random

MyLiteral = Literal["pending", "approved", "rejected"]

# Test selecting a random value from the allowed values
literals = ["pending", "approved", "rejected"]  # Hardcoded for testing
selected = random.choice(literals)
print(f"Selected value: {selected}")
