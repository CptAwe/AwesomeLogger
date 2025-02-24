from awesomelogger import Log
from unittest import TestCase

class AwesomeLoggerTester(TestCase):

    __logger = Log(
        name=__name__,
        logging_level="INFO"
    ).logger

    def test_all_messages(self):

        self.__logger.debug("Debug message")
        self.__logger.info("Info message")
        self.__logger.warning("Warning message")
        self.__logger.error("Error message")
        self.__logger.critical("Critical message")
