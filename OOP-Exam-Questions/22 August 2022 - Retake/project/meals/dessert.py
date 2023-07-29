from project.meals.meal import Meal


class Dessert(Meal):
    MEAL_TYPE = "Dessert"

    def __init__(self, name: str, price: float, quantity=30):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def meal_type(self):
        return self.MEAL_TYPE
