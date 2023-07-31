from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    INITIAL_OX = 50

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OX)

    @property
    def oxygen_decrease_value(self):
        return None
