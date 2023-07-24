import logging
from logging.handlers import RotatingFileHandler

file_handler = RotatingFileHandler('./logs/system.log', maxBytes=10000000, backupCount=100)
console_handler = logging.StreamHandler()

logging.basicConfig(level=logging.INFO, handlers=[file_handler, console_handler],
                    format='%(asctime)s %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger("logger")
