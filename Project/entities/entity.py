import threading
from datetime import datetime, timedelta
from math import sqrt
from map import Map


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
        self.last_cd =  None
        self.last_cd_block = datetime.now()
        self.cd_block =  cd_block
        self.blocki =  False

        self.max_stamina = max_stamina
        self.current_stamina = max_stamina
        self.active_slots = {}

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
        return sqrt( (self.x - other.x) ** 2 + (self.y - other.y) ** 2 ),(self.x,self.y),(other.x,other.y)

    # def get_normalize(self, other):
    #     if self.get_dist(other) == 0:
    #         return 0, 0
    #
    #     return int((self.x - other.x) / self.get_dist(other)), int((self.y - other.y) / self.get_dist(other))

    def get_damage(self,damage,enemy):
        if self.block :
            self.cur_hp -= damage
            if self.cur_hp <= 0:
                self.dead(enemy)
                self.cur_hp = 0

    def atack(self, map: Map):
        try:
            if self.last_cd + timedelta(seconds=self.cd) < datetime.now():
                self.last_cd = datetime.now()
                enemy = map.get_entity_xy(self.x + (self.direct[0]), self.y + (self.direct[1]))
                if enemy != None and self.blocki == False :
                    print(2323232323232)
                    enemy.get_damage(self.damage, enemy)
        except Exception:
            enemy = map.get_entity_xy(self.x + (self.direct[0]), self.y + (self.direct[1]))
            if enemy != None and self.blocki == False:
                print(2323232323232)
                enemy.get_damage(self.damage, enemy)
                self.last_cd = datetime.now()
    def block(self):
        if self.last_cd_block + timedelta(seconds=self.cd_block) < datetime.now():
            self.last_cd_block = datetime.now()
            self.blocki  = True

            thr = threading.Timer(2, lambda: setattr(self, "blocki", False))
            thr.start()
    def blok(self):
        if self.blocki:
            return True
        else:
            return False