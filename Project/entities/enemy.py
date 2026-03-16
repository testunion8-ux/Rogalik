import threading
from datetime import timedelta, datetime
from encodings import search_function

from .entity import Entity
from  .player import  Player
from map import Map

class Enemy(Entity):
    def __init__(self, hp, speed, coords, damage, cd, sign='ъ', devil_trigger=500,trigger_damage=1):
        super().__init__(hp, speed, coords, damage, cd, sign)
        self.devil_trigger = devil_trigger
        self.trigger_damage = trigger_damage


    def atack(self, map: Map):
        try:
            if self.last_cd + timedelta(seconds=self.cd) < datetime.now() :
                self.last_cd = datetime.now()
                Player.get_damage_player(map.get_MC(), self.damage)

        except Exception:
            if map.get_MC().blocki == False and self.blocki == False:
                self.last_cd = datetime.now()
                Player.get_damage_player(map.get_MC(), self.damage)

