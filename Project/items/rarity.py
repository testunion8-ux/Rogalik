from enum import Enum

class Rarity(Enum):
    COMMON = {
        "id": "common",
        "display_name": "Обычный",
        "color": (200, 200, 200),
        "drop_multiplier": 1.0,
    }
    UNCOMMON = {
        "id": "uncommon",
        "display_name": "Необычный",
        "color": (80, 200, 120),
        "drop_multiplier": 0.7,
    }
    RARE = {
        "id": "rare",
        "display_name": "Редкий",
        "color": (70, 130, 250),
        "drop_multiplier": 0.4,
    }
    EPIC = {
        "id": "epic",
        "display_name": "Эпический",
        "color": (180, 70, 250),
        "drop_multiplier": 0.2,
    }
    LEGENDARY = {
        "id": "legendary",
        "display_name": "Легендарный",
        "color": (255, 180, 0),
        "drop_multiplier": 0.1,
    }

    @property
    def id(self) -> str:
        return self.value["id"]

    @property
    def display_name(self) -> str:
        return self.value["display_name"]

    @property
    def color(self) -> tuple[int, int, int]:
        return self.value["color"]

    @property
    def drop_multiplier(self) -> float:
        return self.value["drop_multiplier"]

    def __str__(self) -> str:
        return self.display_name

