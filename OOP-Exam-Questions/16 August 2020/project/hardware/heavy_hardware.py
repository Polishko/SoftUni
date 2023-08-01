from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    _TYPE = "Heavy"
    _MEMORY_FACTOR = 0.75
    _CAPACITY_FACTOR = 2

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, HeavyHardware._TYPE, capacity * HeavyHardware._CAPACITY_FACTOR,
                         int(memory * HeavyHardware._MEMORY_FACTOR))
