import pandas as pd
from flask_restplus import fields


class HighchartsSeries(fields.String):
    """
    Frame field
    """
    __schema_type__ = 'string'
    __schema_format__ = 'frame'
    __schema_example__ = '{columns=...}'

    def format(self, value):
        return [[int(pd.Timestamp(t).value * 1e-6), float(value)] for t, value in value.dropna().items()]

    @staticmethod
    def to_json(series):
        return [[int(pd.Timestamp(t).value * 1e-6), float(value)] for t, value in series.dropna().items()]

    @staticmethod
    def parse(value):
        return pd.Series({pd.Timestamp(1e6 * int(v[0])): float(v[1]) for v in value})

