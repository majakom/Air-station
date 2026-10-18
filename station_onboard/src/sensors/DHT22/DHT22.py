from DHT22_config_loader import DHT22ConfigLoader

import adafruit_dht
import logging
import threading
from pathlib import Path
import time

class DHT22(threading.Thread):
    def __init__(self):
        super().__init__()
        self._pathname = Path("DHT22_config.yaml") #TODO: move this
        self._setup()

    def _setup(self):
        self._setup_logging()
        self._loader()
        self._setup_device()

    def _setup_logging(self):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def _loader(self):
        """
        Load config file for DHT22 sensor from given pathname
        """
        self._config = DHT22ConfigLoader(pathname=self._pathname)

    def _setup_device(self):
        self.device = adafruit_dht.DHT22(self._config.pin, use_pulseio=False)

    def read_temperature(self) -> float:
        return self.device.temperature

    def read_humidity(self) -> float:
        return self.device.humidity

    def run(self):
        """
        Sensor runner
        """
        while True: 
            temperature = self.read_temperature()
            humidity = self.read_humidity()
            time.sleep(10)

    def stop(self):
        """
        Stop sensor runner
        """
        self.device.exit()