from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    _INITIAL_WEIGHT = 7
    _WEIGHT_INCREASE = 1

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self._INITIAL_WEIGHT)

    @property
    def weight_increase(self):
        return self._WEIGHT_INCREASE
