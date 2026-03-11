import pygame

class MapItem:
    def __init__(self, item_obj, x, y, sprites_dict):
        self.item = item_obj
        self.x = x
        self.y = y

        sprite_key = None
        name_lower = item_obj.name.lower()

        # Создаем словарь для автоматической подстановки sprite_key
        sprite_mapping = {
            "меч": "start sword",
            "лабрис": "cool axe",
            "зелье здоровья": "health",
            "зелье скорости": "speed",
            "мачете": "machete",
            "крутой меч": "cool sword",
            "топор": "axe"
        }

        # Находим подходящий ключ в словаре
        for key in sprite_mapping:
            if key in name_lower:
                sprite_key = sprite_mapping[key]
                break

        if sprite_key and sprite_key in sprites_dict:
            self.sprite = sprites_dict[sprite_key]
        else:
            # Заглушка с названием
            self.sprite = pygame.Surface((32, 32))
            self.sprite.fill((100, 100, 50))  # не ярко-желтый

            # Пишем первые буквы названия
            font = pygame.font.Font(None, 14)
            text = font.render(item_obj.name[:3], True, (255, 255, 255))
            text_rect = text.get_rect(center=(16, 16))
            self.sprite.blit(text, text_rect)