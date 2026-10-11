from config_handler import ConfigHandler
from mqtt_client import MQTTClient

import logging

class ConnectionHandler():
    def __init__(self, config: ConfigHandler):
        self.config = config
        self._setup()

    def _setup(self):
        self._setup_logging()

    def _setup_logging(self):
        self.logger = logging.getLogger(__name__)

    def get_all_send_topics(self):
        """
        Get all topics send data from "topics_data/topics_send"
        """
        pass

    def start_connection(self):
        self.client_mqtt = MQTTClient(config=self.config, topics=self.topics)