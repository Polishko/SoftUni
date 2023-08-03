class Child:
    MONTH_DAYS = 30

    def __init__(self, food_cost: int, *toys_cost):
        self.cost = food_cost + sum(toys_cost)

    def get_monthly_expense(self):
        return self.MONTH_DAYS * self.cost
