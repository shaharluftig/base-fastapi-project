import logging

from api.v1.config import config

logging.basicConfig(level=logging.INFO, handlers=config.log_handlers,
                    format='%(asctime)s %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger("logger")
