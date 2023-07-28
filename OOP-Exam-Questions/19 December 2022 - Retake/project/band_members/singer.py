from project.band_members.musician import Musician


class Singer(Musician):
    _AVAILABLE_SKILLS = ["sing high pitch notes", "sing low pitch notes"]

    @property
    def available_skills(self):
        return self._AVAILABLE_SKILLS
