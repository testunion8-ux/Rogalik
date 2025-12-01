from entity import Entity


class Enemy(Entity):
    def __init__(self, hp, speed, coords, damage, sign='ъ', devil_trigger=5):
        super().__init__(hp, speed, coords, damage, sign)
        self.devil_trigger = devil_trigger
