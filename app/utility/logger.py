import sys
import logging
from logging.handlers import RotatingFileHandler

# Setting logging
logger = logging.getLogger(__name__)

# Logging level threshold
logger.setLevel(logging.INFO)  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# Setting LogRecord
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s')

# handlers
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(formatter)
logger.addHandler(ch)
fh = RotatingFileHandler('app.log', maxBytes=1024 * 1024, backupCount=10)
fh.setFormatter(formatter)
logger.addHandler(fh)

if __name__ == '__main__':
    # test
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

    try:
        1 / 0
    except Exception as e:
        logger.error("Exception occurred", exc_info=True)
