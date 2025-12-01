from map import Map
from entity import Entity
from enemy_manager import EnemyManager,Enemy
import pygame

if __name__ == "__main__":
    # Размер одного элемента
    EL_SIZE = 25
    GUI_TOP_SIZE = 50

    # Создаем карту
    main_map = Map(30, 25, (10, 10))

    #Создаем менеджера противников
    manager = EnemyManager(main_map)

    # Создаем существо-игрока
    main_map.add_entity(
        Entity(10, 10, (0, 0), 10, 'ь'),
        main_map.player_spawn_point
    )
    main_map.add_entity(
        Enemy(10, 7, (0, 0), 10, 'ъ'),
        (20, 20)
    )

    main_map.add_entity(
        Enemy(10, 7, (0, 0), 10, 'ъ'),
        (19, 20)
    )

    # Инициализация pygame
    pygame.init()

    # Создание окна заданной ширины
    screen = pygame.display.set_mode( (main_map.width * EL_SIZE, main_map.height * EL_SIZE + GUI_TOP_SIZE) )

    # Загружаем шрифт
    font = pygame.font.SysFont("Arial Black", EL_SIZE)
    tm = 0
    # Основной игровой цикл
    while True:
        # Заливка
        screen.fill( (0, 0, 0) )

        # Получение текущего кадра карты
        frame = main_map.render()

        # Обработка карты
        for y in range(main_map.height):
            for x in range(main_map.width):
                if frame[y][x] == "#":
                    # Рисуем квадрат
                    pygame.draw.rect(screen, (100, 100, 100), [x * EL_SIZE, y * EL_SIZE + GUI_TOP_SIZE, EL_SIZE, EL_SIZE])
                else:
                    color = (255, 255, 255)
                    if frame[y][x] == "ъ":
                        color = (255, 0, 0)

                    # Рисуем букву
                    text_surface = font.render(frame[y][x], True, color)

                    # entity = main_map.get_entity_xy(x,y)
                    # if entity != None:
                    #     text_surface = pygame.transform.rotate(text_surface, entity.angle)

                    screen.blit(text_surface, (x * EL_SIZE + 10, y * EL_SIZE  + GUI_TOP_SIZE))

        tm += 0.5
        # GUI
        text_surface = font.render("♥" * main_map.get_MC().cur_hp , True, (255, 0, 0))
        screen.blit(text_surface, (10, 0))

        # Обновление изображения
        pygame.display.flip()

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Обработка нажатий клавы
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] == 1:
            main_map.entity_move(0,0, -1)
        if keys[pygame.K_s] == 1:
            main_map.entity_move(0,0, 1)
        if keys[pygame.K_a] == 1:
            main_map.entity_move(0, -1, 0)
        if keys[pygame.K_d] == 1:
            main_map.entity_move(0,1, 0)

        #Обработка противников
        manager.tick()





