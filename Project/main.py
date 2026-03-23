from datetime import datetime
from map import Map
from entities import Enemy, EnemyManager
import pygame
from entities.player import Player
from BackMusic import BackgroundMusic
from items import MapItem, Item, Inventory, InventoryRenderer, SWORDS, HEALTH_POTIONS, SPEED_POTIONS
from sprites import load_sprites
import random

if __name__ == "__main__":
    # Размер одного элемента
    EL_SIZE = 25
    GUI_TOP_SIZE = 50

    # Создаем карту
    main_map = Map(40, 30, (10, 10))

    # Создаем менеджера противников
    manager = EnemyManager(main_map)

    # Создаем существо-игрока
    last_gnagatie = datetime.now()
    last_gnagatie2 = datetime.now()

    # Размер окна
    screen_width = main_map.width * EL_SIZE
    screen_height = main_map.height * EL_SIZE + GUI_TOP_SIZE + 50  # +50 для инвентаря
    screen = pygame.display.set_mode((screen_width, screen_height))

    player_spawn = main_map.get_random_free_cell()
    if player_spawn is None:
        raise Exception("Нет места для игрока!")

    main_map.add_entity(
        Player((0, 0), 5, 5),
        main_map.player_spawn_point
    )

    enemy_params = [
        (10, 7, (0, 0), 10, 3, "d"),
        (10, 7, (0, 0), 10, 3, "e"),
        (10, 7, (0, 0), 10, 3, "ъ"),
        (10, 7, (0, 0), 10, 3, "g"),
    ]

    for params in enemy_params:
        pos = main_map.get_random_free_cell()
        if pos:
            main_map.add_entity(Enemy(*params), pos)
        else:
            print("Недостаточно места для врага")
            break

    # Инициализация pygame
    pygame.init()


    # Загружаем шрифт
    font = pygame.font.SysFont("Arial Black", EL_SIZE)
    font1 = pygame.font.SysFont("Segoe UI Symbol", EL_SIZE)
    tm = 0

    # спрайты
    WEAPONS = {
        "start sword": (3, 0),  # стартовый меч
        "cool sword": (7, 9),  # крутой меч
        "axe": (0, 17),  # топор
        "cool axe": (2, 19),  # крутой топор(лабрис)
        "machete": (11, 8),  # мачете
    }

    POTIONS = {
        "health": (3, 2),  # красное зелье
        "speed": (12, 2)  # синее зелье
    }

    weapons_sprites = load_sprites("assets/weapons.png", 16, WEAPONS)
    potions_sprites = load_sprites("assets/potions.png", 16, POTIONS)

    all_sprites = {}
    all_sprites.update(weapons_sprites)
    all_sprites.update(potions_sprites)

    # Связываем спрайты с icon_path предметов
    all_sprites["icons/weapons/swords/rapira.png"] = weapons_sprites.get("start sword")
    all_sprites["icons/potions/health_potion_small.png"] = potions_sprites.get("health")
    all_sprites["icons/potions/speed_potion_small.png"] = potions_sprites.get("speed")


    inventory = Inventory()

    # Добавляем стартовые предметы через объекты
    inventory.add_item(SWORDS[0])  # Рапира
    inventory.add_item(HEALTH_POTIONS[0])  # Маленькое зелье здоровья x3
    inventory.add_item(HEALTH_POTIONS[0])
    inventory.add_item(HEALTH_POTIONS[0])
    inventory.add_item(SPEED_POTIONS[0])  # Маленькое зелье скорости x2
    inventory.add_item(SPEED_POTIONS[0])

    # Рендерер инвентаря
    renderer = InventoryRenderer(
        screen_width=screen_width,
        screen_height=screen_height,
        sprites_dict=all_sprites
    )

    # Предметы на карте
    map_items_data = [
        SWORDS[0],  # Рапира
        HEALTH_POTIONS[0],  # Зелье здоровья
        SPEED_POTIONS[0],  # Зелье скорости
    ]

    for item in map_items_data:
        x = random.randint(2, main_map.width - 3)
        y = random.randint(2, main_map.height - 3)
        if (x, y) == main_map.player_spawn_point:
            continue
        main_map.item_list.append(MapItem(item, x, y, all_sprites))

    clock = pygame.time.Clock()

    # Переменные для отображения сообщений
    message_text = ""
    message_timer = 0
    message_color = (255, 255, 255)

    music = BackgroundMusic(volume=0.5)

    print( music.load_music(r"background_music.mp3") )
    # print( music.load_music(r"C:\Users\Student\PycharmProjects\GAME_ФЫФЫФЫф\v001\background_music.mp3") )
    music.play()

    floor_img = pygame.image.load("assets/пол.png")
    wall_img = pygame.image.load("assets/Стены.png")
    floor_img = pygame.transform.scale(floor_img, (EL_SIZE, EL_SIZE))
    wall_img = pygame.transform.scale(wall_img, (EL_SIZE, EL_SIZE))

    # Основной игровой цикл
    while True:
        # Заливка
        for y in range(main_map.height):
            for x in range(main_map.width):
                screen.blit(floor_img, (x * EL_SIZE, y * EL_SIZE + GUI_TOP_SIZE))

        # Получение текущего кадра карты
        frame = main_map.render()
        player = main_map.get_MC()

        # Обработка карты
        for y in range(main_map.height):
            for x in range(main_map.width):
                if frame[y][x] == "#":
                    screen.blit(wall_img, (x * EL_SIZE + 10, y * EL_SIZE + 6 + GUI_TOP_SIZE))
                else:
                    color = (255, 255, 255)
                    if frame[y][x] == "ъ":
                        color = (255, 0, 0)

                    # Рисуем буквуaaa
                    text_surface = font.render(frame[y][x], True, color)

                    # entities = main_map.get_entity_xy(x,y)
                    # if entities != None:
                    #     text_surface = pygame.transform.rotate(text_surface, entities.angle)

                    screen.blit(text_surface, (x * EL_SIZE + 10, y * EL_SIZE + GUI_TOP_SIZE))

            # Отрисовка предметов
            for item in main_map.item_list[:]:
                sprite_x = item.x * EL_SIZE + (EL_SIZE - item.sprite.get_width()) // 2
                sprite_y = item.y * EL_SIZE + GUI_TOP_SIZE + (EL_SIZE - item.sprite.get_height()) // 2
                screen.blit(item.sprite, (sprite_x, sprite_y))
                # Обработка подбора и т.п. — тут ваш оставшийся код

            # Отрисовка предметов на карте со спрайтами
            for item in main_map.item_list[:]:  # копируем список для безопасного удаления
                sprite_x = item.x * EL_SIZE + (EL_SIZE - item.sprite.get_width()) // 2
                sprite_y = item.y * EL_SIZE + GUI_TOP_SIZE + (EL_SIZE - item.sprite.get_height()) // 2
                screen.blit(item.sprite, (sprite_x, sprite_y))

                # ПРОВЕРКА ПОДБОРА - когда герой сталкивается с предметом
                if item.x == player.x and item.y == player.y:
                    # Определяем ключ спрайта для этого предмета
                    sprite_key = None
                    name_lower = item.item.name.lower()

                    sprite_mapping = {
                        "меч": "start sword",
                        "лабрис": "cool axe",
                        "зелье здоровья": "health",
                        "зелье скорости": "speed",
                        "мачете": "machete",
                        "крутой меч": "cool sword",
                        "топор": "axe"
                    }

                    name_lower = item.item.name.lower()
                    sprite_key = None

                    for key in sprite_mapping:
                        if key in name_lower:
                            sprite_key = sprite_mapping[key]
                            break

                    # В случае отсутствия совпадения sprite_key останется None, можно оставить как есть или задать значение по умолчанию
                    if sprite_key is None:
                        sprite_key = "default_sprite_key"  # или оставить без изменения

                    # в инвентарь
                    inventory.add_item(item.item.name, sprite_key, 1)

                    # удаление с карты
                    main_map.item_list.remove(item)

                    # сообщение о подборе на экране
                    message_text = f"Подобран: {item.item.name}"
                    message_color = (100, 255, 100)  # зеленый
                    message_timer = 60  # 1 секунда (60 кадров)

        tm += 0.5
        # GUI
        text_surface = font.render("♥" * main_map.get_MC().cur_hp, True, (255, 0, 0))
        screen.blit(text_surface, (10, 0))
        text_surfac = font1.render("\u26A1" * main_map.get_MC().cd_stamina, True, (255, 255, 0))
        screen.blit(text_surfac, (10, 20))

        # Отрисовка инвентаря (теперь передаем player)
        renderer.draw(screen, inventory, player)

        # Отображение сообщения на экране
        if message_timer > 0:
            message_font = pygame.font.SysFont("Arial", 20)
            message_surface = message_font.render(message_text, True, message_color)

            # Позиция сообщения - под полоской HP
            message_x = screen_width // 2 - message_surface.get_width() // 2
            message_y = 30

            # Фон для сообщения
            bg_rect = pygame.Rect(message_x - 10, message_y - 5,
                                  message_surface.get_width() + 20,
                                  message_surface.get_height() + 10)
            pygame.draw.rect(screen, (30, 30, 30), bg_rect)
            pygame.draw.rect(screen, (80, 80, 80), bg_rect, 2)

            screen.blit(message_surface, (message_x, message_y))
            message_timer -= 1

        # Обновление изображения
        pygame.display.flip()

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Открытие/закрытие инвентаря по клавише I
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                inventory.toggle()

            # Использование предметов по цифрам 1-8
            # ТОЛЬКО ЕСЛИ ИНВЕНТАРЬ ЗАКРЫТ
            if event.type == pygame.KEYDOWN and not inventory.is_open:
                # Проверяем сначала на Shift+цифра (выброс предмета)
                if event.mod & pygame.KMOD_SHIFT:
                    if pygame.K_1 <= event.key <= pygame.K_8:
                        index = event.key - pygame.K_1
                        dropped = inventory.drop_item(index)
                        if dropped:
                            name, sprite, count = dropped
                            message_text = f"Выброшено: {name}"
                            message_color = (255, 200, 100)  # желтый для выброса
                            message_timer = 60

                            # Кладем рядом с игроком
                            placed = False
                            # Пробуем разные направления вокруг игрока
                            directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
                            for dx, dy in directions:
                                tx, ty = player.x + dx, player.y + dy
                                if 0 <= tx < main_map.width and 0 <= ty < main_map.height:
                                    # Проверяем, свободно ли место
                                    free = True
                                    for e in main_map.entity_list:
                                        if e.x == tx and e.y == ty:
                                            free = False
                                            break
                                    for it in main_map.item_list:
                                        if it.x == tx and it.y == ty:
                                            free = False
                                            break

                                    if free:
                                        # Ищем ключ спрайта для брошенного предмета
                                        sprite_key = None
                                        for key, spr in all_sprites.items():
                                            if spr is sprite:
                                                sprite_key = key
                                                break

                                        # Создаем предмет на карте
                                        item_obj = Item(name)
                                        map_item = MapItem(item_obj, tx, ty, all_sprites)
                                        main_map.item_list.append(map_item)
                                        placed = True
                                        break

                            if not placed:
                                message_text = f"Нет места для {name}!"
                                message_color = (255, 100, 100)
                                message_timer = 60
                                # Возвращаем предмет обратно в инвентарь
                                inventory.add_item(name, None, count)
                            continue  # Важно: пропускаем дальнейшую обработку этой цифры

                # Обычное использование предметов по цифрам (без Shift)
                elif pygame.K_1 <= event.key <= pygame.K_8:
                    index = event.key - pygame.K_1
                    # Используем предмет и получаем сообщение от инвентаря
                    used, item_message = inventory.use_item(index, player)

                    if item_message:
                        message_text = item_message
                        if "HP уже полное" in item_message or "полное" in item_message.lower():
                            message_color = (255, 100, 100)  # красный для ошибки
                        elif "использован" in item_message.lower() or "+" in item_message or "экипировано" in item_message or "надето" in item_message:
                            message_color = (100, 200, 255)  # синий для успеха
                        else:
                            message_color = (255, 200, 100)  # желтый для других
                        message_timer = 60

        # Обработка нажатий клавы
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE ] == 1:
            if (datetime.now() - last_gnagatie2 ).total_seconds() > 2:
                last_gnagatie2 = datetime.now()
                main_map.get_MC().desh(main_map)
                main_map.get_MC().regeniration_stamina(2)
        if keys[pygame.K_w] == 1:
            main_map.entity_move(0, 0, -1)
        if keys[pygame.K_s] == 1:
            main_map.entity_move(0, 0, 1)
        if keys[pygame.K_a] == 1:
            main_map.entity_move(0, -1, 0)
        if keys[pygame.K_d] == 1:
            main_map.entity_move(0, 1, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                main_map.get_MC().atack(main_map)
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 2:
        #         main_map.get_MC().block(main_map)
        if keys[pygame.K_LALT] == 1:
            if (datetime.now() - last_gnagatie).total_seconds() > 1 :
                last_gnagatie = datetime.now()
                main_map.get_MC().stamina()
                main_map.get_MC().regeniration_stamina(1)

        # Обновление эффектов предметов
        effect_message = inventory.update_effects(player)
        if effect_message:
            message_text = effect_message
            message_color = (255, 200, 100)  # оранжевый
            message_timer = 60

        # Обработка противников
        manager.tick()
