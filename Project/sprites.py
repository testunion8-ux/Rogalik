import pygame


def load_sprites(filename: str, sprite_size: int, sprite_map: dict) -> dict:
    # безопасная загрузка: pygame.image.load может выбросить pygame.error если
    # неинициализирована видео подсистема или файл не найден.
    try:
        sheet = pygame.image.load(filename)
    except Exception as e:
        # выводим понятную ошибку и возвращаем пустой словарь
        print(f"Ошибка загрузки файла {filename}: {e}")
        return {}

    # Попытка конвертировать с альфой, fallback — обычный convert
    try:
        sheet = sheet.convert_alpha()
    except Exception:
        try:
            sheet = sheet.convert()
        except Exception:
            # если не получилось — оставляем как есть
            pass

    sprites = {}

    for item_name, (col, row) in sprite_map.items():
        x = col * sprite_size
        y = row * sprite_size

        if x + sprite_size <= sheet.get_width() and y + sprite_size <= sheet.get_height():
            sprite = sheet.subsurface((x, y, sprite_size, sprite_size))
            sprite = pygame.transform.scale(sprite, (32, 32))
            sprites[item_name] = sprite
        else:
            print(f"СТОП: спрайт {item_name} выходит за пределы файла {filename}")
            surf = pygame.Surface((32, 32), pygame.SRCALPHA)
            surf.fill((255, 0, 255))
            sprites[item_name] = surf

    return sprites