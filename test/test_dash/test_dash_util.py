import pandas as pd

from pyweb.pydash.pydash.dash_util import dropdown, dropdown_multi, year_slider, frame2href, frame2lines, frame2table
from test.settings import read


def test_dropdown():
    assert str(dropdown(options=["A", "B"], id=1))


def test_dropdown_multi():
    assert str(dropdown_multi(options=["A", "B"], id=1))


def test_year_slider():
    assert str(year_slider(1990, 1992))


def test_href():
    frame = read("price.csv", index_col=0)
    assert frame2href(frame)


def test_lines():
    frame = read("price.csv", index_col=0)
    assert frame2lines(frame)


def test_table():
    frame = read("price.csv", index_col=0)
    columns, data = frame2table(frame)
    assert columns
    assert data


def test_table_empty():
    frame = pd.DataFrame({})
    columns, data = frame2table(frame)
    assert columns == []
    assert data == []