from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Ondurdis", 1, 100, 100)
        self.enemy = Hero("Rockwind", 2, 50, 50)

    def test_correct_initialization(self):
        self.assertEqual("Ondurdis", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_attack_self_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_remove_enemy_health_after_battle(self):
        self.hero.battle(self.enemy)
        self.assertEqual(-50, self.enemy.health)

    def test_remove_hero_health_after_battle(self):
        self.hero.battle(self.enemy)
        self.assertEqual(0, self.hero.health)

    def test_attack_with_low_health_raises_val_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0."
                         " You need to rest", str(ve.exception))

    def test_enemy_with_low_health_raises_val_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Rockwind. He needs to rest",
                         str(ve.exception))

    def test_draw_condition_works(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

    def test_you_win_condition_works(self):
        self.hero.level = 4
        self.enemy.level = 1

        result = self.hero.battle(self.enemy)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual("You win", result)

    def test_enemy_won_condition_works(self):
        self.hero = Hero("Ondurdis", 1, 100, 100)
        self.enemy = Hero("Rockwind", 5, 150, 50)

        result = self.hero.battle(self.enemy)
        self.assertEqual(6, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(55, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_str_returns_correct_info(self):
        self.assertEqual("Hero Ondurdis: 1 lvl\n"
                         "Health: 100\n"
                         "Damage: 100\n", str(self.hero))


if __name__ == "__main__":
    main()
