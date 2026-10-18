from service import Service

from pathlib import Path

if __name__ == "__main__":
    CONNECTION_FILENAME = Path("config.yaml")

    new_service = Service(connection_filename_config=CONNECTION_FILENAME)
    new_service.start()

    new_service.join()