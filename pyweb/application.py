import abc
from flask import Flask


class Application(object):
    @property
    @abc.abstractmethod
    def blueprints(self):
        """ blueprints registered for the application"""
    @property
    @abc.abstractmethod
    def extensions(self):
        """ extensions registered for the application """

    def register(self, app):
        for extension in self.extensions:
            extension.init_app(app)

        for blueprint in self.blueprints:
            app.register_blueprint(blueprint)


def create_app(application, static_folder, template_folder):
    app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

    success = app.config.from_envvar('APPLICATION_SETTINGS', silent=False)
    assert success

    assert isinstance(application, Application)
    application.register(app)

    print(app.url_map)

    return app

