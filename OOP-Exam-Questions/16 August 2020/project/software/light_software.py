from project.software.software import Software


class LightSoftware(Software):
    _TYPE = "Light"
    _MEMORY_FACTOR = 0.50
    _CAPACITY_FACTOR = 1.50

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Light", int(capacity_consumption * LightSoftware._CAPACITY_FACTOR),
                         int(memory_consumption * LightSoftware._MEMORY_FACTOR))
