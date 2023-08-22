from flask import Flask


def create_server(
    name=__name__, static_folder=None, template_folder=None, extensions=None
):
    server = Flask(name, static_folder=static_folder, template_folder=template_folder)

    if not extensions:
        extensions = []

    success = server.config.from_envvar("APPLICATION_SETTINGS", silent=False)
    if not success:
        raise AssertionError

    for extension in extensions:
        extension.init_app(server)

    return server
