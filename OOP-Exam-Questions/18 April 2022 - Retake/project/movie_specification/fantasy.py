from project.movie_specification.movie import Movie


class Fantasy(Movie):
    _min_Age = 6

    def __init__(self, title, year, owner, age_restriction=6):
        super().__init__(title, year, owner, age_restriction)

    @property
    def genre(self):
        return self.__class__.__name__

    @property
    def min_age(self):
        return self._min_Age
