import os
from pyweb.web.application import create_server


class MockExtension:
    def init_app(self, server):
        pass


def test_application_extensions(application_settings):
    os.environ["APPLICATION_SETTINGS"] = application_settings
    assert create_server(extensions=[MockExtension()])


def test_application(application_settings):
    os.environ["APPLICATION_SETTINGS"] = application_settings
    assert create_server(extensions=[])
