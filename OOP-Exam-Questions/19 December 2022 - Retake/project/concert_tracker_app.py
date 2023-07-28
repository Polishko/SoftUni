from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    _MUSICIAN_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    _NEEDED_CONCERT_SKILLS = {
        "Rock": {
            "Drummer": ["play the drums with drumsticks"],
            "Singer": ["sing high pitch notes"],
            "Guitarist": ["play rock"]
        },
        "Metal": {
            "Drummer": ["play the drums with drumsticks"],
            "Singer": ["sing low pitch notes"],
            "Guitarist": ["play metal"]
        },
        "Jazz": {
            "Drummer": ["play the drums with drum brushes"],
            "Singer": ["sing high pitch notes", "sing low pitch notes"],
            "Guitarist": ["play jazz"]
        }
    }

    def __init__(self):
        self.bands: list = []
        self.musicians: list = []
        self.concerts: list = []

    def find_musician(self, name):
        for musician_obj in self.musicians:
            if musician_obj.name == name:
                return musician_obj

    def find_band(self, name):
        for band_obj in self.bands:
            if band_obj.name == name:
                return band_obj

    def find_concert(self, place):
        for concert_obj in self.concerts:
            if concert_obj.place == place:
                return concert_obj

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self._MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        if self.find_musician(name):
            raise Exception(f"{name} is already a musician!")

        musician_obj = self._MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(musician_obj)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self.find_band(name):
            raise Exception(f"{name} band is already created!")

        band_obj = Band(name)
        self.bands.append(band_obj)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        searched_concert = self.find_concert(place)
        if searched_concert:
            raise Exception(f"{place} is already registered for {searched_concert.genre} concert!")

        concert_obj = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert_obj)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician_obj = self.find_musician(musician_name)

        if not musician_obj:
            raise Exception(f"{musician_name} isn't a musician!")

        band_obj = self.find_band(band_name)

        if not band_obj:
            raise Exception(f"{band_name} isn't a band!")

        band_obj.members.append(musician_obj)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band_obj = self.find_band(band_name)

        if not band_obj:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician_obj = next(m for m in band_obj.members if m.name == musician_name)
            band_obj.members.remove(musician_obj)
            return f"{musician_name} was removed from {band_name}."
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

    def start_concert(self, concert_place: str, band_name: str):
        musician_types = set()
        band_obj = self.find_band(band_name)
        [musician_types.add(m.__class__.__name__) for m in band_obj.members]

        if len(musician_types) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert_obj = self.find_concert(concert_place)
        required_skills = self._NEEDED_CONCERT_SKILLS[concert_obj.genre]

        for m in band_obj.members:
            type_m = m.__class__.__name__
            skills = m.skills
            if not set(required_skills[type_m]).issubset(set(skills)):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert_obj.audience * concert_obj.ticket_price) - concert_obj.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert_obj.genre} concert in {concert_obj.place}."
