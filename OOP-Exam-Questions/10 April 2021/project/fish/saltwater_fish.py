from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    SIZE_INCREASE = 2
    INITIAL_SIZE = 5

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.INITIAL_SIZE, price)

    @property
    def size_increase_increment(self):
        return self.SIZE_INCREASE
