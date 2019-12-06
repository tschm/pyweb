import logging

from pyweb.pydash.common import DashLogger


class TestLogger(object):
    def test_dashlogger(self):
        handler = DashLogger()
        handler.setLevel(logging.DEBUG)
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        # this should call the emit
        logger.info("test")
        assert handler.logs == ["test"]
