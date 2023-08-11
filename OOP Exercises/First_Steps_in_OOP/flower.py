class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int) -> None:
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self) -> str:
        return f"{self.name} is {'' if self.is_happy else 'not '}happy"


# class Flower:
#     def __init__(self, name, water_requirements, is_happy=False):
#         self.name = name
#         self.water_requirements = water_requirements
#         self.is_happy = is_happy

#     def water(self, quantity):
#         if quantity >= self.water_requirements:
#             self.is_happy = True

#     def status(self):
#         if self.is_happy:
#             return f"{self.name} is happy"
#         else:
#             return f"{self.name} is not happy"
