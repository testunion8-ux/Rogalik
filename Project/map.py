class Map:
    map_array = []
    entity_list = []

    def __init__(self, width: int, height: int, player_spawn_point: tuple):
        self.player_spawn_point = player_spawn_point
        self.height = height
        self.width = width

        self.generate()

    def add_entity(self, entity, coords: tuple):
        entity.coords = list(coords)
        self.entity_list.append(entity)

    def generate(self):
        for y in range(self.height):
            self.map_array.append([])
            for x in range(self.width):
                if x == 0 or x == self.width - 1 \
                        or y == 0 or y == self.height - 1:
                    self.map_array[y].append("#")
                else:
                    self.map_array[y].append(" ")

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
            current_entity.angle = 180
        elif x == 1:
            current_entity.angle = 0

        if y == -1:
            current_entity.angle = 90
        elif y == 1:
            current_entity.angle = 270

        is_busy = False

        for entity in self.entity_list:
            if entity.x == way_x and entity.y == way_y:
                is_busy = True
                break

        if self.map_array[way_y][way_x] == " " and not is_busy:
            if current_entity.is_movable:
                current_entity.add_coords(x, y)

    def get_MC(self):
        return self.entity_list[0]

    def get_entity_xy(self, x, y):
        for entity in self.entity_list:
            if entity.coords == [x, y]:
                return entity

        return None

