from pyweb.core.cache import read_cache

from test.settings import read, client
import pandas.testing as pt


def test_cache(client):
    def __f():
        return read("price.csv")

    read_cache(name="maffay", fct=__f)
    pt.assert_frame_equal(read_cache(name="maffay"), read("price.csv"))