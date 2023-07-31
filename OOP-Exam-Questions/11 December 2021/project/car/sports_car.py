from project.car.car import Car


class SportsCar(Car):
    MIN_SPEED = 400
    MAX_SPEED = 600

    @property
    def min_speed_limit(self):
        return self.MIN_SPEED

    @property
    def max_speed_limit(self):
        return self.MAX_SPEED
