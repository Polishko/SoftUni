from project.supply.supply import Supply


class Drink(Supply):
    TYPE = "Drink"

    def __init__(self, name, energy=15):
        super().__init__(name, energy)

    def details(self):
        return f"{self.TYPE}: {self.name}, {self.energy}"
