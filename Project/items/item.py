from .rarity import Rarity


class Item:
    def __init__(
            self,
            item_id: str = 0,
            name: str = "",
            description: str = "",
            icon_path: str = "",
            rarity: Rarity = Rarity.COMMON,
    ):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.icon_path = icon_path
        self.rarity = rarity

        self.is_stackable = False
        self.max_stack_size = 1
        self.quantity = 1

    def __str__(self):
        return f"{self.name} [{self.rarity}] (ID: {self.item_id})"


    def get_info(self) -> str:
        info = (
            f"Название: {self.name}\n"
            f"Редкость: {self.rarity.display_name}\n"
            f"Описание: {self.description}\n"
        )
        if self.is_stackable:
            info += f"Количество: {self.quantity}/{self.max_stack_size}\n"
        return info

