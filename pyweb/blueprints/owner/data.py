import numpy as np
import pandas as pd


def _f(series):
    if series is not None and not series.empty:
        return series.dropna()
    else:
        return np.nan


def returns(owners):
    return pd.DataFrame({owner.name: _f(owner.returns) for owner in owners}).dropna(axis=1, how="all")


def owner_volatility(owners):
    return pd.DataFrame({owner.name: _f(owner.volatility) for owner in owners}).dropna(axis=1, how="all")
