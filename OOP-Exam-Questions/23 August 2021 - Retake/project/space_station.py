from project.planet.planet_repository import PlanetRepository
from project.planet.planet import Planet
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class SpaceStation:
    ASTRONAUT_TYPES = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist
    }

    SUCCESSFUL_MISSIONS = 0
    UNSUCCESSFUL_MISSIONS = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type not in self.ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        self.astronaut_repository.add(self.ASTRONAUT_TYPES[astronaut_type](name))

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet_obj = Planet(name)
        planet_obj.items = items.split(", ")
        self.planet_repository.add(planet_obj)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut_obj = self.astronaut_repository.find_by_name(name)

        if not astronaut_obj:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut_obj)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet_obj = self.planet_repository.find_by_name(planet_name)

        if not planet_obj:
            raise Exception("Invalid planet name!")

        suitable_astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]

        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        sorted_suitable = sorted(suitable_astronauts, key=lambda x: -x.oxygen)

        explorer_count = 0
        for curr_astr in sorted_suitable:
            explorer_count += 1

            while planet_obj.items:
                curr_item = planet_obj.items.pop()
                curr_astr.backpack.append(curr_item)
                curr_astr.breathe()

                if len(planet_obj.items) == 0:
                    self.SUCCESSFUL_MISSIONS += 1
                    return f"Planet: {planet_name} was explored. {explorer_count}" \
                           f" astronauts participated in collecting items."

                if curr_astr.oxygen <= 0:
                    break

            if explorer_count == 5:
                break

        self.UNSUCCESSFUL_MISSIONS += 1
        return "Mission is not completed."

    def report(self):
        result = [f"{self.SUCCESSFUL_MISSIONS} successful missions!",
                  f"{self.UNSUCCESSFUL_MISSIONS} missions were not completed!", f"Astronauts' info:"]

        for astronaut in self.astronaut_repository.astronauts:
            result.append(f"Name: {astronaut.name}")
            result.append(f"Oxygen: {astronaut.oxygen}")
            backpack = "none" if len(astronaut.backpack) == 0 else ", ".join(astronaut.backpack)
            result.append(f"Backpack items: {backpack}")

        return "\n".join(result)
