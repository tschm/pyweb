from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from pyweb.pydash.common import *

import dash_html_components as html


class Help(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def register_callback(self):
        pass

    def build_layout(self):
        return html.H1("Hello World")


if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    with app.test_request_context():
        db = SQLAlchemy(current_app)

    h = Help.construct_with_flask(server=app, url="/admin")

    assert isinstance(h, Dash)
    assert isinstance(h, Help)
    assert isinstance(h, App)
    h.serve(name="admin")
