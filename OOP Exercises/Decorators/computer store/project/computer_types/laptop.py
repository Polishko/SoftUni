from project.computer_types.computer import Computer

class Laptop(Computer):
    _MAX_RAM = 64
    _TYPE = "laptop"

    @property
    def processors(self):
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }

    @property
    def max_ram(self):
        return self._MAX_RAM

    @property
    def type_computer(self):
        return self._TYPE
