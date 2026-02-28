import dataclasses

import pandas as pd

from autofaker.attributes import Attributes
from autofaker.generator import TypeDataGenerator


class PandasDataFrameGenerator:
    def __init__(self, t, rows: int = 3, use_fake_data: bool = False):
        self.t = t
        self.data = []
        for _ in range(rows):
            row = TypeDataGenerator.create(t, use_fake_data=use_fake_data).generate()
            self.data.append(row)

    def _get_columns(self, instance):
        return [
            attr
            for attr in dir(instance)
            if (dataclasses.is_dataclass(getattr(instance, attr))
            or not callable(getattr(instance, attr)))
            and not attr.startswith("__")
        ]

    def generate(self):
        if not self.data:
            sample = TypeDataGenerator.create(self.t).generate()
            columns = self._get_columns(sample)
            return pd.DataFrame(columns=columns)
        members = self._get_columns(self.data[0])
        rows = []
        for d in self.data:
            row = []
            for member in members:
                row.append(Attributes(d).get_attribute(member))
            rows.append(row)
        return pd.DataFrame(rows, columns=members)
