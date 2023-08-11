from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        ...

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        ...


class Car(Vehicle):
    CONDITIONER_ON = 0.9

    def drive(self, distance: float) -> None:
        expected_consumption = (self.fuel_consumption + Car.CONDITIONER_ON) * distance
        if expected_consumption <= self.fuel_quantity:
            self.fuel_quantity -= expected_consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_ON = 1.6
    LOSS_ADDED = 0.95

    def drive(self, distance: float) -> None:
        expected_consumption = (self.fuel_consumption + Truck.CONDITIONER_ON) * distance

        if expected_consumption <= self.fuel_quantity:
            self.fuel_quantity -= expected_consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * Truck.LOSS_ADDED

