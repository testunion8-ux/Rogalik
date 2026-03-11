from . import Item, Rarity

class Armor(Item):
    """Класс для брони"""

    def __init__(
            self,
            item_id: str,
            name: str,
            description: str,
            icon_path: str,
            rarity: Rarity = Rarity.COMMON,
            armor_type: str = "chest",
            defense: int = 5,
            health_bonus: int = 0,
            stamina_bonus: int = 0,
            speed_bonus: float = 0.0,
    ):
        super().__init__(item_id, name, description, icon_path, rarity)
        self.armor_type = armor_type
        self.defense = defense
        self.health_bonus = health_bonus
        self.stamina_bonus = stamina_bonus
        self.speed_bonus = speed_bonus

    def get_info(self) -> str:
        info = super().get_info()
        info += (
            f"Тип: {self.armor_type}\n"
            f"Защита: {self.defense}\n"
        )
        if self.health_bonus > 0:
            info += f"Бонус здоровья: +{self.health_bonus}\n"
        if self.stamina_bonus > 0:
            info += f"Бонус выносливости: +{self.stamina_bonus}\n"
        if self.speed_bonus != 0:
            info += f"Бонус скорости: {self.speed_bonus:+.1f}\n"
        return info