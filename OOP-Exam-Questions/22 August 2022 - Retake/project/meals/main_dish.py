from project.meals.meal import Meal


class MainDish(Meal):
    MEAL_TYPE = "Main Dish"

    def __init__(self, name: str, price: float, quantity=50):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def meal_type(self):
        return self.MEAL_TYPE
