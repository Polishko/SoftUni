from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    SIZE_INCREASE = 3
    INITIAL_SIZE = 3
    
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.INITIAL_SIZE, price)

    @property
    def size_increase_increment(self):
        return self.SIZE_INCREASE
