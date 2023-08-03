from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        budget = salary_one + salary_two
        members_count = 2 + len(children)

        super().__init__(family_name, budget, members_count)
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * members_count
        self.calculate_expenses(self.children, self.appliances)
        self.room_cost = 30


