from map import Map
from .entity import Entity

class Enemy(Entity):
    def __init__(self, hp, speed, coords, damage, cd, sign='ъ', devil_trigger=5,trigger_damage=1):
        super().__init__(hp, speed, coords, damage, cd, sign)
        self.devil_trigger = devil_trigger
        self.trigger_damage = trigger_damage
