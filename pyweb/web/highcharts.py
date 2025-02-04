import pandas as pd


def to_json(series):
    """
    Converts a pandas Series to a JSON-like format.

    Args:
    - series (pd.Series): A pandas Series with a timestamp index and numeric values.

    Returns:
    - List of lists where each inner list contains a timestamp (in ms) and a corresponding value.
    """
    # Ensure that the index is of Timestamp type and drop NaN values
    return [
        [int(pd.Timestamp(t).value * 1e-6), float(value)]  # Convert timestamp to ms, value to float
        for t, value in series.dropna().items()
        if isinstance(t, pd.Timestamp)  # Ensure valid timestamp index
    ]


def parse(value):
    """
    Converts a list of timestamp-value pairs back to a pandas Series.

    Args:
    - value (list of lists): A list where each inner list contains a timestamp (ms) and a corresponding value.

    Returns:
    - pd.Series: A pandas Series with timestamps as index and numeric values.
    """
    # Convert list of timestamp-value pairs to Series
    try:
        return pd.Series(
            {
                pd.Timestamp(1e6 * int(v[0])): float(v[1])  # Convert timestamp from ms and value to float
                for v in value
            }
        )
    except Exception as e:
        raise ValueError(f"Error parsing value: {e}")
