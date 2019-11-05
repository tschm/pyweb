# -*- coding: utf-8 -*-
import datetime
import logging

import dash
import dash_core_components as dcc
import dash_html_components as html
#from pyweb.dash.common import App

from pyweb.pydash.common import DashLogger, App


class Wurst(App):
    def register_callback(self):
        pass

    def build_layout(self):
        return html.H1('The time is: ' + str(datetime.datetime.now()))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)



if __name__ == '__main__':
    from pyweb.application import create_server
    from waitress import serve

    server = create_server(extensions=[])
    server.logger.setLevel(logging.INFO)

    # create a new handler and add to existing logger
    server.logger.addHandler(DashLogger(fmt='[%(asctime)s] %(levelname)s: %(message)s'))

    Wurst.construct_with_flask(server=server, url="/test")
    print("http://localhost:8050/test")
    serve(app=server, port=8050)

    #app.run_server(debug=True)