from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CARS = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def __init__(self):
        self.cars: list = []
        self.drivers: list = []
        self.races: list = []

    def find_car(self, model):
        for car in self.cars:
            if car.model == model:
                return car

    def find_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.VALID_CARS:
            return

        if self.find_car(model):
            raise Exception(f"Car {model} is already created!")

        car_obj = self.VALID_CARS[car_type](model, speed_limit)
        if car_obj:
            self.cars.append(car_obj)

            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.find_driver(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        driver_obj = Driver(driver_name)
        if driver_obj:
            self.drivers.append(driver_obj)

            return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.find_race(race_name):
            raise Exception(f"Race {race_name} is already created!")

        race_obj = Race(race_name)
        if race_obj:
            self.races.append(race_obj)

            return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver_obj = self.find_driver(driver_name)
        if not driver_obj:
            raise Exception(f"Driver {driver_name} could not be found!")

        potential_cars = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken]
        if not potential_cars:
            raise Exception(f"Car {car_type} could not be found!")

        car_obj = potential_cars[-1]

        if driver_obj.car:
            old_car_obj = driver_obj.car
            old_car_obj.is_taken = False

            driver_obj.car = car_obj
            car_obj.is_taken = True

            return f"Driver {driver_name} changed his car from {old_car_obj.model} to {car_obj.model}."

        driver_obj.car = car_obj
        car_obj.is_taken = True

        return f"Driver {driver_name} chose the car {car_obj.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race_obj = self.find_race(race_name)
        if not race_obj:
            raise Exception(f"Race {race_name} could not be found!")

        driver_obj = self.find_driver(driver_name)
        if not driver_obj:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver_obj.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver_obj in race_obj.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race_obj.drivers.append(driver_obj)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race_obj = self.find_race(race_name)
        if not race_obj:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race_obj.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        drivers_with_fastest_cars = sorted(race_obj.drivers, key=lambda x: -x.car.speed_limit)[:3]

        result = []
        for d in drivers_with_fastest_cars:
            d.number_of_wins += 1
            result.append(f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}.")

        return "\n".join(result)
