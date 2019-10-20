import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
from urllib.parse import quote

from collections import namedtuple
Page = namedtuple('Page', ['Link', 'id', 'href', 'layout'])

def dropdown(options, id):
    return dcc.Dropdown(
            id=id,
            options=[{'label': name, 'value': name} for name in options],
            value=options[0],
            clearable=False,
            multi=False,
            searchable=True
        )

def dropdown_multi(options, id):
    return dcc.Dropdown(
            id = id,
            options=[{'label': name, 'value': name} for name in options],
            multi=True,
            searchable=True
    )
 

def frame2lines(frame):   
    return [go.Scatter(
            x=frame[col].dropna().index, y=frame[col].dropna().values,
            mode="lines", name=col, showlegend=True) for col in frame]
   
def year_slider(minyear, maxyear):
        return dcc.RangeSlider(
            id='year-slider',
            min=minyear,
            max=maxyear,
            value=[minyear, maxyear],
            marks={str(year): str(year) for year in range(minyear, maxyear + 1)},
            step=None
        )

def frame2href(frame):
    csv_string = frame.to_csv(encoding='utf-8')
    return "data:text/csv;charset=utf-8," + quote(csv_string)


def build_app(name):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(name, external_stylesheets=external_stylesheets)
    app.logger.handlers = []

    # Since we're adding callbacks to elements that don't exist in the app.layout,
    # Dash will raise an exception to warn us that we might be
    # doing something wrong.
    # In this case, we're adding the elements through a callback, so we can ignore
    # the exception.
    app.config.suppress_callback_exceptions = True

    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])

    return app


def pages2index(pages):
    from itertools import chain
    divs = [[html.A(page.Link, id=page.id, href=page.href), html.Br()] for page in pages]
    return html.Div(list(chain.from_iterable(divs)))