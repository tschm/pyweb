import logging

from pyweb.pydash.common import DashLogger


def test_dashlogger():
    handler = DashLogger()
    handler.setLevel(logging.DEBUG)
    logger = logging.getLogger(__name__)
    #assert logger.logs == []

    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    # this should call the emit
    logger.info("test")
    assert handler.logs == ["test"]
