from dash_core_components import Dropdown, RangeSlider

from pyweb.pydash.pydash.dash_util import dropdown, dropdown_multi, year_slider, frame2href, frame2lines
from test.settings import read


class TestDashUtil(object):
    def test_dropdown(self):
        assert str(dropdown(options=["A", "B"], id=1)) #== Dropdown(id=1, options=[{'label': 'A', 'value': 'A'}, {'label': 'B', 'value': 'B'}], value='A', clearable=False, multi=False, searchable=True)

    def test_dropdown_multi(self):
        assert str(dropdown_multi(options=["A", "B"], id=1)) #== Dropdown(id=1, options=[{'label': 'A', 'value': 'A'}, {'label': 'B', 'value': 'B'}], multi=True, searchable=True)

    def test_year_slider(self):
        assert str(year_slider(1990, 1992)) # == RangeSlider(id='year-slider', marks={'1990': '1990', '1991': '1991', '1992': '1992'}, value=[1990, 1992], min=1990, max=1992)

    def test_href(self):
        frame = read("price.csv", index_col=0)
        assert frame2href(frame)

    def test_lines(self):
        frame = read("price.csv", index_col=0)
        assert frame2lines(frame)
