import sys
import unittest

from autofaker import Autodata


class StaffTests(unittest.TestCase):

    def test_create_pandas_dataframe_returns_not_none(self):
        pdf = Autodata.create_pandas_dataframe(SimpleClass)
        self.assertIsNotNone(pdf)

    @unittest.skipIf(sys.platform.startswith("win") or sys.platform == "darwin", "tests are very slow")
    def test_create_spark_dataframe_returns_not_none(self):
        df = Autodata.create_spark_dataframe(SimpleClass)
        self.assertIsNotNone(df)


class SimpleClass:
    id = 123
    text = 'test'
