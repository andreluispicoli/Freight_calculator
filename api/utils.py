import logging


class Logging:

    def __init__(self, file_name):
        self.logger = logging.getLogger(file_name)
        self.logger.setLevel(logging.DEBUG)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)
