from typing import List


class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __add__(self, other) -> "Person":
        return Person(self.name, other.surname)

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name: str, people: List[Person]) -> None:
        self.name = name
        self.people = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, grp_1) -> "Group":
        new_group = self.people + grp_1.people
        new_name = f"{self.name} {grp_1.name}"
        return Group(new_name, new_group)

    def __getitem__(self, index: int) -> str:
        return f"Person {index}: {self.people[index]}"

    def __repr__(self) -> str:
        return f"Group {self.name} with members {', '.join([p.__repr__() for p in self.people])}"


