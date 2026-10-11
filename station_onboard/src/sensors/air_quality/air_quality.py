import logging

class AirQualitySensor():
    def __init__(self):
        self._setup()

    def _setup(self):
        self._setup_logging()

    def _setup_logging(self):
        self.logger = logging.getLogger(__name__)