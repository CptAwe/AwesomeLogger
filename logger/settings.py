import logging
import os

from logger.handlers.custom import CustomStreamHandler

### DATETIME FORMATS ###
TIME_FORMAT = "%H:%M:%S.%f"
TIME_FORMAT_SIMPLE = "%H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"
DT_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
DT_FORMAT_SIMPLE = "%Y-%m-%d %H:%M:%S"

### DIRECTORIES ###
PARENT_DIR = os.getcwd() + os.sep
TEMP_DIR = os.path.join(PARENT_DIR, "tmp") + os.sep
__DIRECTORIES = [
    TEMP_DIR
]
# Make sure all the directories are created
for dir in __DIRECTORIES:
    if not os.path.isdir(dir): os.mkdir(dir)

#### LOGGER COLOURS ####
ENABLE_LOGGER_COLOURS = True

#### LOGGER SETTINGS ####
LOGGER_CONFIGS = {
    # Make logs pretty
    "datefmt": DT_FORMAT_SIMPLE,
    "format" : '{asctime}:{levelname:<9}:{name} >>> {message}',
    "style" : '{',
    # Where to log
    "handlers" : [
        logging.FileHandler(
            filename = TEMP_DIR + "logs.log",
            mode = 'w'# always overwrite, no need to have GB of logs
        ),
        CustomStreamHandler(ENABLE_LOGGER_COLOURS)
    ],
    # What to log
    # "level" : "NOTSET" if DEVELOPMENT_MODE else "INFO"
    "level" : "ERROR"
}
