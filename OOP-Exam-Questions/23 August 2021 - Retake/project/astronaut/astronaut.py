from abc import ABC, abstractmethod


class Astronaut(ABC):
    OX_DECREASE = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @property
    @abstractmethod
    def oxygen_decrease_value(self):
        ...

    @property
    def oxygen_decrease(self):
        return self.oxygen_decrease_value if self.oxygen_decrease_value else self.OX_DECREASE

    def breathe(self):
        self.oxygen -= self.oxygen_decrease

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
