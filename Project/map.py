import random
import networkx as nx
from datetime import datetime, timedelta



class Map:
    map_array = []
    entity_list = []
    old_path  = None
    vremy =  datetime.now()
    def __init__(self, width: int, height: int, player_spawn_point: tuple):
        self.player_spawn_point = player_spawn_point
        self.height = height
        self.width = width
        self.item_list = []  # для предметов на карте

        self.generate()

    def add_entity(self, entity, coords: tuple):
        entity.coords = list(coords)
        self.entity_list.append(entity)

    def create_room(self, room):
        x1, y1 = room["x"], room["y"]
        x2, y2 = x1 + room["width"], y1 + room["height"]

        is_left = (x1 == 1)  # левая
        is_right = (x2 == self.width - 1)  # правая
        is_top = (y1 == 1)  # верхняя
        is_bottom = (y2 == self.height - 1)  # нижная

        for y in range(y1, y2):
            for x in range(x1, x2):
                if 0 <= y < self.height and 0 <= x < self.width:
                    self.map_array[y][x] = "#"

        for y in range(y1 + 1, y2 - 1):
            for x in range(x1 + 1, x2 - 1):
                if 0 <= y < self.height and 0 <= x < self.width:
                    self.map_array[y][x] = " "
        if is_top:
            for x in range(x1, x2):
                switch = False
                if x == x1 and not is_left:
                    switch = True
                elif x == x2 - 1 and not is_right:
                    switch = True

                self.map_array[y1][x] = "#" if switch else " "

        if is_bottom:
            for x in range(x1, x2):
                switch = False
                if x == x1 and not is_left:
                    switch = True
                elif x == x2 - 1 and not is_right:
                    switch = True

                self.map_array[y2 - 1][x] = "#" if switch else " "

        if is_left:
            for y in range(y1, y2):
                switch = False
                if y == y1 and not is_top:
                    switch = True
                elif y == y2 - 1 and not is_bottom:
                    switch = True

                self.map_array[y][x1] = "#" if switch else " "

        if is_right:
            for y in range(y1, y2):
                switch = False
                if y == y1 and not is_top:
                    switch = True
                elif y == y2 - 1 and not is_bottom:
                    switch = True

                self.map_array[y][x2 - 1] = "#" if switch else " "

    def Grah(self,mapi):
        spisik = []
        en = {(e.x, e.y) for e in self.entity_list}
        for y in range(self.height):
            for x in range(self.width):
                if mapi[y][x] == " " and (x,y) not  in en :
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx_, ny_ = x + dx, y + dy
                        if 0 <= nx_ < self.width and 0 <= ny_ < self.height:
                            if mapi[ny_][nx_] == " ":
                                spisik.append(((x, y), (nx_, ny_), 1))


        g = nx.Graph()
        g.add_weighted_edges_from(spisik)
        return g

    def path(self,map,start, target):
        try:
            g = map.Grah(self.map_array)
            path = nx.dijkstra_path(g, start, target, weight="weight")
            self.old_path = path
            return path
        except nx.NetworkXNoPath:
            return None
        except  nx.NodeNotFound:
            return  None
    def create_door(self, room, room_index):
        x1, y1 = room["x"], room["y"]
        x2, y2 = x1 + room["width"], y1 + room["height"]

        walls = []

        if room_index == 0:
            walls = ["right", "bottom"]
        elif room_index == 1:
            walls = ["left", "bottom"]
        elif room_index == 2:
            walls = ["right", "top"]
        elif room_index == 3:
            walls = ["left", "top"]

        wall_door = random.choice(walls)

        if wall_door == "top":
            middle = x1 + (x2 - x1) // 2
            self.map_array[y1][middle - 1] = " "
            self.map_array[y1][middle] = " "

        elif wall_door == "bottom":
            middle = x1 + (x2 - x1) // 2
            self.map_array[y2 - 1][middle - 1] = " "
            self.map_array[y2 - 1][middle] = " "

        elif wall_door == "left":
            middle = y1 + (y2 - y1) // 2
            self.map_array[middle - 1][x1] = " "
            self.map_array[middle][x1] = " "

        elif wall_door == "right":
            middle = y1 + (y2 - y1) // 2
            self.map_array[middle - 1][x2 - 1] = " "
            self.map_array[middle][x2 - 1] = " "

    def entity_move_desh(self, entity_idx, x, y):
        current_entity = self.entity_list[entity_idx]
        if x == -1:
            current_entity.direct = [-1, 0]
        elif x == 1:
            current_entity.direct = [1, 0]

        if y == -1:
            current_entity.direct = [0, -1]
        elif y == 1:
            current_entity.direct = [0, 1]

        current_entity.add_coords(x, y)



    def generate(self):
        # Перезапись карты\очищение
        for y in range(self.height):
            self.map_array.append([])
            for x in range(self.width):
                if x == 0 or x == self.width - 1 \
                        or y == 0 or y == self.height - 1:
                    self.map_array[y].append("#")
                else:
                    self.map_array[y].append(" ")

        mid_x = self.width // 2
        mid_y = self.height // 2

        rooms = [
            {"x": 1, "y": 1, "width": mid_x - 2, "height": mid_y - 2},
            {"x": mid_x + 1, "y": 1, "width": self.width - mid_x - 2, "height": mid_y - 2},
            {"x": 1, "y": mid_y + 1, "width": mid_x - 2, "height": self.height - mid_y - 2},
            {"x": mid_x + 1, "y": mid_y + 1, "width": self.width - mid_x - 2, "height": self.height - mid_y - 2}
        ]

        corridor_idx = random.randint(0, 3)

        for i, room in enumerate(rooms):
            if i != corridor_idx:
                self.create_room(room)
                self.create_door(room, i)

    def render(self):
        output_frame = [row[:] for row in self.map_array]

        for entity in self.entity_list:
            output_frame[entity.y][entity.x] = entity.sign

        return output_frame

    def entity_move(self, entity_idx, x, y):
        current_entity = self.entity_list[entity_idx]
        way_x = current_entity.x + x
        way_y = current_entity.y + y

        if x == -1:
            current_entity.direct = [-1, 0]
        elif x == 1:
            current_entity.direct = [1, 0]

        if y == -1:
            current_entity.direct = [0, -1]
        elif y == 1:
            current_entity.direct = [0, 1]

        is_busy = False

        for entity in self.entity_list:
            if entity.x == way_x and entity.y == way_y:
                is_busy = True
                break

        if self.is_empty_struct(way_x, way_y) and not is_busy:
            if current_entity.is_movable:
                current_entity.add_coords(x, y)

    # Новые методы для работы с предметами
    def get_item_at(self, x, y):
        """Получить предмет по координатам"""
        for item in self.item_list:
            if item.x == x and item.y == y:
                return item
        return None

    def add_item(self, item):
        self.item_list.append(item)

    def remove_item(self, item):
        """Удалить предмет с карты"""
        if item in self.item_list:
            self.item_list.remove(item)

    def get_MC(self):
        return self.entity_list[0]

    def is_empty_struct(self, x, y):
        return self.map_array[y][x] == " "

    def is_entity_on_coords(self, x, y):
        return self.get_entity_xy(x, y) == None

    def get_entity_xy(self, x, y):
        for entity in self.entity_list:
            if entity.coords == [x, y]:
                return entity

        return None

    def get_random_free_cell(self):
        free_cells = []
        for y in range(self.height):
            for x in range(self.width):
                if self.map_array[y][x] == " " and self.get_entity_xy(x, y) is None:
                    free_cells.append((x, y))
        if not free_cells:
            return None
        return random.choice(free_cells)