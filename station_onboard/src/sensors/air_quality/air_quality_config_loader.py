from air_quality_data.air_quality_data import AirQualityData

import logging
from pathlib import Path
import yaml

class AirQualityConfigLoader:
    def __init__(self, pathname: Path):
        self._pathname = pathname
        self._setup()

    def _setup(self):
        self._setup_logging()
        self._make_root()
        self._loader_config()

    def _setup_logging(self):
        logging.basicConfig(level=logging.DEBUG)
        self._logger = logging.getLogger(__name__)

    def _loader_config(self):
        """
        Load config for path "res/sensors/*.yaml"
        """
        try:
            with self.config_path.open("r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
                self.air_quality_data = AirQualityData(pin=config["device"]["pin"])
                self.pin = self.air_quality_data.pin
        except Exception as e:
            self._logger.error(f"Failed loading config file for Air Quality: {self.config_path} - {e}")

    @staticmethod
    def _make_root(self):
        root = Path(__file__).resolve().parent
        self.config_path = root / Path("res") / Path("sensors") / self._pathname