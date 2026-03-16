import pygame
from datetime import datetime, timedelta


class Inventory:
    def __init__(self, screen_width: int, screen_height: int, sprites_dict: dict = None):
        self.items = []
        self.sprites = sprites_dict or {}
        self.is_open = False

        # Хотбар (всегда внизу) - 9 ячеек для ровности
        self.hotbar_cell_size = 40
        self.hotbar_cells = 9
        self.hotbar_spacing = 5

        # Расчет позиции хотбара - ровно по центру внизу
        hotbar_total_width = (self.hotbar_cells * self.hotbar_cell_size +
                              (self.hotbar_cells - 1) * self.hotbar_spacing)
        self.hotbar_x = (screen_width - hotbar_total_width) // 2
        self.hotbar_y = screen_height - self.hotbar_cell_size - 10

        # Инвентарь (точные размеры)
        self.cell_size = 50
        self.inventory_cols = 9
        self.inventory_rows = 3
        self.hotbar_in_inventory_cells = 9

        # Слоты брони
        self.armor_slots = 4
        self.armor_cell_size = 50

        # Расчеты размеров
        self.left_panel_width = 150
        self.right_panel_width = self.inventory_cols * self.cell_size

        self.panel_spacing = 20
        self.side_padding = 20

        self.total_inventory_width = (
            self.side_padding * 2 +
            self.left_panel_width +
            self.panel_spacing +
            self.right_panel_width
        )

        self.header_height = 40
        self.player_area_height = 100
        self.armor_spacing = 20  # увеличено расстояние между броневыми слотами
        self.armor_title_height = 30
        self.armor_area_height = (
            self.armor_title_height +
            (self.armor_slots * self.armor_cell_size) +
            (self.armor_slots - 1) * self.armor_spacing +
            20
        )
        self.inventory_row_spacing = 10
        self.inventory_area_height = (
            (self.inventory_rows + 1) * self.cell_size +
            self.inventory_rows * self.inventory_row_spacing
        )
        self.total_inventory_height = (
            self.header_height +
            max(self.player_area_height + self.armor_area_height, self.inventory_area_height) +
            40
        )

        # Расчет позиций
        self.inventory_x = (screen_width - self.total_inventory_width) // 2
        self.inventory_y = (screen_height - self.total_inventory_height) // 2

        self.left_panel_x = self.inventory_x + self.side_padding
        self.right_panel_x = self.left_panel_x + self.left_panel_width + self.panel_spacing
        self.header_y = self.inventory_y + 20
        self.player_area_y = self.header_y + self.header_height + 10
        self.armor_start_y = self.player_area_y + self.player_area_height + 10 + self.armor_title_height
        self.inventory_start_y = self.player_area_y

        # Позиции для брони (поднимаем на 5 пикселей вверх)
        self.armor_positions = []
        current_armor_y = self.armor_start_y - 5
        for i in range(self.armor_slots):
            x = self.left_panel_x + (self.left_panel_width - self.armor_cell_size) // 2
            self.armor_positions.append((x, current_armor_y))
            current_armor_y += self.armor_cell_size + self.armor_spacing

        self.armor_names = ["Шлем", "Нагрудник", "Поножи", "Ботинки"]

    def add_item(self, name: str, sprite_key: str = None, count: int = 1):
        if sprite_key is None:
            name_lower = name.lower()
            # Словарь соответствий для поиска по ключевым словам
            item_map = {

                # ===== МЕЧИ =====
                "рапира": "sword_rapira",
                "сабля": "sword_sablia",
                "надежда королевства": "sword_hope_of_kingdom",
                "меч": "start sword",
                "крутой меч": "cool sword",

                # ===== ТОПОРЫ =====
                "одноручный топор": "axe_one_handed",
                "двуручный топор": "axe_two_handed",
                "костолом": "axe_bonebreaker",
                "топор дровосека": "axe",
                "топор": "cool axe",
                "лабрис": "cool axe",

                # ===== КОСЫ =====
                "коса": "scythe_basic",
                "жнец": "scythe_reaper",
                "собиратель душ": "scythe_soul_harvester",

                # ===== ЗЕЛЬЯ ЗДОРОВЬЯ =====
                "маленькое зелье здоровья": "small_health_potion",
                "среднее зелье здоровья": "medium_health_potion",
                "большое зелье здоровья": "big_health_potion",
                "зелье здоровья": "health",

                # ===== ЗЕЛЬЯ СКОРОСТИ =====
                "маленькое зелье скорости": "small_speed_potion",
                "среднее зелье скорости": "medium_speed_potion",
                "большое зелье скорости": "big_speed_potion",
                "зелье скорости": "speed",

                # ===== ЗЕЛЬЯ ВЫНОСЛИВОСТИ =====
                "маленькое зелье выносливости": "small_stamina_potion",
                "среднее зелье выносливости": "medium_stamina_potion",
                "большое зелье выносливости": "big_stamina_potion",

                # ===== ПРОЧЕЕ =====
                "мачете": "machete",
            }

            # Проходим по словарю и ищем ключевое слово
            sprite_key_found = None
            for key_word, sprite_name in item_map.items():
                if key_word in name_lower:
                    sprite_key_found = sprite_name
                    break

            sprite_key = sprite_key_found

        # Далее логика добавления предмета по выбранному sprite_key
        sprite = None
        if sprite_key and sprite_key in self.sprites:
            sprite = self.sprites[sprite_key]
        else:
            sprite = pygame.Surface((32, 32), pygame.SRCALPHA)
            sprite.fill((0, 0, 0, 0))
        # остальной код добавления предмета остаётся без изменений
        for i, (existing_name, existing_sprite, existing_count) in enumerate(self.items):
            if existing_name == name and existing_sprite is sprite:
                self.items[i] = (name, sprite, existing_count + count)
                return
        self.items.append((name, sprite, count))

    def toggle(self):
        self.is_open = not self.is_open

    def drop_item(self, index: int):
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        return None

    def use_item(self, index: int, player):
        if not (0 <= index < len(self.items)):
            return False, "Нет предмета в этой ячейке"

        name, sprite, count = self.items[index]
        name_lower = name.lower()

        if "зелье" in name_lower:
            if "здор" in name_lower:
                if player.cur_hp < player.max_hp:
                    old_hp = player.cur_hp
                    player.cur_hp = min(player.cur_hp + 2, player.max_hp)
                    healed = player.cur_hp - old_hp
                    message = f"{name}: HP +{healed}"
                    count -= 1
                    if count <= 0:
                        self.items.pop(index)
                    else:
                        self.items[index] = (name, sprite, count)
                    return True, message
                else:
                    return False, "HP уже полное!"
            elif "скор" in name_lower:
                if not hasattr(player, 'original_speed'):
                    player.original_speed = player.speed
                player.speed = player.original_speed + 3
                player.speed_boost_end = datetime.now() + timedelta(seconds=5)
                message = f"{name}: скорость +3 на 5 сек"
                count -= 1
                if count <= 0:
                    self.items.pop(index)
                else:
                    self.items[index] = (name, sprite, count)
                return True, message
            return None

        elif "меч" in name_lower or "топор" in name_lower or "лабрис" in name_lower or "мачете" in name_lower:
            message = f"{name}: экипировано"
            return True, message
        elif "шлем" in name_lower or "нагрудник" in name_lower or "поножи" in name_lower or "ботинки" in name_lower or "сапоги" in name_lower:
            message = f"{name}: надето"
            return True, message
        else:
            message = f"{name}: нельзя использовать"
            return False, message

    def update_effects(self, player):
        if hasattr(player, 'speed_boost_end'):
            if datetime.now() > player.speed_boost_end:
                if hasattr(player, 'original_speed'):
                    player.speed = player.original_speed
                    delattr(player, 'speed_boost_end')
                    delattr(player, 'original_speed')
                    return "Эффект скорости закончился!"
        return None

    def draw_hotbar(self, screen: pygame.Surface):
        for i in range(self.hotbar_cells):
            x = self.hotbar_x + i * (self.hotbar_cell_size + self.hotbar_spacing)
            y = self.hotbar_y
            rect = pygame.Rect(x, y, self.hotbar_cell_size, self.hotbar_cell_size)
            pygame.draw.rect(screen, (100, 100, 100), rect)
            pygame.draw.rect(screen, (50, 50, 50), rect, 2)
            font = pygame.font.Font(None, 16)
            num_text = font.render(str(i + 1), True, (200, 200, 200))
            screen.blit(num_text, (x + 3, y + 3))
            if i < len(self.items):
                _, sprite, count = self.items[i]
                if sprite.get_alpha() is not None:
                    scaled_sprite = pygame.transform.scale(sprite,
                                                           (self.hotbar_cell_size - 10, self.hotbar_cell_size - 10))
                    sprite_x = x + (self.hotbar_cell_size - scaled_sprite.get_width()) // 2
                    sprite_y = y + (self.hotbar_cell_size - scaled_sprite.get_height()) // 2
                    screen.blit(scaled_sprite, (sprite_x, sprite_y))
                if count > 1:
                    count_font = pygame.font.Font(None, 18)
                    count_text = count_font.render(str(count), True, (255, 255, 0))
                    screen.blit(count_text, (x + self.hotbar_cell_size - 20, y + self.hotbar_cell_size - 20))

    def draw_inventory(self, screen: pygame.Surface, player):
        if not self.is_open:
            return
        overlay = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))
        bg_rect = pygame.Rect(self.inventory_x, self.inventory_y,
                              self.total_inventory_width, self.total_inventory_height)
        pygame.draw.rect(screen, (30, 30, 40), bg_rect)
        pygame.draw.rect(screen, (60, 60, 80), bg_rect, 3)
        font = pygame.font.Font(None, 36)


        # левая панель
        player_box_y = self.player_area_y
        player_box_width = self.left_panel_width - 20
        player_box_height = 90
        player_box_rect = pygame.Rect(self.left_panel_x + 10, player_box_y, player_box_width, player_box_height)
        pygame.draw.rect(screen, (40, 40, 50), player_box_rect)
        pygame.draw.rect(screen, (80, 80, 100), player_box_rect, 2)

        # "Персонаж" заголовок
        player_font = pygame.font.Font(None, 24)
        player_text = player_font.render("Персонаж", True, (200, 220, 255))
        player_text_x = self.left_panel_x + (self.left_panel_width - player_text.get_width()) // 2
        screen.blit(player_text, (player_text_x, player_box_y - 25))

        # слот персонажа с символом '@'
        player_slot_x = self.left_panel_x + (self.left_panel_width - self.armor_cell_size) // 2
        player_slot_y = player_box_y + (player_box_height - self.armor_cell_size) // 2
        player_rect = pygame.Rect(player_slot_x, player_slot_y, self.armor_cell_size, self.armor_cell_size)
        pygame.draw.rect(screen, (50, 50, 60), player_rect)
        pygame.draw.rect(screen, (90, 90, 110), player_rect, 2)
        font_char = pygame.font.Font(None, 32)
        char_symbol = font_char.render("ь", True, (50, 150, 255))
        char_x = player_slot_x + (self.armor_cell_size - char_symbol.get_width()) // 2
        char_y = player_slot_y + (self.armor_cell_size - char_symbol.get_height()) // 2
        screen.blit(char_symbol, (char_x, char_y))

        # "Броня" заголовок
        armor_title_y = player_box_y + player_box_height + 15
        armor_title = player_font.render("Броня", True, (200, 220, 255))
        armor_title_x = self.left_panel_x + (self.left_panel_width - armor_title.get_width()) // 2
        screen.blit(armor_title, (armor_title_x, armor_title_y))

        # слоты брони под заголовком "Броня"
        for i in range(self.armor_slots):
            x, y = self.armor_positions[i]
            slot_rect = pygame.Rect(x, y, self.armor_cell_size, self.armor_cell_size)
            pygame.draw.rect(screen, (40, 40, 50), slot_rect)
            pygame.draw.rect(screen, (80, 80, 100), slot_rect, 2)
            name_font = pygame.font.Font(None, 20)
            name_text = name_font.render(self.armor_names[i], True, (180, 180, 200))
            name_x = x + (self.armor_cell_size - name_text.get_width()) // 2
            name_y = y + self.armor_cell_size + 2
            screen.blit(name_text, (name_x, name_y))

        # правая панель
        inv_font = pygame.font.Font(None, 24)
        inv_text = inv_font.render("ИНВЕНТАРЬ", True, (200, 220, 255))
        inv_text_x = self.right_panel_x + (self.right_panel_width - inv_text.get_width()) // 2
        screen.blit(inv_text, (inv_text_x, self.player_area_y - 25))

        # инвентарь + хотбар
        current_y = self.inventory_start_y
        for row in range(self.inventory_rows + 1):
            is_hotbar_row = (row == self.inventory_rows)
            for col in range(self.inventory_cols):
                x = self.right_panel_x + col * self.cell_size
                y = current_y
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                bg_color = (50, 50, 60) if is_hotbar_row else (40, 40, 50)
                border_color = (90, 90, 110) if is_hotbar_row else (80, 80, 100)
                pygame.draw.rect(screen, bg_color, rect)
                pygame.draw.rect(screen, border_color, rect, 2)
                if is_hotbar_row:
                    num_font = pygame.font.Font(None, 16)
                    num_text = num_font.render(str(col + 1), True, (200, 200, 200))
                    screen.blit(num_text, (x + 5, y + 5))
            current_y += self.cell_size + self.inventory_row_spacing

        # предметы в хотбаре
        hotbar_y = self.inventory_start_y + self.inventory_rows * (self.cell_size + self.inventory_row_spacing)
        for i in range(self.hotbar_in_inventory_cells):
            if i >= len(self.items):
                break
            x = self.right_panel_x + i * self.cell_size
            y = hotbar_y
            name, sprite, count = self.items[i]
            if sprite.get_alpha() is not None:
                scaled_sprite = pygame.transform.scale(sprite, (self.cell_size - 10, self.cell_size - 10))
                sprite_x = x + (self.cell_size - scaled_sprite.get_width()) // 2
                sprite_y = y + (self.cell_size - scaled_sprite.get_height()) // 2
                screen.blit(scaled_sprite, (sprite_x, sprite_y))
            if count > 1:
                count_font = pygame.font.Font(None, 18)
                count_text = count_font.render(str(count), True, (255, 255, 0))
                screen.blit(count_text, (x + self.cell_size - 20, y + self.cell_size - 20))

        # остальной инвентарь
        for row in range(self.inventory_rows):
            y = self.inventory_start_y + row * (self.cell_size + self.inventory_row_spacing)
            for col in range(self.inventory_cols):
                idx = 9 + (row * self.inventory_cols) + col
                if idx >= len(self.items):
                    continue
                x = self.right_panel_x + col * self.cell_size
                name, sprite, count = self.items[idx]
                if sprite.get_alpha() is not None:
                    scaled_sprite = pygame.transform.scale(sprite, (self.cell_size - 10, self.cell_size - 10))
                    sprite_x = x + (self.cell_size - scaled_sprite.get_width()) // 2
                    sprite_y = y + (self.cell_size - scaled_sprite.get_height()) // 2
                    screen.blit(scaled_sprite, (sprite_x, sprite_y))
                if count > 1:
                    count_font = pygame.font.Font(None, 18)
                    count_text = count_font.render(str(count), True, (255, 255, 0))
                    screen.blit(count_text, (x + self.cell_size - 20, y + self.cell_size - 20))

    def draw(self, screen: pygame.Surface, player=None):
        self.draw_hotbar(screen)
        if self.is_open and player:
            self.draw_inventory(screen, player)
