from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OX_DECREASE = 15
    INITIAL_OX = 90

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OX)

    @property
    def oxygen_decrease_value(self):
        return self.OX_DECREASE
