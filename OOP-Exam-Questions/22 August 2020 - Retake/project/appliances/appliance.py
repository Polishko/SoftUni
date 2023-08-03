class Appliance:
    MONTH_DAYS = 30

    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expense(self):
        return self.MONTH_DAYS * self.cost
