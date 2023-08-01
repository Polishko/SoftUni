from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.decoration.decoration_repository import DecorationRepository
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUMS = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }

    VALID_DECORATIONS = {
        "Ornament": Ornament,
        "Plant": Plant
    }

    VALID_FISH = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: list = []

    # helper methods
    def find_aquarium(self, aqu_name):
        for aqu in self.aquariums:
            if aqu.name == aqu_name:
                return aqu

    # class methods
    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.VALID_AQUARIUMS:
            return "Invalid aquarium type."

        aqua_obj = self.VALID_AQUARIUMS[aquarium_type](aquarium_name)
        self.aquariums.append(aqua_obj)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.VALID_DECORATIONS:
            return "Invalid decoration type."

        deco_obj = self.VALID_DECORATIONS[decoration_type]()
        self.decorations_repository.add(deco_obj)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        deco_obj = self.decorations_repository.find_by_type(decoration_type)

        if deco_obj == "None":
            return f"There isn't a decoration of type {decoration_type}."

        aqu_obj = self.find_aquarium(aquarium_name)

        if aqu_obj:
            aqu_obj.add_decoration(deco_obj)
            self.decorations_repository.remove(deco_obj)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.VALID_FISH:
            return f"There isn't a fish of type {fish_type}."

        aqu_obj = self.find_aquarium(aquarium_name)

        if aqu_obj.FISH_TYPE != fish_type:
            return "Water not suitable."

        fish_obj = self.VALID_FISH[fish_type](fish_name, fish_species, price)
        return aqu_obj.add_fish(fish_obj)

    def feed_fish(self, aquarium_name: str):
        aqu_obj = self.find_aquarium(aquarium_name)

        aqu_obj.feed()
        return f"Fish fed: {len(aqu_obj.fish)}"

    def calculate_value(self, aquarium_name: str):
        aqu_obj = self.find_aquarium(aquarium_name)
        price = sum(f.price for f in aqu_obj.fish) + sum(d.price for d in aqu_obj.decorations)

        return f"The value of Aquarium {aquarium_name} is {price:.2f}."

    def report(self):
        result = []
        [result.append(str(aqu)) for aqu in self.aquariums]

        return "\n".join(result)
