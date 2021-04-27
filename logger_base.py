
import logging
logger = logging.getLogger('P_INFO')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('info_hostory.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s  %(filename)s _line: %(lineno)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

if __name__ == '__main__':
    logger.debug('mensaje debug')
    logger.info('mensaje info')
    logger.warning('mensaje warning')
    logger.error('mensaje error')
    logger.critical('mensaje critical')

