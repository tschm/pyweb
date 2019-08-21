from py_mini_racer import py_mini_racer
from test.settings import client

class TestRacer(object):
    def test_sum(self):
        ctx = py_mini_racer.MiniRacer()
        assert ctx.eval('1+1') == 2

    def test_lobnek_perf(self, client):
        ctx = py_mini_racer.MiniRacer()
        assert ctx.eval('lobnekperf.drawdown(s)') == 0
