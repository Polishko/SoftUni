from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player_1 = TennisPlayer("Serena Williams", 41, 100)
        self.player_2 = TennisPlayer("Naomi Osaka", 25, 90)

    def test_correct_initiation(self):
        self.assertEqual("Serena Williams", self.player_1.name)
        self.assertEqual(41, self.player_1.age)
        self.assertEqual(100, self.player_1.points)
        self.assertEqual([], self.player_1.wins)

    def test_name_setter_raises_value_err_upon_invalid_value(self):
        with self.assertRaises(ValueError) as ve:
            self.player_1.name = "Se"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_setter_raises_value_err_upon_invalid_value(self):
        with self.assertRaises(ValueError) as ve:
            self.player_1.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_correctly_adds_new_win(self):
        self.player_1.add_new_win("Australian Open")
        self.assertEqual(["Australian Open"], self.player_1.wins)

    def test_add_new_win_dismisses_already_added_wins(self):
        self.player_1.wins = ["Australian Open"]
        result = self.player_1.add_new_win("Australian Open")
        self.assertEqual("Australian Open has been already added to the list of wins!", result)

    def test_less_than_returns_correct_message_for_lower_self_points(self):
        result = self.player_2 < self.player_1
        self.assertEqual("Serena Williams is a top seeded player "
                         "and he/she is better than Naomi Osaka", result)

    def test_less_than_returns_correct_message_for_lower_other_points(self):
        result = self.player_1 < self.player_2
        self.assertEqual("Serena Williams is a better player than Naomi Osaka",
                         result)

    def test_str_returns_correct_player_info(self):
        self.player_1.wins = ["Australian Open", "French Open", "US Open"]
        self.assertEqual("Tennis Player: Serena Williams\n"
                         "Age: 41\nPoints: 100.0\nTournaments won: Australian Open,"
                         " French Open, US Open", str(self.player_1))


if __name__ == "__main__":
    main()
