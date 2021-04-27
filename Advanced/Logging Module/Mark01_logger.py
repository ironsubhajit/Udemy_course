import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s : %(lineno)d]  %(message)s',
    datefmt='%d - %m - %Y %H:%M:%S',
    level='DEBUG',
    filename='logs.txt'
)
logger = logging.getLogger('test_logger')   # CAN USE __name__ ALSO USE LOGGER Child FORMATTING

logger.info('This is info message')
logger.warning('This is warning message')
logger.debug('This is debug msg')
logger.critical('This is critical error msg')
logger.error('This is error msg')


"""
DEBUG   [THIS IS THE LOWEST LEVEL]
INFO
WARNING
ERROR
CRITICAL
"""
