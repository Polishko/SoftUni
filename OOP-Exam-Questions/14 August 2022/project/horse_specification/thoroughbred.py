from project.horse_specification.horse import Horse


class Thoroughbred (Horse):
    MAX_SPEED = 140
    SPEED_INCREASE = 3

    @property
    def max_speed(self):
        return self.MAX_SPEED

    @property
    def speed_increase_increment(self):
        return self.SPEED_INCREASE
