#!/usr/bin/env python3
import os

from waitress import serve

from pyweb.app import create_app

# def create_server(extensions=None, static_folder=None):
#     server = Flask(__name__, static_folder=static_folder)
#
#     # Check if the environment variable is set, otherwise use a default config
#     app_settings = os.getenv("APPLICATION_SETTINGS", "default_config.py")
#
#     try:
#         success = server.config.from_envvar("APPLICATION_SETTINGS", silent=False)
#     except RuntimeError:
#         # Fallback if the environment variable is not set or file doesn't exist
#         print(f"Warning: Could not load config from {app_settings}, using default config.")
#         server.config.from_pyfile(app_settings)
#
#     # Continue with server setup (add extensions, etc.)
#     if extensions:
#         for ext in extensions:
#             ext.init_app(server)
#
#     return server

if __name__ == "__main__":
    # Use environment variable to set port, default to 8000 if not set
    port = int(os.getenv("PORT", 8000))  # Defaults to 8000 if PORT is not set
    print(f"Go to http://localhost:{port}/admin")

    # Initialize app from create_app function
    server = create_app()

    # Run the app using Waitress on the specified port
    serve(app=server, host="0.0.0.0", port=port)

# try whitenoise
