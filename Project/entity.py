from datetime import datetime, timedelta
from math import sqrt

class Entity:
    def __init__(self, hp, speed, coords, damage, sign = 'ъ'):
        self.sign = sign
        self.damage = damage
        self.cur_hp = hp
        self.max_hp = hp
        self.speed = speed
        self.last_time_move = datetime.now()

        self.coords = list(coords)
        self.angle = 0

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


if __name__ == "__main__":
    e1 = Entity(100, 1, (1, 1), 0)
    print(e1.coords)
    print( e1.x )
    e1.coords = [4, 5]
    print( e1.x )


