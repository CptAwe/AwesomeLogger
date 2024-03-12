import sys
from logging import LogRecord, StreamHandler


LOGGER_COLOURS = {
    "DEBUG" : "\x1b[38;20m", # Grey
    "INFO" : "\x1b[38;20m", # Grey
    "WARNING" : "\x1b[33;20m", # Yellow
    "ERROR" : "\x1b[31;20m", # Red
    "CRITICAL" : "\x1b[31;1m", # Bold Red
    "RESET" : "\x1b[0m"
}

class CustomStreamHandler(StreamHandler):

    def __init__(self, enable_colours = True) -> None:
        self.__enable_colours = enable_colours
        return super().__init__(sys.stdout)

    def emit(self, record: LogRecord) -> None:
        print(record.levelname)

        record.message = LOGGER_COLOURS[record.levelname] + record.message + LOGGER_COLOURS["RESET"]
        print(record.message)

        return super().emit(record)
    
