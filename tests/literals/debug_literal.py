from dataclasses import dataclass
from typing import Literal

from autofaker import Autodata

@dataclass
class DataClassWithLiteral:
    id: int
    status: Literal["pending", "approved", "rejected"]

try:
    data = Autodata.create(DataClassWithLiteral)
    print(f"Generated: id={data.id}, status={data.status}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
