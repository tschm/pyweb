import io

import pandas as pd
import requests


def fetch_csv(url, params=None, **kwargs):
    r = requests.get(url, params)
    if r.status_code != 200:
        raise AssertionError(f"The status code is {r.status_code}")
    return pd.read_csv(io.StringIO(r.content.decode()), **kwargs)


def fetch_json(url, params=None, **kwargs):
    r = requests.get(url, params)
    if not r.ok:
        raise AssertionError(f"The status code is {r.status_code}")
    return pd.read_json(r.json(), **kwargs)
