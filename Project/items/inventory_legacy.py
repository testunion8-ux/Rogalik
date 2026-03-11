from item import Item


class Inventory:
    def __init__(self, max_size=30):
        self.items = []
        self.max_size = max_size

    def add_item(self, item: Item):
        if len(self.items) >= self.max_size:
            return False

        for existing_item in self.items:
            if existing_item.can_stack(item):
                existing_item.quantity += item.quantity
                return True

        if len(self.items) >= self.max_size:
            return False

        self.items.append(item)
        return True

    def remove(self, item: Item, quantity: int = None):
        if item in self.items:

            if quantity is None:
                quantity = item.quantity

            for i, existing_item in enumerate(self.items):
                if existing_item == item:
                    if quantity >= existing_item.quantity:
                        self.items.pop(i)
                    else:
                        existing_item.quantity -= quantity
                    return True
            return False

    def is_inventory_full(self):
        return len(self.items) >= self.max_size

    def __str__(self):
        return (f"Инвентарь: {len(self.items)}/{self.max_size}")

    def swap_items(self, index1: int, index2: int):
        if 0 <= index1 < len(self.items) and 0 <= index2 < len(self.items):
            self.items[index1], self.items[index2] = self.items[index2], self.items[index1]
            return True
        return False

    def display_numbers(self):
        result = []
        for i, item in enumerate(self.items):
            result.append(f"{i}. {item.name} ({item.type})")
        return "\n".join(result)

    def split_stack(self, index: int, quantity: int):
        if 0 <= index < len(self.items):
            item = self.items[index]
            if item.quantity > quantity:
                new_item = Item(item.name, item.type, quantity)
                if self.add_item(new_item):
                    item.quantity -= quantity
                    return True
        return False
