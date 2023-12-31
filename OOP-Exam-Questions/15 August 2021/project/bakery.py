from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    FOOD_TYPES = {
        "Bread": Bread,
        "Cake": Cake
    }

    DRINK_TYPES = {
        "Tea": Tea,
        "Water": Water
    }

    TABLE_TYPES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu: list = []
        self.drinks_menu: list = []
        self.tables_repository: list = []
        self.total_income: float = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    # helper methods
    def find_food(self, name):
        for food in self.food_menu:
            if food.name == name:
                return food

    def find_drink(self, name):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink

    def find_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def order_food_or_drink(self, table_number: int, type, *items):
        table_obj = self.find_table(table_number)

        if not table_obj:
            return f"Could not find table {table_number}"

        not_in_menu = []
        for item_name in items:
            try:
                if type == "food":
                    item_obj = next(item for item in self.food_menu if item.name == item_name)
                    table_obj.food_orders.append(item_obj)
                else:
                    item_obj = next(item for item in self.drinks_menu if item.name == item_name)
                    table_obj.drink_orders.append(item_obj)
            except StopIteration:
                not_in_menu.append(item_name)

        info = [f"Table {table_number} ordered:"]

        if type == "food":
            [info.append(repr(item)) for item in table_obj.food_orders]
        else:
            [info.append(repr(item)) for item in table_obj.drink_orders]

        info.append(f"{self.name} does not have in the menu:")
        [info.append(item) for item in not_in_menu]

        return "\n".join(info)

    # class methods
    def add_food(self, food_type: str, name: str, price: float):
        if self.find_food(name):
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self.FOOD_TYPES:
            self.food_menu.append(self.FOOD_TYPES[food_type](name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if self.find_drink(name):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self.DRINK_TYPES:
            self.drinks_menu.append(self.DRINK_TYPES[drink_type](name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if self.find_table(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self.TABLE_TYPES:
            self.tables_repository.append(self.TABLE_TYPES[table_type](table_number, capacity))
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        try:
            table_obj = next(t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people)
            table_obj.reserve(number_of_people)
            return f"Table {table_obj.table_number} has been reserved for {number_of_people} people"
        except StopIteration:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        return self.order_food_or_drink(table_number, "food", *food_names)

    def order_drink(self, table_number: int, *drink_names):
        return self.order_food_or_drink(table_number, "drink", *drink_names)

    def leave_table(self, table_number: int):
        table_obj = self.find_table(table_number)
        if table_obj:
            bill = table_obj.get_bill()
            self.total_income += bill
            table_obj.clear()

            return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        info = []
        [info.append(t.free_table_info()) for t in self.tables_repository if not t.is_reserved]

        return "\n".join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

# testing options_adapted from @Devihem's tests:
# from project.bakery import Bakery

# bakery = Bakery("Sunny")

# print(f"{'# ADD_FOOD'}")
# print(bakery.add_food("Bread", "Sour", 1.50))
# print(bakery.add_food("Bread", "White", 1.30))
# print(bakery.add_food("Cake", "Chocolate", 2.90))
# print(bakery.add_food("Cake", "Vanilla", 2.90))
# [print(repr(f)) for f in bakery.food_menu]

# print(f"\n\n{'# ADD_DRINK'}")
# print(bakery.add_drink("Water", "Spring", 250, "Bankya"))
# print(bakery.add_drink("Water", "Mineral", 500, "Devin"))
# print(bakery.add_drink("Tea", "Black", 250, "Ahmad Tea"))
# print(bakery.add_drink("Tea", "Green", 250, "Lipton"))
# [print(repr(d)) for d in bakery.drinks_menu]

# print(f"\n\n{'# ADD_TABLE'}")
# print(bakery.add_table("InsideTable", 5, 5))
# print(bakery.add_table("OutsideTable", 52, 10))
# print(bakery.add_table("OutsideTable", 95, 15))
# print(bakery.add_table("InsideTable", 15, 15))
# print(bakery.add_table("InsideTable", 4, 15))
# [print(t.free_table_info()) for t in bakery.tables_repository]

# print(f"\n\n{'# RESERVE_TABLE'}")
# print(bakery.reserve_table(12))
# [print(t.is_reserved) for t in bakery.tables_repository]
# [print(t.number_of_people) for t in bakery.tables_repository]
# print(bakery.reserve_table(20))

# print(f"\n\n{'# ORDERS_FOOD'}")
# print(bakery.order_food(95, "Sour", "White", "Chocolate", "Vanilla", "Strawberry", "Hazelnut", "Wholegrain"))
# print(bakery.order_food(34, "Sour", "White", "Chocolate", "Vanilla", "Strawberry", "Hazelnut", "Wholegrain"))
# #
# print(f"\n\n{'# ORDERS_DRINK'}")
# print(bakery.order_drink(95, "Spring", "Mineral", "Black", "Green", "White", "Tap", "Fruit"))
# for t in bakery.tables_repository:
#     if t.is_reserved:
#         [print(repr(f)) for f in t.food_orders]
# print()
# for t in bakery.tables_repository:
#     if t.is_reserved:
#         [print(repr(d)) for d in t.drink_orders]


# print(f"\n\n{'# LEAVE_TABLE'}")
# print(bakery.leave_table(95))
# [print(t.free_table_info()) for t in bakery.tables_repository]
# [print(t.is_reserved) for t in bakery.tables_repository]
# [print(t.number_of_people) for t in bakery.tables_repository]

# #
# print(f"\n\n{'# GET_TOTAL_INCOME'}")
# print(bakery.get_total_income())

# print(bakery.reserve_table(8))
# print(f"\n\n{'# ORDERS_FOOD'}")
# print(bakery.order_food(52, "Sour", "White", "Chocolate", "Vanilla", "Strawberry", "Hazelnut", "Wholegrain"))

# print(f"\n\n{'# ORDERS_DRINK'}")
# print(bakery.order_drink(52, "Spring", "Mineral", "Black", "Green", "White", "Tap", "Fruit"))

# print(f"\n\n{'# LEAVE_TABLE'}")
# print(bakery.leave_table(52))

# print(f"\n\n{'# GET_TOTAL_INCOME'}")
# print(bakery.get_total_income())

# print(f"\n\n{'# RESERVE_TABLE'}")
# print(bakery.reserve_table(4))

# print(f"\n\n{'# TABLES_INFO'}")
# print(bakery.get_free_tables_info())
