import time
from datetime import datetime, timedelta
from math import sqrt
from items import Item
from map import Map
from typing import Optional, Dict, Tuple

class Entity:
    def __init__(self, hp, speed, coords, damage, cd,cd_block,sign = 'ъ', max_stamina=10 ):
        self.sign = sign
        self.damage = damage
        self.cur_hp = hp
        self.max_hp = hp
        self.speed = speed
        self.last_time_move = datetime.now()
        self.cd = cd
        self.coords = list(coords)
        self.direct = [1,0]
        self.last_cd =  datetime.now()
        self.last_cd_block = datetime.now()
        self.cd_block =  cd_block
        self.block =  True

        self.max_stamina = max_stamina
        self.current_stamina = max_stamina

        self.stats = {
            "strength": 10,
            "dexterity": 10,
            "intelligence": 10,
            "charisma": 10,
        }

        self.equipment = {
            "weapon": None,
            "helmet": None,
            "chest": None,
            "gloves": None,
            "boots": None,
        }



    def equip_item(self, item: Item) -> bool:
        """Экипировать предмет"""
        if isinstance(item, Weapon):
            if self.equipment["weapon"]:
                self.unequip_item("weapon")
            self.equipment["weapon"] = item
            return True

        elif isinstance(item, Armor):
            if item.armor_type not in self.equipment:
                return False

            if self.equipment[item.armor_type]:
                self.unequip_item(item.armor_type)

            self.equipment[item.armor_type] = item
            return True

        return False

    def unequip_item(self, slot: str) -> Optional[Item]:
        """Снять предмет с экипировки"""
        if slot not in self.equipment:
            return None

        item = self.equipment[slot]
        if item:
            self.equipment[slot] = None
        return item

    def get_total_defense(self) -> int:
        """Получить общую защиту"""
        total_defense = 0
        for slot, item in self.equipment.items():
            if item and isinstance(item, Armor):
                total_defense += item.defense
        return total_defense

    def get_total_bonuses(self) -> Dict[str, int]:
        """Получить все бонусы от экипировки"""
        bonuses = {
            "health": 0,
            "stamina": 0,
            "speed": 0.0,
        }

        for item in self.equipment.values():
            if item and isinstance(item, Armor):
                bonuses["health"] += item.health_bonus
                bonuses["stamina"] += item.stamina_bonus
                bonuses["speed"] += item.speed_bonus

        return bonuses

    def get_effective_stats(self) -> Dict[str, int]:
        """Получить эффективные характеристики с учётом бонусов"""
        effective_stats = self.stats.copy()

        bonuses = self.get_total_bonuses()
        effective_stats["max_hp"] = self.max_hp + bonuses["health"]
        effective_stats["max_stamina"] = self.max_stamina + bonuses["stamina"]
        effective_stats["speed"] = 5.0 + bonuses["speed"]

        return effective_stats

    def calculate_attack(self) -> Tuple[int, bool]:
        """Рассчитать урон атаки"""
        if not self.equipment["weapon"]:
            return 5, False  # Базовый урон без оружия

        weapon = self.equipment["weapon"]
        return weapon.calculate_damage(self.stats)

    def receive_damage(self, damage: int) -> int:
        """Получить урон с учётом защиты"""
        defense = self.get_total_defense()
        actual_damage = max(1, damage - defense)

        self.cur_hp = max(0, self.cur_hp - actual_damage)
        return actual_damage

    def is_alive(self) -> bool:
        """Проверить, жив ли персонаж"""
        return self.cur_hp > 0

    def heal(self, amount: int) -> int:
        """Восстановить здоровье"""
        old_health = self.cur_hp
        self.cur_hp = min(self.max_hp, self.cur_hp + amount)
        return self.cur_hp - old_health

    def show_status(self) -> str:
        """Показать статус персонажа"""
        status = f"{self.name}\n"
        status += f"Здоровье: {self.cur_hp}/{self.max_hp}\n"
        status += f"Выносливость: {self.current_stamina}/{self.max_stamina}\n"
        status += f"Защита: {self.get_total_defense()}\n"

        if self.equipment["weapon"]:
            status += f"Оружие: {self.equipment['weapon'].name}\n"

        return status

    def show_equipment(self) -> str:
        """Показать экипировку"""
        equipment_text = f"Экипировка {self.name}:\n"
        for slot, item in self.equipment.items():
            if item:
                equipment_text += f"  {slot}: {item.name} [{item.rarity}]\n"
            else:
                equipment_text += f"  {slot}: пусто\n"
        return equipment_text

    @property
    def x(self):
        return self.coords[0]

    @property
    def y(self):
        return self.coords[1]

    @property
    def is_movable(self):
        if self.last_time_move + timedelta(seconds=1 / self.speed) < datetime.now():
            self.last_time_move = datetime.now()
            return True

        return False

    @property
    def d_x(self):
        return self.direct[0]

    @property
    def d_y(self):
        return self.direct[1]

    def dead(self,enemy):
        if enemy in Map.entity_list:
            Map.entity_list.remove(enemy)

    def add_x(self, x):
        self.coords[0] += x

    def add_y(self, y):
        self.coords[1] += y

    def add_coords(self, x, y):
        self.add_x(x)
        self.add_y(y)

    def set_coords(self, x, y):
        self.coords[0] = x
        self.coords[1] = y

    def get_dist(self, other):
        return sqrt( (self.x - other.x) ** 2 + (self.y - other.y) ** 2 )

    def get_normalize(self, other):
        if self.get_dist(other) == 0:
            return 0, 0

        return (self.x - other.x) / self.get_dist(other), (self.y - other.y) / self.get_dist(other)

    def get_damage(self,damage,enemy):
        if self.block :
            self.cur_hp -= damage
            if self.cur_hp <= 0:
                self.dead(enemy)
                self.cur_hp = 0

    def atack(self, map: Map):
        if self.last_cd + timedelta(seconds=self.cd) < datetime.now():
            self.last_cd = datetime.now()
            enemy = map.get_entity_xy(self.x + (self.direct[0]), self.y + (self.direct[1]))
            if enemy != None:
                enemy.get_damage(self.damage, enemy)

    def block(self):
        if self.last_cd_block + timedelta(seconds=self.cd_block) < datetime.now():
            self.last_cd_block = datetime.now()
            self.block  = True

