import json

import pandas as pd
from flask import Response


def respond_pandas(frame, fmt="json"):
    # Ensure `fmt` is normalized
    fmt = fmt.lower().strip()

    # Handle DataFrame input
    if isinstance(frame, pd.DataFrame):
        if fmt == "json":
            # Convert DataFrame to JSON with table format
            return Response(frame.to_json(orient="table"), mimetype="application/json")

        if fmt == "csv":
            # Convert DataFrame to CSV
            return Response(frame.to_csv(), mimetype="text/csv; charset=utf-8")

    # Handle non-DataFrame input (assuming `frame` is serializable)
    if fmt == "json":
        return Response(json.dumps(frame), mimetype="application/json")

    # If no matching format, return None or you could raise an error or return a 400 response
    return Response("Unsupported format", status=400, mimetype="text/plain")
