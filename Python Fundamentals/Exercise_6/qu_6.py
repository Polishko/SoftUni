class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity == len(self.items):
            return "not enough room in the inventory"

        self.items.append(item)

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        capacity_left = self.__capacity - len(self.items)
        result = f"Items: {', '.join(self.items)}.\nCapacity left: {capacity_left}"
        return result


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)




