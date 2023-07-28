from project.supply.supply import Supply


class Food(Supply):
    TYPE = "Food"

    def __init__(self, name, energy=25):
        super().__init__(name, energy)

    def details(self):
        return f"{self.TYPE}: {self.name}, {self.energy}"
