from dataclasses import dataclass
import board

@dataclass
class DHT22Data:
    pin: int = board.D4