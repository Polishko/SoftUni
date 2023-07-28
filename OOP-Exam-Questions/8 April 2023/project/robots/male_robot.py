from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    _INITIAL_WEIGHT = 9
    _WEIGHT_INCREASE = 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self._INITIAL_WEIGHT)

    @property
    def weight_increase(self):
        return self._WEIGHT_INCREASE
