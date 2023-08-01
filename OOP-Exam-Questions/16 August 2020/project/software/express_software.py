from project.software.software import Software


class ExpressSoftware(Software):
    _TYPE = "Express"
    _MEMORY_FACTOR = 2

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, ExpressSoftware._TYPE, capacity_consumption,
                         memory_consumption * ExpressSoftware._MEMORY_FACTOR)
