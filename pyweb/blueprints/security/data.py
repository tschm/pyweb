import numpy as np
import pandas as pd


def _f(series):
    if series is not None and not series.empty:
        return series.dropna()
    else:
        return np.nan


def prices(securities):
    return pd.DataFrame({security.name: _f(security.price) for security in securities}).dropna(axis=1, how="all")

