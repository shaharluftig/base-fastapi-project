import logging
import os
import sys
from logging.handlers import RotatingFileHandler

ENV = os.getenv("ENV")


def get_log_handlers():
    if ENV == "prod":
        output_log_file = './logs/system.log'
        max_log_file_size = 10000000
        log_file_count = 100
        return [RotatingFileHandler(output_log_file, maxBytes=max_log_file_size
                                    , backupCount=log_file_count), logging.StreamHandler(sys.stdout)]
    return [logging.StreamHandler(sys.stdout)]


class DefaultConfig:
    port = 8080
    log_handlers = get_log_handlers()


class ProdConfig(DefaultConfig):
    host = "0.0.0.0"
    workers = 4
    reload = False


class DevConfig(DefaultConfig):
    host = "localhost"
    workers = 1
    reload = True


config = ProdConfig if ENV == "prod" else DevConfig
