from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove


class OldCouple(Room):

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        budget = pension_one + pension_two

        super().__init__(family_name, budget, 2)
        self.appliances = [TV(), Fridge(), Stove()] * 2
        self.calculate_expenses(self.appliances)
        self.room_cost = 15

