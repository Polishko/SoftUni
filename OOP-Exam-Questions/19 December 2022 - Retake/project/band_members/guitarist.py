from project.band_members.musician import Musician


class Guitarist(Musician):
    _AVAILABLE_SKILLS = ["play metal", "play rock", "play jazz"]

    @property
    def available_skills(self):
        return self._AVAILABLE_SKILLS
