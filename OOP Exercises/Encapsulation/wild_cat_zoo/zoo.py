from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List = []
        self.workers: List = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity == 0:
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__animal_capacity -= 1
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        worker_to_fire = [w for w in self.workers if w.name == worker_name]

        if not worker_to_fire:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker_to_fire[0])
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        sum_salary = sum(worker_to_pay.salary for worker_to_pay in self.workers)

        if sum_salary > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= sum_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        sum_tending = sum(animal_to_tend.money_for_care for animal_to_tend in self.animals)

        if sum_tending > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= sum_tending
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:

        all_animals = {
            "Lions": [animal_type for animal_type in self.animals if animal_type.__class__.__name__ == "Lion"],
            "Tigers": [animal_type for animal_type in self.animals if animal_type.__class__.__name__ == "Tiger"],
            "Cheetahs": [animal_type for animal_type in self.animals if animal_type.__class__.__name__ == "Cheetah"]
        }

        result = f"You have {len(self.animals)} animals\n"

        for group, group_animals in all_animals.items():
            result += f"----- {len(group_animals)} {group}:\n"
            result += "\n".join(member.__repr__() for member in group_animals)
            if group != "Cheetahs":
                result += "\n" # this is to remove the \n at the end, using result[:-1] or result.strip() is also an optuon

        return result

    def workers_status(self) -> str:

        all_workers = {
            "Keepers": [employee for employee in self.workers if employee.__class__.__name__ == "Keeper"],
            "Caretakers": [employee for employee in self.workers if employee.__class__.__name__ == "Caretaker"],
            "Vets": [employee for employee in self.workers if employee.__class__.__name__ == "Vet"]
        }

        result = f"You have {len(self.workers)} workers\n"

        for group, group_workers in all_workers.items():
            result += f"----- {len(group_workers)} {group}:\n"
            result += "\n".join(member.__repr__() for member in group_workers)
            if group != "Vets":
                result += "\n" # this is to remove the \n at the end, using result[:-1] or result.strip() is also an optuon

        return result
