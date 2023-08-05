from unittest import TestCase, main
from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self):
        self.movie_1 = Movie("Don't Look Now", 1973, 7.1)
        self.movie_2 = Movie("Insomnia", 1997, 7.2)
        self.movie_3 = Movie("Spoorlos", 1977, 7.7)

    def test_correct_initialization(self):
        self.assertEqual("Don't Look Now", self.movie_1.name)
        self.assertEqual(1973, self.movie_1.year)
        self.assertEqual(7.1, self.movie_1.rating)
        self.assertEqual([], self.movie_1.actors)

    def test_setter_raises_val_error_for_empty_name(self):
        with self.assertRaises(ValueError) as ve:
            self.movie_1.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_setter_raises_val_error_for_year_before_1887(self):
        with self.assertRaises(ValueError) as ve:
            self.movie_1.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_adds_actor_not_in_actor_list(self):
        result_1 = self.movie_1.add_actor("Julie Christie")
        self.assertEqual(["Julie Christie"], self.movie_1.actors)
        self.assertIsNone(result_1)
        result_2 = self.movie_1.add_actor("Donald Sutherland")
        self.assertEqual(["Julie Christie", "Donald Sutherland"], self.movie_1.actors)
        self.assertIsNone(result_2)

    def test_add_actor_doesnt_add_actor_if_actor_in_actors_list(self):
        self.movie_1.actors = ["Julie Christie", "Donald Sutherland"]
        result = self.movie_1.add_actor("Julie Christie")
        self.assertEqual(["Julie Christie", "Donald Sutherland"], self.movie_1.actors)
        self.assertEqual(f"Julie Christie is already added in the list of actors!", result)

    def test_gt_rating_evaluation_correct_for_lower_other_rating(self):
        result = self.movie_3.__gt__(self.movie_2)
        self.assertEqual(f'"Spoorlos" is better than "Insomnia"', result)

    def test_gt_rating_evaluation_correct_for_higher_other_rating(self):
        result = self.movie_1.__gt__(self.movie_2)
        self.assertEqual(f'"Insomnia" is better than "Don\'t Look Now"', result)

    def test_repr_returns_correct_string(self):
        self.movie_2.actors = ["Stellan Skarsgard", "Maria Mathiesen"]
        result = repr(self.movie_2)
        self.assertEqual("Name: Insomnia\n"
                         "Year of Release: 1997\n"
                         "Rating: 7.20\n"
                         "Cast: Stellan Skarsgard, Maria Mathiesen", result)


if __name__ == "__main__":
    main()