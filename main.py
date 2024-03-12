from src.awesomelogger.customLogger import Log

__logger = Log(
    name=__name__,
    logging_level="INFO"
).logger

def main():

    __logger.debug("Debug message")
    __logger.info("Info message")
    __logger.warning("Warning message")
    __logger.error("Error message")
    __logger.critical("Critical message")


if __name__ == "__main__":

    main()
