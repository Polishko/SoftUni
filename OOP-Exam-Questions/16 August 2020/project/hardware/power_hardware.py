from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    _TYPE = "Power"
    _MEMORY_FACTOR = 1.75
    _CAPACITY_FACTOR = 0.25

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, PowerHardware._TYPE, int(capacity * PowerHardware._CAPACITY_FACTOR),
                         int(memory * PowerHardware._MEMORY_FACTOR))
