from datetime import datetime, timedelta
from .item import Item
from .consumable import Consumable
from weapon import Weapon
from armor import Armor


class Inventory:
    MAX_SIZE = 36  # 3 строки по 9 + 9 хотбар

    def __init__(self):
        self.items: list[Item] = []          # все предметы подряд
        self.hotbar_size = 9                 # первые 9 слотов хотбар
        self.is_open = False

        self.equipped_armor: dict[str, Armor | None] = {
            "helmet":  None,
            "chest":   None,
            "gloves":  None,
            "boots":   None,
        }
        # Экипированное оружие
        self.equipped_weapon: Weapon | None = None

        # Активные эффекты
        self._active_effects: list[dict] = []

    # Добавление / удаление

    def add_item(self, item: Item) -> bool:
        if item.is_stackable:
            for existing in self.items:
                if existing.item_id == item.item_id:
                    if existing.quantity < existing.max_stack_size:
                        existing.quantity += item.quantity
                        return True

        if len(self.items) >= self.MAX_SIZE:
            return False

        self.items.append(item)
        return True

    def remove_item(self, item: Item, quantity: int = None) -> bool:
        for i, existing in enumerate(self.items):
            if existing is item or existing.item_id == item.item_id:
                qty = quantity if quantity is not None else existing.quantity
                if qty >= existing.quantity:
                    self.items.pop(i)
                else:
                    existing.quantity -= qty
                return True
        return False

    def remove_by_index(self, index: int, quantity: int = None) -> Item | None:
        if not (0 <= index < len(self.items)):
            return None
        item = self.items[index]
        qty = quantity if quantity is not None else item.quantity
        if qty >= item.quantity:
            return self.items.pop(index)
        else:
            item.quantity -= qty
            return item

    def get_item(self, index: int) -> Item | None:
        if 0 <= index < len(self.items):
            return self.items[index]
        return None

    def swap(self, index1: int, index2: int) -> bool:
        if 0 <= index1 < len(self.items) and 0 <= index2 < len(self.items):
            self.items[index1], self.items[index2] = self.items[index2], self.items[index1]
            return True
        return False
    
    # Использование

    def use_item(self, index: int, player) -> tuple[bool, str]:
        item = self.get_item(index)
        if item is None:
            return False, "Нет предмета в этой ячейке"

        if isinstance(item, Consumable):
            return self._use_consumable(item, index, player)

        if isinstance(item, Weapon):
            return self._equip_weapon(item)

        if isinstance(item, Armor):
            return self._equip_armor(item)

        return False, f"«{item.name}» нельзя использовать"

    def _use_consumable(self, item: Consumable, index: int, player) -> tuple[bool, str]:
        if item.quantity <= 0:
            return False, f"«{item.name}» закончилось"

        effect = item.effect_type
        value  = item.effect_value

        if effect == "health":
            if player.cur_hp >= player.max_hp:
                return False, "HP уже полное!"
            healed = min(value, player.max_hp - player.cur_hp)
            player.cur_hp += healed
            msg = f"{item.name}: HP +{healed}"

        elif effect == "speed":
            if not hasattr(player, "original_speed"):
                player.original_speed = player.speed
            player.speed = player.original_speed + value
            end_time = datetime.now() + timedelta(seconds=item.duration)
            self._active_effects.append({
                "stat": "speed", "value": value,
                "end_time": end_time, "player": player
            })
            msg = f"{item.name}: скорость +{value} на {item.duration:.0f} сек"

        elif effect == "stamina":
            heal = min(value, getattr(player, "max_stamina", 100) - getattr(player, "stamina", 0))
            player.stamina = getattr(player, "stamina", 0) + heal
            msg = f"{item.name}: выносливость +{heal}"

        else:
            msg = f"{item.name}: эффект «{effect}» применён"

        item.quantity -= 1
        if item.quantity <= 0:
            self.items.pop(index)

        return True, msg

    def _equip_weapon(self, item: Weapon) -> tuple[bool, str]:
        self.equipped_weapon = item
        return True, f"{item.name}: экипировано"

    def _equip_armor(self, item: Armor) -> tuple[bool, str]:
        self.equipped_armor[item.armor_type] = item
        return True, f"{item.name}: надето"

    def update_effects(self) -> list[str]:
        messages = []
        still_active = []
        for eff in self._active_effects:
            if datetime.now() > eff["end_time"]:
                player = eff["player"]
                if eff["stat"] == "speed" and hasattr(player, "original_speed"):
                    player.speed = player.original_speed
                    del player.original_speed
                messages.append(f"Эффект «{eff['stat']}» закончился")
            else:
                still_active.append(eff)
        self._active_effects = still_active
        return messages

    def toggle(self):
        self.is_open = not self.is_open

    def is_full(self) -> bool:
        return len(self.items) >= self.MAX_SIZE

    @property
    def hotbar_items(self) -> list[Item]:
        return self.items[:self.hotbar_size]

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"Инвентарь: {len(self.items)}/{self.MAX_SIZE}"
