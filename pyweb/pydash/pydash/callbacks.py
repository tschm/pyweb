from io import StringIO

import pandas as pd


class Cache:
    @staticmethod
    def read_json(f):
        return pd.read_json(StringIO(f), orient="split")

    @staticmethod
    def to_json(frame):
        return frame.to_json(orient="split")
