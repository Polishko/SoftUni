from project.computer_types.computer import Computer

class DesktopComputer(Computer):
    _MAX_RAM = 128
    _TYPE = "desktop computer"

    @property
    def processors(self):
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }

    @property
    def max_ram(self):
        return self._MAX_RAM

    @property
    def type_computer(self):
        return self._TYPE

