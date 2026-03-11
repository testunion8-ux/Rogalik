from fileinput import close

from .enemy import Enemy


class EnemyManager:
    def __init__(self, map):
        self.map = map

    def tick(self):
        MC = self.map.get_MC()

        # Ищем врагов в списке
        for idx, entity in enumerate(self.map.entity_list):
            if isinstance(entity, Enemy):
                # Получаем расстояние от моба до игрока
                dist = entity.get_dist(MC)
                current_entity = self.map.entity_list[idx]
                # print(f"{entities.sign}: {entities.coords}")
                if dist <= entity.devil_trigger:
                    # Двигаем их на игрока
                    norm = MC.get_normalize(entity)
                    self.map.entity_move(idx, round(norm[0]), round(norm[1]))

                if dist <= entity.trigger_damage and current_entity != 12 :
                    # Двигаем их на игрокаssssss
                    current_entity.atack(self.map)


    def attack_Player(self):
        # как то определ
                MC = self.map.get_MC()

                # Ищем врагов в списке
                for idx, entity in enumerate(self.map.entity_list):
                    if isinstance(entity, Enemy):
                        # Получаем расстояние от моба до игрока
                        dist = entity.get_dist(MC)
                        # print(f"{entities.sign}: {entities.coords}")
                        if dist <= entity.trigger_damage:
                            # Двигаем их на игрока
                            entity.atack(MC)

