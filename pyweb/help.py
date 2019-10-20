import dash_html_components as html

from pyweb.dash.common import *


class Help(App):
    def __init__(self, app=None):
        super().__init__(app)

    def register_callback(self):
        pass

    @property
    def layout(self):
        return html.H1("Hello World")


if __name__ == '__main__':
    Help().serve()
