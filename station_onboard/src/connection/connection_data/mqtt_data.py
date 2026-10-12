from dataclasses import dataclass

@dataclass
class MQTTData:
    port: int
    host: str