from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
from pyweb.pydash.common import *



import dash_html_components as html


class Help(App):
    def __init__(self, app=None):
        super().__init__(app)

    def register_callback(self):
        pass

    @property
    def layout(self):
        return html.H1("Hello World")


if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    with app.test_request_context():
        db = SQLAlchemy(current_app)

    Help.construct_with_flask(server=app, url="/admin")

    serve(app=app, port=8050)