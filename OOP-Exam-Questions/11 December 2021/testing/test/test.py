from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team1 = Team("Hotties")
        self.team1.members = {"Nalan": 44, "Tanya": 42, "Elena": 36, "Sultan": 41}
        self.team2 = Team("Lazies")
        self.team2.members = {"Someguy1": 42, "Someguy2": 40, "Someguy3": 33}
        self.team3 = Team("CoolGals")
        self.team3.members = {"Gal1": 24, "Gal2": 33, "Gal3": 46, "Gal4": 28}
        self.team4 = Team("Test")
        self.team5 = Team("OnFire")
        self.team5.members = {"Nalan": 38}
        self.team6 = Team("Empty")

    def test_correct_initialisation(self):
        self.assertEqual("Hotties", self.team1.name)
        self.assertEqual({
            "Nalan": 44,
            "Tanya": 42,
            "Elena": 36,
            "Sultan": 41
        }, self.team1.members)
        self.assertEqual(4, len(self.team1.members))
        self.assertEqual({}, self.team4.members)

    def test_non_letter_char_in_team_name_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team1.name = ",otties"
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))
        self.assertEqual("Hotties", self.team1.name)

        with self.assertRaises(ValueError) as ve:
            self.team1.name = "Hot1ies"
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))
        self.assertEqual("Hotties", self.team1.name)

        with self.assertRaises(ValueError) as ve:
            self.team4.name = "  "
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))
        self.assertEqual("Test", self.team4.name)

    def test_add_member_adds_new_members_omits_existing_members(self):
        result = self.team1.add_member(Leman=42, Ozge=40, Sultan=41, Nalan=40)
        self.assertEqual({
            "Nalan": 44,
            "Tanya": 42,
            "Elena": 36,
            "Sultan": 41,
            "Leman": 42,
            "Ozge": 40
        }, self.team1.members)
        self.assertEqual("Successfully added: Leman, Ozge", result)
        self.assertEqual(6, len(self.team1.members))

        result2 = self.team4.add_member()
        self.assertEqual({}, self.team4.members)
        self.assertEqual(0, len(self.team4.members))
        self.assertEqual("Successfully added: ", result2)

    def test_remove_member_removes_existing_member(self):
        result1 = self.team1.remove_member("Nalan")
        self.assertEqual({
            "Tanya": 42,
            "Elena": 36,
            "Sultan": 41,
        }, self.team1.members)
        self.assertEqual("Member Nalan removed", result1)
        self.assertEqual(3, len(self.team1.members))
        self.assertNotIn("Nalan", self.team1.members)

        result2 = self.team1.remove_member("Elena")
        self.assertEqual({
            "Tanya": 42,
            "Sultan": 41,
        }, self.team1.members)
        self.assertEqual("Member Elena removed", result2)
        self.assertEqual(2, len(self.team1.members))
        self.assertNotIn("Elena", self.team1.members)

    def test_remove_member_omits_non_existent_member(self):
        result = self.team1.remove_member("Ozge")
        self.assertEqual({
            "Nalan": 44,
            "Tanya": 42,
            "Elena": 36,
            "Sultan": 41,
        }, self.team1.members)
        self.assertEqual("Member with name Ozge does not exist", result)
        self.assertEqual(4, len(self.team1.members))

        result2 = self.team4.remove_member("")
        self.assertEqual({}, self.team4.members)
        self.assertEqual("Member with name  does not exist", result2)
        self.assertEqual(0, len(self.team4.members))

    def test_greater_than_returns_true_for_for_self_with_more_members(self):
        result = self.team1 > self.team2
        self.assertTrue(result)
        self.assertEqual(True, result)

    def test_greater_than_returns_false_for_self_with_less_or_equal_members(self):
        result = self.team2 > self.team1
        self.assertFalse(result)
        self.assertEqual(False, result)
        result2 = self.team1 > self.team3
        self.assertFalse(result2)
        self.assertEqual(False, result2)

    def test_len_returns_correct_number_of_members(self):
        self.assertEqual(4, len(self.team1))
        self.assertEqual(3, len(self.team2))
        self.team2.remove_member("Someguy2")
        self.assertEqual(2, len(self.team2))
        self.team2.remove_member("Someguy2")
        self.assertEqual(2, len(self.team2))
        self.assertEqual(0, len(self.team4))
        self.team4.add_member(Defne=10)
        self.assertEqual(1, len(self.team4))
        self.assertEqual(len(self.team1.members), len(self.team1))

    def test_add_correctly_merges_teams(self):
        result = self.team1 + self.team3
        self.assertTrue(isinstance(result, Team))
        self.assertEqual("HottiesCoolGals", result.name)
        self.assertEqual({
            "Nalan": 44,
            "Tanya": 42,
            "Elena": 36,
            "Sultan": 41,
            "Gal1": 24,
            "Gal2": 33,
            "Gal3": 46,
            "Gal4": 28
        }, result.members)
        self.assertEqual(8, len(result))

        result2 = self.team1 + self.team5
        self.assertTrue(isinstance(result2, Team))
        self.assertEqual("HottiesOnFire", result2.name)
        self.assertEqual({
            "Nalan": 44,
            "Tanya": 42,
            "Elena": 36,
            "Sultan": 41,
        }, result2.members)
        self.assertEqual(4, len(result2))

        result3 = result2 + self.team6
        self.assertTrue(isinstance(result3, Team))
        self.assertEqual("HottiesOnFireEmpty", result3.name)
        self.assertEqual({
            "Nalan": 44,
            "Tanya": 42,
            "Elena": 36,
            "Sultan": 41,
        }, result2.members)
        self.assertEqual(4, len(result3))

    def test_str_returns_correct_output(self):
        self.team1.add_member(Ozge=41)
        output = str(self.team1)
        expected = "Team name: Hotties\n" \
                   "Member: Nalan - 44-years old\n" \
                   "Member: Tanya - 42-years old\n" \
                   "Member: Ozge - 41-years old\n" \
                   "Member: Sultan - 41-years old\n" \
                   "Member: Elena - 36-years old"

        self.assertEqual(expected, output)

        self.team1.members = {}
        output2 = str(self.team1)
        expected2 = "Team name: Hotties"

        self.assertEqual(expected2, output2)


if __name__ == "__main__":
    main()

