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
        
# tests
# from project.controller import Controller

# print("# ADD_AQUA")
# controller = Controller()
# print(controller.add_aquarium("FreshwaterAquarium", "FreshAqu_1"))
# print(controller.add_aquarium("SaltwaterAquarium", "SaltAqu_1"))
# print(controller.add_aquarium("FreshwaterAquarium", "FreshAqu_2"))
# print(controller.add_aquarium("SaltwaterAquarium", "SaltAqu_2"))
# print(controller.add_aquarium("RiverwaterAquarium", "SaltAqu_2"))
# # print(controller.add_aquarium("FreshwaterAquarium", ""))
# print(len(controller.aquariums))
# print(controller.aquariums[0].capacity)
# print(controller.aquariums[1].capacity)

# print("# ADD_DECO")
# print(controller.add_decoration("Plant"))
# print(controller.add_decoration("Ornament"))
# print(controller.add_decoration("Plant"))
# print(controller.add_decoration("Ornament"))
# print(controller.add_decoration("LittleStone"))
# print(len(controller.decorations_repository.decorations))
# print(controller.decorations_repository.decorations[0].comfort)
# print(controller.decorations_repository.decorations[0].price)
# print(controller.decorations_repository.decorations[1].comfort)
# print(controller.decorations_repository.decorations[1].price)

# print("# INSERT DECO")
# print(controller.insert_decoration("SaltAqu_1", "Plant"))
# print(len(controller.decorations_repository.decorations))
# print(len(controller.aquariums[1].decorations))
# print(controller.insert_decoration("SaltAqu_1", "LittleStone"))

# print(("# ADD FISH"))
# print(controller.add_fish("SaltAqu_1", "SaltwaterFish", "salt_fish_1", "species_1", 10.00))
# print(controller.add_fish("FreshAqu_2", "FreshwaterFish", "fresh_fish_1", "species_1", 5.00))
# print(controller.add_fish("SaltAqu_1", "SaltwaterFish", "salt_fish_2", "species_2", 15.00))
# print(controller.add_fish("FreshAqu_2", "FreshwaterFish", "fresh_fish_2", "species_2", 10.00))
# print(controller.add_fish("FreshAqu_2", "SaltwaterFish", "fresh_fish_1", "species_1", 5.00))
# print(controller.add_fish("FreshAqu_2", "StrangeFish", "fresh_fish_1", "species_1", 5.00))
# # print(controller.add_fish("FreshAqu_2", "SaltwaterFish", "", "species_1", 5.00))
# # print(controller.add_fish("FreshAqu_2", "SaltwaterFish", "salt_fish_1", "", 5.00))
# # print(controller.add_fish("FreshAqu_2", "SaltwaterFish", "salt_fish_1", "species_1", 0.00))
# print(len(controller.aquariums[0].fish))
# print(len(controller.aquariums[1].fish))
# print(len(controller.aquariums[2].fish))
# print(len(controller.aquariums[3].fish))
# [print(f.name) for f in controller.aquariums[1].fish]
# [print(f.name) for f in controller.aquariums[2].fish]
# print(controller.feed_fish("SaltAqu_1"))
# print(controller.calculate_value("SaltAqu_1"))
# print(controller.report())

# print(controller.add_fish("SaltAqu_1", "SaltwaterFish", "salt_fish_1", "species_1", 10.00))
# fishes = [(f"salt_fish_{i}", f"species_{i}") for i in range(25)]

# for fish in fishes:
#     print(controller.add_fish("SaltAqu_1", "SaltwaterFish", fish[0], fish[1], 10.00))

# print(len(controller.aquariums[2].fish))
# controller.aquariums[2].remove_fish(controller.aquariums[2].fish[0])
# print(len(controller.aquariums[2].fish))

# test output
# # ADD_AQUA
# Successfully added FreshwaterAquarium.
# Successfully added SaltwaterAquarium.
# Successfully added FreshwaterAquarium.
# Successfully added SaltwaterAquarium.
# Invalid aquarium type.
# 4
# 50
# 25
# # ADD_DECO
# Successfully added Plant.
# Successfully added Ornament.
# Successfully added Plant.
# Successfully added Ornament.
# Invalid decoration type.
# 4
# 5
# 10
# 1
# 5
# # INSERT DECO
# Successfully added Plant to SaltAqu_1.
# 3
# 1
# There isn't a decoration of type LittleStone.
# # ADD FISH
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added FreshwaterFish to FreshAqu_2.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added FreshwaterFish to FreshAqu_2.
# Water not suitable.
# There isn't a fish of type StrangeFish.
# 0
# 2
# 2
# 0
# salt_fish_1
# salt_fish_2
# fresh_fish_1
# fresh_fish_2
# Fish fed: 2
# The value of Aquarium SaltAqu_1 is 35.00.
# FreshAqu_1:
# Fish: none
# Decorations: 0
# Comfort: 0
# SaltAqu_1:
# Fish: salt_fish_1 salt_fish_2
# Decorations: 1
# Comfort: 5
# FreshAqu_2:
# Fish: fresh_fish_1 fresh_fish_2
# Decorations: 0
# Comfort: 0
# SaltAqu_2:
# Fish: none
# Decorations: 0
# Comfort: 0
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Successfully added SaltwaterFish to SaltAqu_1.
# Not enough capacity.
# Not enough capacity.
# Not enough capacity.
# 2
# 1

