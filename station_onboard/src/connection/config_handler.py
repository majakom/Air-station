from pathlib import Path
import logging
import yaml

def ConfigHandler(pathname: Path):
    def __init__(self):
        self.pathname = pathname
        self._setup()

    def _setup(self):
        self._setup_logging()
        self._make_root()
        self._open_config()

    def _setup_logging(self):
        self.logger = logging.getLogger(__name__)

    def _open_config(self):
        """
        Open config file from res
        """
        with self.config_path.open("r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
            #TODO: validation
            self.host = config["mqtt_data"]["host"]
            self.port = config["mqtt_data"]["port"]

    @staticmethod
    def _make_root(self):
        root = Path(__file__).resolve().parent
        self.config_path = root / Path("res") / self.pathname
