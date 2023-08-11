from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal(
            "Gizmo",
            "Cat",
            "Meow"
        )

    def test_correct_initialization(self):
        self.assertEqual("Gizmo", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("Meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_returns_correct_info(self):
        self.assertEqual("Gizmo makes Meow", self.mammal.make_sound())

    def test_get_kingdom_returns_correct_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_returns_correct_info(self):
        self.assertEqual("Gizmo is of type Cat", self.mammal.info())


if __name__ == "__main__":
    main()
