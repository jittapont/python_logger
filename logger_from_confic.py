import json
import logging
import logging.config
from pathlib import Path

# logging.config.fileConfig('logging.conf')

# # create logger
# logger = logging.getLogger('simpleExample')

# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

current_directory = Path()
log_file_name = Path(__file__).stem
log_folder = current_directory / "logs"
log_config_path = current_directory / 'logging.json'


def setup_logging(log_file_name, log_folder, log_config_path):
    if not log_folder.exists():
        log_folder.mkdir()
    with open(log_config_path, "r") as f:
        config = json.load(f)
    config["handlers"]["file_handler"]["filename"] = str(log_folder /
                                                         config["handlers"]["file_handler"]["filename"].format(
                                                             filename=log_file_name))
    logging.config.dictConfig(config)


setup_logging(log_file_name, log_folder, log_config_path)
logger = logging.getLogger(log_file_name)
logger.info('Startlogging:')
try:
    logger.info("start div")
    1/0
except Exception as e:
    logger.exception(f"Error in div -> {repr(e)}")
