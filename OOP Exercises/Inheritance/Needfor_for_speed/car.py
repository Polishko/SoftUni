from project.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

    DEFAULT_FUEL_CONSUMPTION = 3
