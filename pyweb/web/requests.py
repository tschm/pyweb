import io

import pandas as pd
import requests


def fetch_csv(url, params=None, **kwargs):
    """
    Fetches a CSV file from a URL and returns a pandas DataFrame.

    Args:
    - url (str): The URL from which to fetch the CSV.
    - params (dict, optional): Parameters to pass in the URL query string.
    - **kwargs: Additional keyword arguments passed to `pandas.read_csv`.

    Returns:
    - pd.DataFrame: The CSV data loaded into a pandas DataFrame.

    Raises:
    - AssertionError: If the HTTP response status code is not 200 or CSV cannot be parsed.
    """
    params = params or {}  # Default to empty dict if no params provided
    r = requests.get(url, params=params)

    if r.status_code != 200:
        raise AssertionError(f"Failed to fetch CSV from {url}. Status code: {r.status_code}")

    try:
        # Stream the response directly into pandas read_csv if the content is large
        return pd.read_csv(io.StringIO(r.content.decode(r.encoding or "utf-8")), **kwargs)
    except Exception as e:
        raise AssertionError(f"Failed to parse CSV from {url}. Error: {str(e)}")


def fetch_json(url, params=None, **kwargs):
    """
    Fetches a JSON file from a URL and returns a pandas DataFrame.

    Args:
    - url (str): The URL from which to fetch the JSON.
    - params (dict, optional): Parameters to pass in the URL query string.
    - **kwargs: Additional keyword arguments passed to `pandas.read_json`.

    Returns:
    - pd.DataFrame: The JSON data loaded into a pandas DataFrame.

    Raises:
    - AssertionError: If the HTTP response status code is not 200 or JSON cannot be parsed.
    """
    params = params or {}  # Default to empty dict if no params provided
    r = requests.get(url, params=params)

    if not r.ok:
        raise AssertionError(f"Failed to fetch JSON from {url}. Status code: {r.status_code}")

    try:
        return pd.read_json(io.StringIO(r.json()), **kwargs)
    except Exception as e:
        raise AssertionError(f"Failed to parse JSON from {url}. Error: {str(e)}")
