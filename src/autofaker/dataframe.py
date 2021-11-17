import dataclasses

import pandas as pd

from autofaker.attributes import Attributes
from autofaker.generator import TypeDataGenerator


class PandasDataFrameGenerator:
    def __init__(self, t, rows: int = 3, use_fake_data: bool = False):
        self.data = []
        for _ in range(rows):
            row = TypeDataGenerator.create(t, use_fake_data=use_fake_data).generate()
            self.data.append(row)

    def generate(self):
        members = [
            attr for attr in dir(self.data[0])
            if dataclasses.is_dataclass(getattr(self.data[0], attr)) or not callable(getattr(self.data[0], attr)) and not attr.startswith("__")
        ]
        rows = []
        for d in self.data:
            row = []
            for member in members:
                row.append(Attributes(d).get_attribute(member))
            rows.append(row)
        return pd.DataFrame(rows, columns=members)
