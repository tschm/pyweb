from pyweb.core.cache import read_cache

from test.settings import read, client
import pandas.util.testing as pdt


def test_cache(client):
    def __f():
        return read("price.csv")

    read_cache(name="maffay", fct=__f)
    pdt.assert_frame_equal(read_cache(name="maffay"), read("price.csv"))