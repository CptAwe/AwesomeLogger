import logging

from .src.settings.defaultSettings import LOGGER_CONFIGS, TEMP_DIR


class Log():
    '''
    A generic logger
    '''

    def __init__(self, name: str, logging_level: str = LOGGER_CONFIGS["level"], specific_log_file: str = None):

        self.logger = logging.Logger(name, logging_level)

        # initialize the default handlers
        file_handler = LOGGER_CONFIGS["handlers"][0]# The default log file
        stream_handler = LOGGER_CONFIGS["handlers"][1]

        # Add them to the logger
        self.logger.addHandler(file_handler)# add file handler
        self.logger.addHandler(stream_handler)# add stream handler

        # initialize the default formatter
        formatter = logging.Formatter(
            datefmt=LOGGER_CONFIGS["datefmt"],
            fmt=LOGGER_CONFIGS["format"],
            style=LOGGER_CONFIGS["style"]
        )

        # Set up for the specific logger
        if specific_log_file:
            # A specific log file is used for this logger. State that to the main log file
            
            self.logger.info(f"{self.logger.name} will log to {specific_log_file}")

            specific_file_handler = logging.FileHandler(
                filename = TEMP_DIR + specific_log_file,
                mode = 'w'# always overwrite, no need to have GB of logs
            )
            
            # add the new file handler and remove the default one
            self.logger.addHandler(specific_file_handler)
            self.logger.removeHandler(file_handler)

        # Apply formatting
        for hndlr in self.logger.handlers:
            hndlr.setFormatter(formatter)

        self.logger.info(f"A new logger has been initialised: {self.logger.name}")
    
    # debug()
    # def debug(self, *args, **kwargs):
    #     print(*args, **kwargs)
    #     self.logger.debug(*args, **kwargs)
    
    # info()
    # warning()
    # error()
    # critical()
