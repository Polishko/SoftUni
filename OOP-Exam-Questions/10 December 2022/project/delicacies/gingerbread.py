from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    WEIGHT = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, self.WEIGHT, price)
