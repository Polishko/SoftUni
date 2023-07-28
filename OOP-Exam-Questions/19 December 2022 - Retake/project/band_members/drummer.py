from project.band_members.musician import Musician


class Drummer(Musician):
    _AVAILABLE_SKILLS = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

    @property
    def available_skills(self):
        return self._AVAILABLE_SKILLS
