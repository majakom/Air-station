from config_handler import ConfigHandler
from mqtt_client import MQTTClient

import logging
from pathlib import Path
import threading

class ConnectionHandler(threading.Thread):
    def __init__(self, path: Path):
        super().__init__()
        self._path = path
        self._setup()

    def _setup(self):
        self._setup_logging()
        self._loader()

    def _setup_logging(self):
        logging.basicConfig(level=logging.DEBUG)
        self._logger = logging.getLogger(__name__)

    def _loader(self):
        """
        Load connection configuration from YAML file.
        """
        self._config = ConfigHandler(pathname=self._path)

    def get_all_send_topics(self):
        """
        Get all topics send data from "topics_data/topics_send"
        """
        raise NotImplementedError()

    def run(self):
        """
        Start MQTT client connection
        """
        self.client_mqtt = MQTTClient(config=self._config, topics=self._topics)

    def stop(self):
        """
        Disconnect MQTT client
        """
        self.client_mqtt.disconnect()