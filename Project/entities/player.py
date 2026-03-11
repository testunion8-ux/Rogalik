import threading
from .entity import Entity
from datetime import datetime
from items import Item
from typing import List


class Player(Entity):

    def dead(self,enemy):
        raise Exception("Конец игры")

    def __init__(self, coordss, cd_stamina, max_stamina):
        super().__init__(hp=50, speed=5, coords=coordss, damage=5, cd=1, sign="ь", cd_block=0)
        self.last_cd_stamina = datetime.now()
        self.cd_stamina = cd_stamina
        self.max_stamina = max_stamina

    def otcat_charactristiki(self, chot_eto, cr):
        if chot_eto == 1:
            self.speed = cr
        if chot_eto == 2:
            stamina = self.cd_stamina + cr
            min(stamina, self.max_stamina)
            self.cd_stamina = stamina

    def stamina(self):
        cur_speed = 1
        cur_s = self.speed
        if self.cd_stamina > 0:
            self.cd_stamina -= 1
            self.speed = cur_s + 5
            thr = threading.Timer(1, self.otcat_charactristiki, args=(cur_speed, cur_s))
            thr.start()

    def regeniration_stamina(self, df):
        if self.cd_stamina < 5:
            cr = 2
            thr = threading.Timer(6, self.otcat_charactristiki, args=(cr, df))
            thr.start()

    def desh(self, map):
        if self.cd_stamina < 2:
            return None

        self.cd_stamina = self.cd_stamina - 2

        for i in range(1, 4):
            way_x = self.x + self.d_x
            way_y = self.y + self.d_y
            # enemy = map.get_entity_xy(way_x, way_y)
            #
            # if enemy == None:
            if 0 <= way_x < map.width and 0 <= way_y < map.height:
                if not map.is_empty_struct(way_x, way_y):
                   break
                map.entity_move_desh(0, (self.d_x), (self.d_y))
