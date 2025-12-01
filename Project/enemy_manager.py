from map import Map
from enemy import Enemy


class EnemyManager:
    def __init__(self, map: Map):
        self.map = map

    def tick(self):
        MC = self.map.get_MC()

        # Ищем врагов в списке
        for idx, entity in enumerate(self.map.entity_list):
            if isinstance(entity, Enemy):
                # Получаем расстояние от моба до игрока
                dist = entity.get_dist(MC)
                # print(f"{entity.sign}: {entity.coords}")
                if dist <= entity.devil_trigger:
                    # Двигаем их на игрока
                    norm = MC.get_normalize(entity)
                    self.map.entity_move(idx, round(norm[0]), round(norm[1]))
