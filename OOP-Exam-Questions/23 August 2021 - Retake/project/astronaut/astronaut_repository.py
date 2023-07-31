class AstronautRepository:
    def __init__(self):
        self.astronauts: list = []

    def add(self, astronaut: object):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: object):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
