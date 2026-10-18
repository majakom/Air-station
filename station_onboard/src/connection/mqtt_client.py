from config_handler import ConfigHandler

import logging
from typing import Any
import paho.mqtt.client as mqtt
import uuid

class MQTTClient():
    def __init__(self, config: ConfigHandler, topics: list[Any]):
        self.config = config
        self.topics = topics
        self._setup()

    def _setup(self):
        self._logging_setup()
        self.run()

    def _logging_setup(self):
        self.logger = logging.getLogger(__name__)

    def run(self):
        """
        Run MQTT client as a thread
        """
        try:
            self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, uuid.uuid4())
            self.client.username_pw_set(self.config.username, self.config.password)
            #self.client.tls_set()
            self.client.on_connect = self._on_connect
            self.client.on_message = self._on_message
            self.client.on_disconnect = self._on_disconnect
            self.client.connect(self.config.host, self.config.port)
            self.client.loop_forever()
        except Exception as e:
            self._logger.error(f"Error occured during mqtt client run: {e}")

    def _on_connect(self, client, userdata, flags, rc):
        """
        Action on connection
        """
        self._logger.info("Client connected.")
        raise NotImplemented
    
    def _on_message(self, client, userdata, msg):
        """
        Action on message
        """
        self._logger.info(f"Message received: {msg.payload.decode()}")
        raise NotImplemented

    def _on_disconnect(self, client, userdata, rc):
        """
        Action on disconnection
        """
        self._logger.info(f"Disconnecting... ")
        raise NotImplemented

    def publish(self, message: str, topic: str):
        """
        Publish message on topic
        """
        self._logger.info(f"Publishing {message} ---> {topic}")
        self.client.publish(topic, message)

    def disconnect(self):
        """
        Disconnect client
        """
        self.client.disconnect()
