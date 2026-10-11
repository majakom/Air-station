from config_handler import ConfigHandler

import logging
import threading
from typing import Any

class MQTTClient(threading.Thread):
    def __init__(self, config: ConfigHandler, topics: list[Any]):
        self._setup()

    def _setup(self):
        self._logging_setup()

    def _logging_setup(self):
        self.logger = logging.getLogger(__name__)

    def run():
        pass
