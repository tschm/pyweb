# import logging
#
# from pyweb.pydash.common import DashLogger
#
#
# def test_dashlogger():
#     handler = DashLogger()
#     handler.setLevel(logging.DEBUG)
#     logger = logging.getLogger(__name__)
#
#     logger.setLevel(logging.DEBUG)
#     logger.addHandler(handler)
#     # this should call the emit
#     logger.info("tests")
#     assert handler.logs == ["tests"]
