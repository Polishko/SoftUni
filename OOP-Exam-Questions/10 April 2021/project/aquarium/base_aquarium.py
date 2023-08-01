from abc import ABC, abstractmethod


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: list = []
        self.fish: list = []
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [f.eat() for f in self.fish]

    def __str__(self):
        fish = " ".join(f.name for f in self.fish) if self.fish else "none"
        return f"{self.name}:\nFish: {fish}\nDecorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"
