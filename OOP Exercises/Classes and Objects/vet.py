from typing import List


class Vet:
    animals = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, animal_name: str) -> str:
        if len(self.animals) >= Vet.space:
            return "Not enough space"

        self.animals.append(animal_name)
        Vet.animals.append(animal_name)

        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"

        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)

        return f"{animal_name} unregistered successfully"

    def info(self) -> str:
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


# class Vet:
#     animals = []
#     space = 5

#     def __init__(self, name: str):
#         self.name = name
#         self.animals = []

#     def register_animal(self, animal_name: str) -> str:
#         if Vet.space > 0:
#             Vet.animals.append(animal_name)
#             self.animals.append(animal_name)
#             Vet.space -= 1

#             return f"{animal_name} registered in the clinic"

#         return "Not enough space"

#     def unregister_animal(self, animal_name: str) -> str:
#         if animal_name in self.animals:
#             self.animals.remove(animal_name)
#             Vet.animals.remove(animal_name)
#             Vet.space += 1

#             return f"{animal_name} unregistered successfully"

#         return f"{animal_name} not in the clinic"

#     def info(self) -> str:
#         return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"
