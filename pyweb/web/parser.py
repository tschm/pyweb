import json

import pandas as pd
from flask import Response


def respond_pandas(frame, fmt="json"):
    if isinstance(frame, pd.DataFrame):
        if fmt.lower().strip() == "json":
            return Response(frame.to_json(orient="table"), mimetype="application/json")

        if fmt.lower().strip() == "csv":
            return Response(frame.to_csv(), mimetype="text/csv")

    if fmt.lower().strip() == "json":
        return Response(json.dumps(frame), mimetype="application/json")

    return None
