from abc import ABC, abstractmethod
from typing import Dict
from math import log2


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @staticmethod
    def validate_attribute(value, attr_name):
        if len(value.split()) == 0:
            raise ValueError(f"{attr_name} name cannot be empty.")
        return value

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self.__manufacturer = self.validate_attribute(value, "Manufacturer")

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = self.validate_attribute(value, "Model")

    @property
    @abstractmethod
    def processors(self) -> Dict[str, int]:
        ...

    @property
    @abstractmethod
    def max_ram(self):
        ...

    @property
    @abstractmethod
    def type_computer(self):
        ...

    @property
    def valid_rams(self):
        return [(2 ** x) for x in range(1, int(log2(self.max_ram)) + 1)]

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.processors:
            raise ValueError(f"{processor} is not compatible"
                             f" with {self.type_computer} {self.manufacturer} {self.model}!")

        if ram not in self.valid_rams:
            raise ValueError(f"{ram}GB RAM is not compatible"
                             f" with {self.type_computer} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = int(log2(ram)) * 100 + self.processors[processor]

        return f"Created {self.__repr__()} for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
