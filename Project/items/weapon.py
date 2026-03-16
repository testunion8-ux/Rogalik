import random

from . import Item, Rarity
from typing import Optional, Dict, Tuple

class Weapon(Item):
    """Класс для оружия"""

    def __init__(
            self,
            item_id: str,
            name: str,
            description: str,
            icon_path: str,
            rarity: Rarity = Rarity.COMMON,
            base_damage: int = 10,
            attack_speed: float = 1.0,
            critical_chance: float = 0.05,
            critical_multiplier: float = 1.5,
            scaling_stats: Optional[Dict[str, float]] = None,
    ):
        super().__init__(item_id, name, description, icon_path, rarity)
        self.base_damage = base_damage
        self.attack_speed = attack_speed
        self.critical_chance = critical_chance
        self.critical_multiplier = critical_multiplier
        self.scaling_stats = scaling_stats or {}

    def get_info(self) -> str:
        info = super().get_info()
        info += (
            f"Урон: {self.base_damage}\n"
            f"Скорость атаки: {self.attack_speed:.1f}\n"
            f"Шанс крита: {self.critical_chance * 100:.1f}%\n"
            f"Крит. урон: x{self.critical_multiplier:.1f}\n"
        )
        if self.scaling_stats:
            scaling_text = ", ".join([f"{stat}: x{mult}" for stat, mult in self.scaling_stats.items()])
            info += f"Зависит от: {scaling_text}\n"
        return info
    def calculate_damage(self, character_stats: Dict[str, int]) -> Tuple[int, bool]:
        """
        Рассчитывает урон оружия на основе характеристик персонажа.
        Возвращает: (урон, был_ли_критический_удар)
        """
        damage = self.base_damage

        for stat, multiplier in self.scaling_stats.items():
            if stat in character_stats:
                damage += int(character_stats[stat] * multiplier)

        is_critical = False
        if random.random() < self.critical_chance:
            damage = int(damage * self.critical_multiplier)
            is_critical = True

        return max(1, damage), is_critical