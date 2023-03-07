from io import StringIO

import pandas as pd


def post(client, data, url):
    response = client.post(url, data=data)
    if response.status_code != 200:
        raise AssertionError(
            "The return code is {r}".format(r=response.status_code))
    return response


def get(client, url):
    response = client.get(url)
    if response.status_code != 200:
        raise AssertionError(f"The return code is {response.status_code}")
    return response


def response2csv(response, **kwargs):
    if response.status_code != 200:
        raise AssertionError(f"The return code is {response.status_code}")
    return pd.read_csv(StringIO(response.data.decode()), **kwargs)


def response2json(response, **kwargs):
    if response.status_code != 200:
        raise AssertionError(f"The return code is {response.status_code}")
    return pd.read_json(response.data.decode(), **kwargs)
