#!/usr/bin/env python3
from waitress import serve

from pyweb.application import create_app

if __name__ == '__main__':
    # It always run on port 8000 within the container.
    # You need to define the port the container will expose...
    print("Go to http://localhost:4445")

    # This assert fails if we start with docker-compose.test.yml...
    # assert not app.config["TESTING"]
    serve(app=create_app(), port=8000)
