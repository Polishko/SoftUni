class Equipment:
    id = 1

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = Equipment.id
        Equipment.id += 1

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id() -> int:
        return Equipment.id

