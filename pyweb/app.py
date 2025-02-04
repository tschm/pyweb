import json
from pathlib import Path
from typing import Any, List, Optional

from flask import Flask
from whitenoise import WhiteNoise

from .blueprints.admin.api import blueprint as blue_admin
from .blueprints.post.api import blueprint as blue_post
from .exts.exts import bootstrap, cache


def create_server(
    name: str = __name__,
    static_folder: Optional[str] = None,
    template_folder: Optional[str] = None,
    extensions: Optional[List[Any]] = None,
) -> Flask:
    """
    Creates and configures a Flask server instance with optional extensions and configuration.

    Args:
        name: The name of the Flask application. Defaults to __name__.
        static_folder: Path to the static files directory. Defaults to None.
        template_folder: Path to the templates directory. Defaults to None.
        extensions: List of Flask extensions to initialize. Defaults to None.
                   Extensions should have an init_app method.

    Returns:
        Flask: Configured Flask application instance.

    Raises:
        FileNotFoundError: If the config file cannot be found.
        ConfigurationError: If there's an error loading the configuration.
        ValueError: If an extension fails to initialize.
    """
    # Initialize Flask app
    server = Flask(name, static_folder=static_folder, template_folder=template_folder)

    # Initialize extensions list if None
    extensions = extensions or []

    try:
        # Attempt to load configuration from file
        config_path = Path(__file__).parent / "config" / "settings.cfg"
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found at: {config_path}")

        success = server.config.from_file(config_path, load=json.load)
        if not success:
            raise ConfigurationError("Failed to load configuration from file")

        # Initialize all provided extensions
        for extension in extensions:
            try:
                if not hasattr(extension, "init_app"):
                    raise ValueError(f"Extension {extension.__class__.__name__} does not have init_app method")
                extension.init_app(server)
            except Exception as e:
                raise ValueError(f"Failed to initialize extension {extension.__class__.__name__}: {str(e)}")

        return server

    except Exception as e:
        # Log the error (assuming you have logging configured)
        server.logger.error(f"Error creating server: {str(e)}")
        raise


class ConfigurationError(Exception):
    """Custom exception for configuration-related errors."""

    pass


def create_app():
    server = create_server(extensions=[cache, bootstrap], static_folder="static")

    server.register_blueprint(blue_post, url_prefix="/engine")
    server.register_blueprint(blue_admin, url_prefix="/admin")

    # add whitenoise
    server.wsgi_app = WhiteNoise(server.wsgi_app, root="static", prefix="/assets")

    return server
