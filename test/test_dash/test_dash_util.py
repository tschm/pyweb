import pandas as pd

from pyweb.pydash.pydash.dash_util import dropdown, dropdown_multi, year_slider, frame2href, frame2lines, frame2table
from test.settings import read


class TestDashUtil(object):
    def test_dropdown(self):
        assert str(dropdown(options=["A", "B"], id=1))

    def test_dropdown_multi(self):
        assert str(dropdown_multi(options=["A", "B"], id=1))

    def test_year_slider(self):
        assert str(year_slider(1990, 1992))

    def test_href(self):
        frame = read("price.csv", index_col=0)
        assert frame2href(frame)

    def test_lines(self):
        frame = read("price.csv", index_col=0)
        assert frame2lines(frame)

    def test_table(self):
        frame = read("price.csv", index_col=0)
        columns, data = frame2table(frame)
        assert columns
        assert data

    def test_table_empty(self):
        #frame = read("price.csv", index_col=0)
        frame = pd.DataFrame({})
        columns, data = frame2table(frame)
        assert columns == []
        assert data == []