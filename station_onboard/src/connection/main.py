from config_handler import ConfigHandler
from connection_handler import ConnectionHandler

from pathlib import Path

if __name__ == "__main__":
    PATH = Path("config.yaml")
    newConfigHandler = ConfigHandler(pathname=PATH)
    newConnectionHandler = ConnectionHandler(config=newConfigHandler)