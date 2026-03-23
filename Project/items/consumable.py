from . import Item
from . import Rarity

class Consumable(Item):
    """Класс для расходуемых предметов"""
    def __init__(
            self,
            item_id: str,
            name: str,
            description: str,
            icon_path: str,
            rarity: Rarity = Rarity.COMMON,
            effect_type: str = "health",
            effect_value: int = 10,
            duration: float = 0.0,
    ):
        super().__init__(item_id, name, description, icon_path, rarity)
        self.effect_type = effect_type
        self.effect_value = effect_value
        self.duration = duration
        self.is_stackable = True
        self.max_stack_size = 10

    def use(self, target=None) -> bool:
        if self.quantity <= 0:
            print(f"Зелье '{self.name}' закончилось!")
            return False

        print(f"Использовано {self.name}!")
        if self.duration > 0:
            print(f"Эффект: {self.effect_type} +{self.effect_value} на {self.duration} сек.")
        else:
            print(f"Эффект: {self.effect_type} +{self.effect_value}")

        self.quantity -= 1
        return True