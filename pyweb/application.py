from flask import Flask, current_app


def create_server(static_folder="static", template_folder="templates", extensions=None):
    server = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

    #server.logger.info("Server created using Flask: {s}".format(s=server))

    success = server.config.from_envvar('APPLICATION_SETTINGS', silent=False)
    assert success

    #server.logger.info("Configuration: \n{c}".format(c=server.config))

    with server.app_context():
        for extension in extensions:
            extension.init_app(current_app)
            #server.logger.info("Extension: \n{e}".format(e=extension))

    return server
