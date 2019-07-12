# import pandas.util.testing as pdt
#
# from pyweb.core.whoosh import Whoosh
# from test.settings import read
#
#
# class TestWhoosh(object):
#     def test_whoosh(self):
#         w1 = Whoosh(title="A", content="AA", path="aaa", group="GA")
#         w2 = Whoosh(title="B", content="BB", path="bbb", group="GB")
#
#         w = read("whoosh.csv", index_col=0)
#         print(Whoosh.frame(rows=[w1, w2]))
#         print(w)
#
#         pdt.assert_frame_equal(w, Whoosh.frame(rows=[w1,w2]), check_dtype=False)
#
#         assert str(w1) == "Whoosh(title=A)"
