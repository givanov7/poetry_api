import logging

logger = logging.getLogger("poetry_api")
logger.setLevel(logging.DEBUG)

if not logger.handlers: # Prevent adding multiple handlers if the logger is already configured
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(ch)
