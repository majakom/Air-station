from air_quality_config_loader import AirQualityConfigLoader

import logging
from pathlib import Path
import threading

class AirQuality(threading.Thread):
    def __init__(self):
        super().__init__()
        self._setup()
        self._pathname = Path("air_quality_config.yaml") #TODO: move this

    def _setup(self):
        self._setup_logging()
        self._loader()

    def _setup_logging(self):
        logging.basicConfig(level=logging.DEBUG)
        self._logger = logging.getLogger(__name__)

    def _loader(self):
        """
        Load config .yaml file from the given pathname
        """
        self._config = AirQualityConfigLoader(pathname=self._pathname)
        

    def run(self):
        """
        Start sensor runner
        """

    def stop(self):
        """
        Stop sensor runner
        """
        raise NotImplemented