from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    SPEED_INCREASE = 2

    @property
    def max_speed(self):
        return self.MAX_SPEED

    @property
    def speed_increase_increment(self):
        return self.SPEED_INCREASE
