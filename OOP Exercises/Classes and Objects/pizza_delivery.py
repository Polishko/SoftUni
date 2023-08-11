class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> str or None:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0

        self.ingredients[ingredient] += quantity
        self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> str or None:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        else:
            if self.ingredients[ingredient] < quantity:
                return f"Please check again the desired quantity of {ingredient}!"
            else:
                self.ingredients[ingredient] -= quantity
                self.price -= price_per_quantity * quantity

    def make_order(self) -> str or None:
        if not self.ordered:
            self.ordered = True
            lst = [f"{key}: {value}" for key, value in self.ingredients.items()]

            return f"You've ordered pizza {self.name} prepared with" \
                   f" {', '.join(item for item in lst)} " \
                   f"and the price will be {self.price}lv."
