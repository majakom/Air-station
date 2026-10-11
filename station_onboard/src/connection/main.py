from config_handler import ConfigHandler
from connnection_handler import ConnectionHandler

from pathlib import Path

if __name__ == "__main__":
    PATH = Path("config.yaml")
    newConfigHandler = ConfigHandler(pathname=PATH)