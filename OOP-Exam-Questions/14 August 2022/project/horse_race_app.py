from project.jockey import Jockey
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_race import HorseRace


class HorseRaceApp:
    VALID_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses: list = []
        self.jockeys: list = []
        self.horse_races: list = []

    def find_horse(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse

    def find_jockey(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def find_race(self, horse_race):
        for race in self.horse_races:
            if race.race_type == horse_race:
                return race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.find_horse(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_TYPES:
            horse_obj = self.VALID_TYPES[horse_type](horse_name, horse_speed)

            if horse_obj:
                self.horses.append(horse_obj)
                return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.find_jockey(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey_obj = Jockey(jockey_name, age)

        if jockey_obj:
            self.jockeys.append(jockey_obj)
            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.find_race(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        race_obj = HorseRace(race_type)

        if race_obj:
            self.horse_races.append(race_obj)
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey_obj = self.find_jockey(jockey_name)

        if not jockey_obj:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for horse in reversed(self.horses):
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                if jockey_obj.horse:
                    return f"Jockey {jockey_name} already has a horse."
                horse.is_taken = True
                jockey_obj.horse = horse

                return f"Jockey {jockey_name} will ride the horse {horse.name}."

        raise Exception(f"Horse breed {horse_type} could not be found!")

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race_obj = self.find_race(race_type)

        if not race_obj:
            raise Exception(f"Race {race_type} could not be found!")

        jockey_obj = self.find_jockey(jockey_name)

        if not jockey_obj:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey_obj.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if [jockey for jockey in race_obj.jockeys if jockey.name == jockey_name]:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race_obj.jockeys.append(jockey_obj)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race_obj = self.find_race(race_type)

        if not race_obj:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race_obj.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(race_obj.jockeys, key=lambda j: -j.horse.speed)[0]

        return f"The winner of the {race_type} race," \
               f" with a speed of {winner.horse.speed}km/h" \
               f" is {winner.name}! Winner's horse: {winner.horse.name}."


        
# tests (mine)
# from project.jockey import Jockey
# from project.horse_specification.appaloosa import Appaloosa
# from project.horse_specification.thoroughbred import Thoroughbred
# from project.horse_race_app import HorseRaceApp
# from project.horse_race import HorseRace
# 
# # jockey_1 = Jockey("Nalan", 43)
# # print(jockey_1.name)
# # print(jockey_1.age)
# # print(jockey_1.horse)
# # horse_1 = Appaloosa("Beyaz Yildirim", 118)
# # horse_2 = Thoroughbred("Kara Bela", 137)
# # print(horse_1.speed)
# # print(horse_2.speed)
# # horse_1.train()
# # horse_2.train()
# # print(horse_1.speed)
# # print(horse_2.speed)
# # horse_1.train()
# # horse_2.train()
# # print(horse_1.speed)
# # print(horse_2.speed)
# # app = HorseRaceApp()
# # print(app.add_horse("Appaloosa", "Beyaz Yildirim", 118))
# # print(app.add_horse("Thoroughbred", "Kara Bela", 137))
# # print(app.add_horse("Appaloosa", "Krema", 120))
# # print(len(app.horses))
# # print(app.add_jockey("Nalan", 43))
# # print(app.add_jockey("Genc", 42))
# # print(len(app.jockeys))
# # print(app.create_horse_race("Winter"))
# # print(app.create_horse_race("Spring"))
# # print(app.create_horse_race("Autumn"))
# # print(app.create_horse_race("Summer"))
# # print(len(app.horse_races))
# # print(app.add_horse_to_jockey("Nalan", "Appaloosa"))
# # print(app.jockeys[0].horse.is_taken)
# # print(app.add_horse_to_jockey("Nalan", "Thoroughbred"))
# # # print(app.add_horse_to_jockey("Leman", "Thoroughbred"))
# 
# # given tests
# 
# horseRaceApp = HorseRaceApp()
# print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
# print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
# print(horseRaceApp.add_jockey("Peter", 19))
# print(horseRaceApp.add_jockey("Mariya", 21))
# print(horseRaceApp.create_horse_race("Summer"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
# print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.start_horse_race("Summer"))
