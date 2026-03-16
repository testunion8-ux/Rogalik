
import  random
from .enemy import Enemy
from  datetime import *
from  .player import Player

class EnemyManager:
    zaebzlo =  datetime.now()
    path =  None


    def __init__(self, map):
        self.map = map
        self.old_position = (Player.x,Player.y)
    def tick(self):
        MC = self.map.get_MC()
        for idx, entity in enumerate(self.map.entity_list):

            if not isinstance(entity, Enemy):
                continue

            dist, start, target = entity.get_dist(MC)

            if dist <= entity.devil_trigger:
                if MC != self.old_position:
                    path = self.map.path(self.map, start, target)

                if (entity.max_hp * 0.3) >= entity.cur_hp:

                    if random.randint(1,5) <=5:
                        if path and len(path) > 1:
                            a, b = path[1]
                            x = a - entity.x
                            y = b - entity.y
                            self.map.entity_move(idx, x, y)


                    else:
                        if path and len(path) > 1:
                            a, b = path[1]
                            x = a - entity.x
                            y = b - entity.y
                            if dist > 1:
                                self.map.entity_move(idx, x, y)

                            if dist <= entity.trigger_damage:
                                Enemy.atack(self.map.entity_list[idx], self.map)

                else:
                    if path and len(path) > 1:
                        a, b = path[1]
                        x = a - entity.x
                        y = b - entity.y
                        if dist > 1:
                            self.map.entity_move(idx, x, y)

                        if dist <= entity.trigger_damage:
                            Enemy.atack(self.map.entity_list[idx], self.map)

