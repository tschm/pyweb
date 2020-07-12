# pyweb

[![Action Status](https://github.com/lobnek/pyweb/workflows/Test/badge.svg)](https://github.com/lobnek/pyweb/actions/)

This project is the backbone for the web applications of Lobnek Wealth Management. 

## Technology

We take advantage of various technologies here

* We host static files with [Whitenoise](https://pypi.org/project/whitenoise/).
    ```python
    # add whitenoise
    server.wsgi_app = WhiteNoise(server.wsgi_app, root='/static', prefix='assets/')
    ```
  
* We use the [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/) server.
    ```python
    #!/usr/bin/env python3
    from waitress import serve
    from pyweb.app import create_app
    
    
    if __name__ == '__main__':
        serve(app=create_app(), port=8000)
    ``` 
    
* The flask application is relying on the popular blueprint concept. We expose a REST server for performance calculations.
Applications built on this package can reuse the very same blueprints and remain slim and elegant.
    ```python
    def create_app():
        server = create_server(extensions=[engine, cache], static_folder="/static")
    
        with server.test_request_context():
            current_app.register_blueprint(blue_whoosh, url_prefix="/whoosh")
            current_app.register_blueprint(blue_post, url_prefix="/engine")
            # links
            links = [LinkTuple(href=url_for("whoosh.search", fmt="html"), text="Search")]
            current_app.register_blueprint(construct_navbar(links=links, version=version), url_prefix="/admin")
        
        # add whitenoise
        server.wsgi_app = WhiteNoise(server.wsgi_app, root='/static', prefix='assets/')
        
        return server
    ```    
* We use Jinja2 templates to create a menubar:
    ```python
    {% extends "base.html" %}
    {% block menu %}
        <ul class="nav navbar-nav mr-auto">
            {% if links %}
                {% for link in links %}
                    <a class="nav-item nav-link" href="{{ link.href }}">{{ link.text }}</a>
                {% endfor %}
            {% endif %}
        </ul>
    {% endblock %}
    ```
* We use Flask extensions and a central settings.cfg file to initialize the extensions only once. Within the Dockerfile we set
    ```python
    ENV APPLICATION_SETTINGS="/server/config/settings.cfg"
    ```


* We extensively test the app and achieve a full coverage score. We test against a client created as a pytest fixture.
    ```python
    @pytest.fixture(scope="module")
    def client():
        app = create_app()
    
        with app.app_context():
            __init_session()
    
        yield app.test_client()
    ```



