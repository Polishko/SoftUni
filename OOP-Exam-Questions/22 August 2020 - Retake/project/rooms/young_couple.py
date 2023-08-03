from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCouple(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        budget = salary_one + salary_two
        super().__init__(family_name, budget, 2)
        self.appliances = [TV(), Fridge(), Laptop()] * 2
        self.calculate_expenses(self.appliances)
        self.room_cost = 20
