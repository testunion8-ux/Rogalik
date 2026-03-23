import pygame
from inventory import Inventory
from item import Item
from weapon import Weapon
from armor import Armor
from consumable import Consumable


class InventoryRenderer:
    # Цвета
    COLOR_BG = (30,  30,  40)
    COLOR_BG_BORDER = (60,  60,  80)
    COLOR_CELL = (40,  40,  50)
    COLOR_CELL_HOTBAR = (50,  50,  60)
    COLOR_BORDER = (80,  80, 100)
    COLOR_BORDER_HOT = (90,  90, 110)
    COLOR_TITLE = (255, 255, 200)
    COLOR_LABEL = (200, 220, 255)
    COLOR_COUNT = (255, 255,   0)
    COLOR_OVERLAY = (0,   0,   0, 180)
    COLOR_RARITY_DEFAULT = (200, 200, 200)

    def __init__(self, screen_width: int, screen_height: int, sprites_dict: dict = None):
        self.sprites = sprites_dict or {}
        self._build_layout(screen_width, screen_height)

    def _build_layout(self, sw: int, sh: int):
        # Хотбар
        self.hotbar_cell_size = 40
        self.hotbar_cells = 9
        self.hotbar_spacing = 5
        hotbar_total_w = (self.hotbar_cells * self.hotbar_cell_size +
                          (self.hotbar_cells - 1) * self.hotbar_spacing)
        self.hotbar_x = (sw - hotbar_total_w) // 2
        self.hotbar_y = sh - self.hotbar_cell_size - 10

        # Панель инвентаря
        self.cell_size = 50
        self.inv_cols = 9
        self.inv_rows = 3
        self.armor_slots = 4
        self.armor_cell_size = 50
        self.armor_spacing = 20

        left_panel_w = 150
        right_panel_w = self.inv_cols * self.cell_size
        panel_spacing = 20
        side_padding = 20
        header_h = 40
        player_area_h = 100
        armor_title_h = 30
        row_spacing = 10

        armor_area_h = (armor_title_h +
                        self.armor_slots * self.armor_cell_size +
                        (self.armor_slots - 1) * self.armor_spacing + 20)
        inv_area_h = ((self.inv_rows + 1) * self.cell_size +
                        self.inv_rows * row_spacing)

        total_w = side_padding * 2 + left_panel_w + panel_spacing + right_panel_w
        total_h = (header_h +
                   max(player_area_h + armor_area_h, inv_area_h) + 40)

        self.inv_x = (sw - total_w) // 2
        self.inv_y = (sh - total_h) // 2

        self.left_x = self.inv_x + side_padding
        self.right_x = self.left_x + left_panel_w + panel_spacing
        self.header_y = self.inv_y + 20
        self.player_y = self.header_y + header_h + 10
        self.inv_start_y = self.player_y

        armor_title_y = self.player_y + player_area_h + 15
        armor_start_y = armor_title_y + armor_title_h - 5

        self.armor_positions = []
        ay = armor_start_y
        for _ in range(self.armor_slots):
            x = self.left_x + (left_panel_w - self.armor_cell_size) // 2
            self.armor_positions.append((x, ay))
            ay += self.armor_cell_size + self.armor_spacing

        self.armor_names = ["Шлем", "Нагрудник", "Перчатки", "Ботинки"]

        self.total_w = total_w
        self.total_h = total_h
        self.left_panel_w = left_panel_w
        self.right_panel_w = right_panel_w
        self.row_spacing = row_spacing
        self._armor_title_y = armor_title_y
        self._player_area_h = player_area_h

    def draw(self, screen: pygame.Surface, inventory: Inventory, player=None):
        self._draw_hotbar(screen, inventory)
        if inventory.is_open:
            self._draw_panel(screen, inventory, player)

    def _draw_hotbar(self, screen: pygame.Surface, inventory: Inventory):
        font_num = pygame.font.Font(None, 16)
        for i in range(self.hotbar_cells):
            x = self.hotbar_x + i * (self.hotbar_cell_size + self.hotbar_spacing)
            y = self.hotbar_y
            rect = pygame.Rect(x, y, self.hotbar_cell_size, self.hotbar_cell_size)
            pygame.draw.rect(screen, (100, 100, 100), rect)
            pygame.draw.rect(screen, (50,  50,  50),  rect, 2)
            num_surf = font_num.render(str(i + 1), True, (200, 200, 200))
            screen.blit(num_surf, (x + 3, y + 3))

            if i < len(inventory.items):
                item = inventory.items[i]
                self._blit_item_sprite(screen, item, x, y,
                                       self.hotbar_cell_size, self.hotbar_cell_size)

    def _draw_panel(self, screen: pygame.Surface, inventory: Inventory, player):
        # Полупрозрачный оверлей
        overlay = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        overlay.fill(self.COLOR_OVERLAY)
        screen.blit(overlay, (0, 0))

        # Фон панели
        bg = pygame.Rect(self.inv_x, self.inv_y, self.total_w, self.total_h)
        pygame.draw.rect(screen, self.COLOR_BG,        bg)
        pygame.draw.rect(screen, self.COLOR_BG_BORDER, bg, 3)

        # Заголовок
        font_title = pygame.font.Font(None, 36)
        title = font_title.render("ИНВЕНТАРЬ", True, self.COLOR_TITLE)
        tx = self.inv_x + (self.total_w - title.get_width()) // 2
        screen.blit(title, (tx, self.header_y))

        self._draw_left_panel(screen, inventory)
        self._draw_right_panel(screen, inventory)

    def _draw_left_panel(self, screen: pygame.Surface, inventory: Inventory):
        font = pygame.font.Font(None, 24)

        # Блок персонажа
        pb_rect = pygame.Rect(self.left_x + 10, self.player_y,
                              self.left_panel_w - 20, self._player_area_h)
        pygame.draw.rect(screen, (40, 40, 50), pb_rect)
        pygame.draw.rect(screen, (80, 80, 100), pb_rect, 2)

        lbl = font.render("Персонаж", True, self.COLOR_LABEL)
        lbl_x = self.left_x + (self.left_panel_w - lbl.get_width()) // 2
        screen.blit(lbl, (lbl_x, self.player_y - 25))

        # Слот "@"
        slot_x = self.left_x + (self.left_panel_w - self.armor_cell_size) // 2
        slot_y = self.player_y + (self._player_area_h - self.armor_cell_size) // 2
        slot_r = pygame.Rect(slot_x, slot_y, self.armor_cell_size, self.armor_cell_size)
        pygame.draw.rect(screen, (50, 50, 60), slot_r)
        pygame.draw.rect(screen, (90, 90, 110), slot_r, 2)
        char_font = pygame.font.Font(None, 32)
        sym = char_font.render("@", True, (50, 150, 255))
        screen.blit(sym, (slot_x + (self.armor_cell_size - sym.get_width())  // 2,
                          slot_y + (self.armor_cell_size - sym.get_height()) // 2))

        # Заголовок "Броня"
        armor_lbl = font.render("Броня", True, self.COLOR_LABEL)
        alx = self.left_x + (self.left_panel_w - armor_lbl.get_width()) // 2
        screen.blit(armor_lbl, (alx, self._armor_title_y))

        # Слоты брони
        for i, (ax, ay) in enumerate(self.armor_positions):
            slot_rect = pygame.Rect(ax, ay, self.armor_cell_size, self.armor_cell_size)
            pygame.draw.rect(screen, (40, 40, 50), slot_rect)
            pygame.draw.rect(screen, (80, 80, 100), slot_rect, 2)

            # Если надета броня — рисуем спрайт
            slot_type = ["helmet", "chest", "gloves", "boots"][i]
            equipped = inventory.equipped_armor.get(slot_type)
            if equipped:
                self._blit_item_sprite(screen, equipped, ax, ay,
                                       self.armor_cell_size, self.armor_cell_size)

            name_font = pygame.font.Font(None, 20)
            name_s = name_font.render(self.armor_names[i], True, (180, 180, 200))
            screen.blit(name_s, (ax + (self.armor_cell_size - name_s.get_width()) // 2,
                                 ay + self.armor_cell_size + 2))

    def _draw_right_panel(self, screen: pygame.Surface, inventory: Inventory):
        font = pygame.font.Font(None, 24)

        # Заголовок правой панели
        lbl = font.render("ИНВЕНТАРЬ", True, self.COLOR_LABEL)
        lx = self.right_x + (self.right_panel_w - lbl.get_width()) // 2
        screen.blit(lbl, (lx, self.player_y - 25))

        cs  = self.cell_size
        rsp = self.row_spacing

        # Рисуем сетку ячеек (3 строки + хотбар-строка)
        cur_y = self.inv_start_y
        for row in range(self.inv_rows + 1):
            is_hotbar = (row == self.inv_rows)
            for col in range(self.inv_cols):
                x = self.right_x + col * cs
                rect = pygame.Rect(x, cur_y, cs, cs)
                bg  = self.COLOR_CELL_HOTBAR if is_hotbar else self.COLOR_CELL
                brd = self.COLOR_BORDER_HOT  if is_hotbar else self.COLOR_BORDER
                pygame.draw.rect(screen, bg,  rect)
                pygame.draw.rect(screen, brd, rect, 2)
                if is_hotbar:
                    nf = pygame.font.Font(None, 16)
                    ns = nf.render(str(col + 1), True, (200, 200, 200))
                    screen.blit(ns, (x + 5, cur_y + 5))
            cur_y += cs + rsp

        # Рисуем предметы в хотбар-строке
        hotbar_y = self.inv_start_y + self.inv_rows * (cs + rsp)
        for i in range(self.hotbar_cells):
            if i >= len(inventory.items):
                break
            x = self.right_x + i * cs
            self._blit_item_sprite(screen, inventory.items[i], x, hotbar_y, cs, cs)

        # Рисуем остальные предметы
        for row in range(self.inv_rows):
            y = self.inv_start_y + row * (cs + rsp)
            for col in range(self.inv_cols):
                idx = 9 + row * self.inv_cols + col
                if idx >= len(inventory.items):
                    continue
                x = self.right_x + col * cs
                self._blit_item_sprite(screen, inventory.items[idx], x, y, cs, cs)

    def _blit_item_sprite(self, screen: pygame.Surface, item: Item,
                          cell_x: int, cell_y: int, cell_w: int, cell_h: int):
        sprite = self._get_sprite(item)
        if sprite:
            img_w = cell_w - 10
            img_h = cell_h - 10
            scaled = pygame.transform.scale(sprite, (img_w, img_h))
            sx = cell_x + (cell_w - scaled.get_width())  // 2
            sy = cell_y + (cell_h - scaled.get_height()) // 2
            screen.blit(scaled, (sx, sy))
        else:
            # Заглушка: квадрат цвета редкости + первые буквы
            color = item.rarity.color if hasattr(item, "rarity") else self.COLOR_RARITY_DEFAULT
            stub = pygame.Surface((cell_w - 10, cell_h - 10))
            stub.fill(color)
            font = pygame.font.Font(None, 18)
            txt = font.render(item.name[:4], True, (0, 0, 0))
            stub.blit(txt, (2, (stub.get_height() - txt.get_height()) // 2))
            screen.blit(stub, (cell_x + 5, cell_y + 5))

        # Счётчик стака
        if item.is_stackable and item.quantity > 1:
            font = pygame.font.Font(None, 18)
            cnt = font.render(str(item.quantity), True, self.COLOR_COUNT)
            screen.blit(cnt, (cell_x + cell_w - 20, cell_y + cell_h - 20))

    def _get_sprite(self, item: Item) -> pygame.Surface | None:
        # Сначала по прямому пути
        if item.icon_path and item.icon_path in self.sprites:
            return self.sprites[item.icon_path]
        # Потом по item_id
        if item.item_id in self.sprites:
            return self.sprites[item.item_id]
        return None
