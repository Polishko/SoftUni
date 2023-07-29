from project.meals.meal import Meal


class Starter(Meal):
    MEAL_TYPE = "Starter"

    def __init__(self, name: str, price: float, quantity=60):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def meal_type(self):
        return self.MEAL_TYPE
