import logging

from pyweb.pydash.common import App
import dash_html_components as html

if __name__ == '__main__':
    from waitress import serve
    from pyweb.application import create_server

    class xxx(App):
        def build_layout(self):
            return html.Div(id="thomas")

        def register_callback(self):
            pass

    server = create_server(name="wurst", extensions=[])

    with server.app_context():
        app = xxx.construct_with_flask(server=server, url="/test")
        print("http://localhost:8050/test")

        app.logger.setLevel(logging.DEBUG)
        app.logger.info("wurst")
        print(app.logs)

        serve(app=server, port=8050)